# script to compute recording time for files in hc-1 dataset
import re
import xml.etree.ElementTree as ET
import os
import pprint
import sys
pp = pprint.PrettyPrinter(indent=4)
import pandas as pd


class ExcelData:
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
    def __init__(self, zipfile, ie_data):
        self.zipfile = zipfile
        self.datfiles = []
        self.channels_consistent = None
        self.recording_time = None
        self.intraExtra_rt = None  # recording time in IntraExtra spreadsheet, or None
        self.ie_data = ie_data

    def add_dat_file(self, name, size, nChannels, samplingRate):
        self.datfiles.append( [name, size, nChannels, samplingRate])

    def calculate_stats(self):
        rt = 0.0
        cur_nChannels = None
        channels_consistent = True
        for dati in self.datfiles:
            name, size, nChannels, samplingRate = dati
            if nChannels is not None:
                timeMin = size / (2 * nChannels * samplingRate * 60.0)
                rt += timeMin
                if cur_nChannels is None:
                    cur_nChannels = nChannels
                else:
                    if cur_nChannels != nChannels:
                        channels_consistent = False
                        print("nChannels in %s is not consistent, %s vs %s" % (name, cur_nChannels, nChannels))
        self.stats = {
            "num_files": len(self.datfiles),
            "rt": rt,
            "channels_consistent": channels_consistent,
            }

    def display(self):
        self.calculate_stats()
        print("\n%s files:" % self.zipfile)
        print("name\tsize\tchannels\tsamplingRate")
        for df in self.datfiles:
            print("%s\t%s\t%s\t%s" % (df[0], df[1], df[2], df[3]))
        print("%s files, total time=%s, channels_consistent=%s"% (self.stats["num_files"], round(self.stats["rt"],2),
            self.stats["channels_consistent"]))
        ied = self.ie_data.get_data(self.zipfile)
        if ied:
            print("intraExtra values: %s" % ied)
        else:
            print("Not in IntraExtra")

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
            print("unable to file file: '%s'" % path)
            return [None, None]
        tree = ET.parse(path)
        root = tree.getroot()
        nChannels = int(root.find('./acquisitionSystem/nChannels').text)
        samplingRate = int(root.find('./acquisitionSystem/samplingRate').text)
        return(nChannels, samplingRate)

    def display(self):
        for dr in sorted(self.datinfo):
            self.datinfo[dr].display()


    # def calculate_rt(self):
    #     # calculate recording time
    #     rctimes = {}
    #     for xmldir in self.datinfo:
    #         rt = 0.0
    #         cur_nChannels = None
    #         for dati in self.datinfo[xmldir]:
    #             datname, datsize, nChannels, samplingRate = dati
    #             if nChannels is not None:
    #                 timeMin = datsize / (2 * nChannels * samplingRate * 60.0)
    #                 rt += timeMin
    #                 if cur_nChannels is None:
    #                     cur_nChannels = nChannels
    #                 elif cur_nChannels != nChannels:
    #                     print("nChannels in %s is not consistent, %s vs %s" % (datname, cur_nChannels, nChannels))
    #         rctimes[xmldir] = rt
    #     self.rctimes = rctimes
    #     print("rctimes is:")
    #     for xmldir in sorted(self.rctimes):
    #         print("%s\t%s" % (xmldir, round(rctimes[xmldir], 2)))


def main():
    topdir = "data_size_info"
    datinfofile = "datfiles.txt"
    xmldir = "xmlnrs"
    dr = Datreader(topdir, datinfofile, xmldir)
    dr.display()


if __name__ == "__main__":
    main()

