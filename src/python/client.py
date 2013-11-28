import sys, json
from jubatus.clustering import client
from jubatus.clustering import types
from jubatus.common import Datum

NAME = "clustering_compounds"
if __name__ == '__main__':
    clustering = client.Clustering("127.0.0.1", 9199, NAME)

    for line in open("../../bench_data/demo4096.smi"):
        smiles, id = line.split(" ")
        datum = Datum()
        datum.add_string("SMILES", smiles)
        clustering.push([datum])
    center_list = clustering.get_k_center()
    members = clustering.get_core_members()
    for i in range(0,4):
        for j in range(len(members[i])):
            print "%d, %d, %s " %(i, j, members[i][j])
#    print "%s \n" % center_list[4]
#    for i in range(len(center_list)):
#        print "%s \n" % center_list[i]
