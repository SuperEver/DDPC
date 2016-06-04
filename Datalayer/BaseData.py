#coding:utf-8
import os
import DataPath
cluster_map = {}

with open(os.path.join(DataPath.map_path, DataPath.map_prefix), 'r') as f:
    for line in f:
        strArr=line.strip().split()
        assert len(strArr) == 2
        cluster_map[strArr[0]] = strArr[1]
    f.close()

