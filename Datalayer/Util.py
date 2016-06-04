#coding:utf-8

def time2Slot(strTime):
    strArr = strTime.split(':')
    slot = int(strArr[0]) * 6 + int(strArr[1]) / 10 + 1
    return slot