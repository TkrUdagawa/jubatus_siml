import sys, json
from jubatus.clustering import client
from jubatus.clustering import types
from jubatus.common import Datum

NAME = "clustering_compounds"
if __name__ == '__main__':
    clustering = client.Clustering("127.0.0.1", 9199, NAME)

    datum = Datum()
    datum.add_string("SMILES", "cccccccc")
    print clustering.get_nearest_center(datum)
#    print "%s \n" % center_list[4]
#    for i in range(len(center_list)):
#        print "%s \n" % center_list[i]
