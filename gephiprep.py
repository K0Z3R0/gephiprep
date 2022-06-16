import numpy as np
import pandas as pd
import argparse
#converts dataset into two files nodes.csv and edges.csv

cmd_parse = argparse.ArgumentParser(description='Creates nodes and edge file from a csv file for gephi')
cmd_parse.add_argument('file',metavar='File',type=str,help='the path to list')

required = cmd_parse.add_argument_group('required arguments')
required.add_argument("-s","--source",type=str,required=True,help='The source column name')
required.add_argument("-d","--dest",type=str,required=True,help='The destination column name')

optional = cmd_parse.add_argument_group('optional arguments')
optional.add_argument("-w","--weight",type=str,required=False,help='The weight column name')

args = cmd_parse.parse_args()
col_list = [args.source,args.dest]

if args.weight is not None:
    col_list.append(args.weight)

df = pd.read_csv(args.file,sep=',',usecols=col_list)#nrows
nodes = pd.DataFrame()
nodes["label"] = pd.unique(pd.concat([df[args.source],df[args.dest]]))
nodes.insert(0,"id",nodes["label"])
nodes.insert(1,"node",nodes["label"])
edges = pd.DataFrame(columns=["source","target","type","weight"], index=range(0,df[args.source].shape[0]))
edges["source"]= df[args.source]
edges["target"] = df[args.dest]

edges.index.name = "id"
edges["type"] = np.repeat("Directed",(edges["source"]).shape[0])
if args.weight is not None:
    edges["weight"] = df[args.weight]
else:
    edges["weight"] = np.repeat("1",(edges["source"]).shape[0])

nodes.to_csv("nodes.csv",index=False)
edges.to_csv("edges.csv",index=False)
    

