#coding:utf-8
import os
import DataPath
import BaseData
import Util
import cPickle as pickle

def generateLabel():
    mapLabel = {}


    outpath = os.path.join(DataPath.runtime_path, DataPath.label_filename)
    outf = open(outpath, 'w')
    for datename in DataPath.traindata_list:
        parseFileAppend(datename, mapLabel)
    pickle.dump(mapLabel, outf)
    outf.close()

def parseFileAppend(datename, mapLabel):

    for clustid in BaseData.cluster_map.values():
        for slotid in range(1, 145):
            label_key = '%s,%d,%s'%(datename, slotid, clustid)
            mapLabel[label_key] = [0, 0]
    filename = os.path.join(DataPath.order_path, DataPath.order_prefix + '_' + datename)
    assert os.path.exists(filename)
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        wordArr = line.strip().split('\t')
        assert len(wordArr) == 7
        start_clusterid = BaseData.cluster_map.get(wordArr[3])
        assert start_clusterid is not None
        slotid = Util.time2Slot(wordArr[6].split(' ')[1])
        keyCur = '%s,%d,%s'%(datename, slotid, start_clusterid)
        valueList = mapLabel.get(keyCur)
        assert valueList is not None
        valueList[0] += 1
        if wordArr[1] != 'NULL':
            valueList[1] += 1
        mapLabel[keyCur] = valueList
    # nSumReq = 0
    # nSumAns = 0
    # for numList in mapLabel.values():
    #     nSumReq += numList[0]
    #     nSumAns += numList[1]
    # print nSumReq, nSumAns
    # print mapLabel