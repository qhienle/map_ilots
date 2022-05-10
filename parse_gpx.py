#!/usr/bin/env python3
"""
Extract Trackpoints from GPX files as CSV.

USAGE: extract_gpx_trackpoints.py --help # And the rest will be handled by library `argparse`
"""
import argparse
import xml.etree.ElementTree as ET

__version__ = "0.1"

def parse_args():
    """
    Parse command-line options
    """
    parser = argparse.ArgumentParser(description="Extract Trackpoints from GPX files as CSV.")
    parser.add_argument('gpx_file', help="GPX file [REQUIRED]")
    return(parser.parse_args())

def get_trkseg(gpx):
    """
    Search the GPX tree to find Element 'trkseg', which holds the trackpoints
    """
    tree = ET.parse(gpx)
    root = tree.getroot()
    for child_L1 in root:
        print(f"A tag in L1: {child_L1.tag}")
        if child_L1.tag.match('trk'):            
            for child_L2 in child_L1:
                print(child_L2.tag)
                if child_L2.tag == 'trkseg':
                    return(child_L2)
    return("Not Found!")
    # This is supposed to find interesting elements, but does nothing
    # for trkpt in root.iter('trkpt'):
    #    print(trkpt.attrib)

if __name__ == '__main__':
    args = parse_args()
    # Retrieve all the "trkpt" elements located under the XPath "/gpx/trk/trkseg/"
    # Send to STDOUT as CSV
    #
    #trkseg = get_trkseg(args.gpx_file)
    #print(trkseg)
    tree = ET.parse(args.gpx_file)
    root = tree.getroot()
    trkseg = root[1][0] # TODO: Doesn't work for Strava GPX
    print(','.join(['time', 'elevation', 'latitude', 'longitude']))
    for trkpt in trkseg:
        time = trkpt[1]
        elev  = trkpt[0]
        print(','.join([time.text, trkpt.attrib['lat'], trkpt.attrib['lon'], elev.text]))
