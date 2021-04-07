# script to compute recording time for files in hc-1 dataset
import re
import xml.etree.ElementTree as ET
import os
import pprint
import sys
pp = pprint.PrettyPrinter(indent=4)


class Datreader:

    def __init__(self, topdir, datinfofile, xmldir):
        self.topdir = topdir
        self.xmldir = xmldir
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
                    datinfo[zipfile] = []
                nChannels, samplingRate = self.get_xml_info(dirname, datname)
                dati = [datname, datsize, nChannels, samplingRate]
                datinfo[zipfile].append( dati )
        print("datinfo is")
        self.datinfo = datinfo
        pp.pprint(datinfo)

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


def main():
    topdir = "data_size_info"
    datinfofile = "datfiles.txt"
    xmldir = "xmlnrs"
    dr = Datreader(topdir, datinfofile, xmldir)


if __name__ == "__main__":
    main()

