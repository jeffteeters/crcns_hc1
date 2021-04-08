# script to compute recording time for files in hc-1 dataset
import re
import xml.etree.ElementTree as ET
import os
import pprint
import sys
pp = pprint.PrettyPrinter(indent=4)
import pandas as pd


class ExcelData:
    # loads data from IntraExtra.xls
    def __init__(self, filename="IntraExtra.xls"):
        self.filename = filename
        dfs = pd.read_excel(filename, sheet_name="Sheet1")
        columns = ['cell', 'recording time', '# of files', 'nChannels']
        self.columns = columns
        df = pd.DataFrame(dfs, columns=columns)
        self.df = df

    def get_data(self, cell):
        cell = "D" + cell[1:]  # make sure starts with "D"
        dfr = self.df.loc[self.df['cell'] == cell]
        if len(dfr) == 1:
            vals = {}
            for col in self.columns:
                val = dfr[col].values[0]
                vals[col] = val
        else:
            vals = None
        return vals


class Recording:
    # stores info about particular cell (including all .dat files for that cell)

    num_intraExtra = 0  # number of recordings that have a row in IntraExtra.xls file

    def __init__(self, zipfile, ie_data):
        self.zipfile = zipfile
        self.datfiles = []
        self.channels_consistent = None
        self.recording_time = None
        self.intraExtra_rt = None  # recording time in IntraExtra spreadsheet, or None
        self.ied = ie_data.get_data(self.zipfile)
        if self.ied:
            Recording.num_intraExtra += 1
        self.stats = None

    def add_dat_file(self, name, size, nChannels, samplingRate):
        if nChannels is not None:
            timeMin = size / (2 * nChannels * samplingRate * 60.0)
        else:
            timeMin = 0.0
        self.datfiles.append( [name, size, nChannels, samplingRate, timeMin])

    def calculate_stats(self):
        if self.stats is not None:
            # already have stats
            return
        rt = 0.0
        first_nChannels = None
        channels_consistent = True
        for dati in self.datfiles:
            name, size, nChannels, samplingRate, timeMin = dati
            if nChannels is not None:
                rt += timeMin
                if first_nChannels is None:
                    first_nChannels = nChannels
                else:
                    if first_nChannels != nChannels:
                        channels_consistent = False
        self.stats = {
            "num_files": len(self.datfiles),
            "rt": rt,
            "first_nChannels": first_nChannels,
            "channels_consistent": channels_consistent,
            }

    def display(self, idstr=""):
        # idstr used to display count before the cell name
        self.calculate_stats()
        print("\n%s%s" % (idstr, self.zipfile))
        print("name\tsize\tchannels\tsamplingRate\tminutes")
        for df in self.datfiles:
            print("%s\t%s\t%s\t%s\t%s" % (df[0], df[1], df[2], df[3], round(df[4], 2)))
        cc_msg = "" if self.stats["channels_consistent"] else ", number of channels inconsistent"
        xm_msg = " (xml file missing)" if self.stats["first_nChannels"] is None else ""
        print("%s files, total time=%s%s%s"% (self.stats["num_files"], round(self.stats["rt"],2), cc_msg, xm_msg))
        if self.ied:
            mismatch = []
            mismatch.append("recording time %s" % self.ied["recording time"])
            if not (self.ied["# of files"].isdigit() and int(self.ied["# of files"]) == self.stats["num_files"]):
                mismatch.append("#_of_files '%s'" % self.ied["# of files"])
            if not self.stats["channels_consistent"] or self.stats["first_nChannels"] != self.ied["nChannels"]:
                mismatch.append("nChannels %s" % self.ied["nChannels"])
            mismatch = ", ".join(mismatch)
            print("differing intraExtra values: %s" % mismatch)

    def display_recTimeDiff_header():
        print("\nintraExtra.xls recording time difference (times are in minutes)")
        print("cell\tintraExtra\tactual\tdiff")

    def display_recTimeDiff(self):
        self.calculate_stats()
        if self.ied is not None:
            ied_rt = self.ied["recording time"]
            act_rt = self.stats["rt"]
            diff = ied_rt - act_rt
            print("%s\t%s\t%s\t%s" % (self.zipfile, ied_rt, round(act_rt, 2), round(diff, 2)))

class Datreader:
    # load info for all dat files into datinfo, each element is a Recording object
    def __init__(self, topdir, datinfofile, xmldir):
        self.topdir = topdir
        self.xmldir = xmldir
        self.ie_data = ExcelData()
        datinfo = {}
        filepath = os.path.join(topdir, datinfofile)
        with open(filepath) as f:
            for line in f:
                # d11221.zip.txt: 90000000  02-14-2008 16:45   d11221/d11221.001.dat
                m = re.match("(d\d+)\.zip\.txt:\s*(\d+)[^d]+(d\d+)/(d\d+.+dat)\s*", line)
                if m is None:
                    sys.exit("could not match line '%s'" % line)
                zipfile = m.group(1)
                datsize = int(m.group(2))
                dirname = m.group(3)
                datname = m.group(4)
                assert zipfile == dirname
                if zipfile not in datinfo:
                    datinfo[zipfile] = Recording(zipfile, self.ie_data)
                nChannels, samplingRate = self.get_xml_info(dirname, datname)
                datinfo[zipfile].add_dat_file(datname, datsize, nChannels, samplingRate)
        # print("datinfo is")
        self.datinfo = datinfo
        # pp.pprint(datinfo)


    def get_xml_info(self, dirname, datname):
        xmlname = datname[0:-3] + "xml"
        path = os.path.join(self.topdir, self.xmldir, dirname, xmlname)
        if not os.path.isfile(path):
            # print("unable to file file: '%s'" % path)
            return [None, None]
        tree = ET.parse(path)
        root = tree.getroot()
        nChannels = int(root.find('./acquisitionSystem/nChannels').text)
        samplingRate = int(root.find('./acquisitionSystem/samplingRate').text)
        return(nChannels, samplingRate)

    def display(self):
        print("\n** crcns.org hc-1 dataset files")
        count = 0
        for dr in sorted(self.datinfo):
            count += 1
            idstr = "%s. " % count
            self.datinfo[dr].display(idstr)

    def display_rt_diff(self):
        Recording.display_recTimeDiff_header()
        for dr in sorted(self.datinfo):
            self.datinfo[dr].display_recTimeDiff()

    def display_intraExtra_counts(self):
        num_cells = len(self.datinfo)
        print("%s cells, %s in IntraExtra, %s not in IntraExtra" % (num_cells, Recording.num_intraExtra, 
            num_cells - Recording.num_intraExtra))

def main():
    topdir = "data_size_info"
    datinfofile = "datfiles.txt"
    xmldir = "xmlnrs"
    dr = Datreader(topdir, datinfofile, xmldir)
    dr.display()
    dr.display_rt_diff()
    dr.display_intraExtra_counts()


if __name__ == "__main__":
    main()

