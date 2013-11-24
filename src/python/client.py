import sys, json
from jubatus.clustering import client
from jubatus.clustering import types


NAME = "clustering_compounds"
if __name__ == '__main__':
    clustering = client.Clustering("127.0.0.1", 9199, NAME)

    for line in open("../../bench_data/demo4096.smi"):
        smiles, id = line.split(" ")
        datum = types.Datum()
#        datum.add_string("ID", id)
        datum.add_string("SMILES", smiles)
        clustering.push(datum)
    center_list = clustering.get_k_center()
    for center in center_list:
        print center
