'''
k Nearest Neighbours (kNN) Algorithm

Author:		Delostik
Version:	0.1
Date:		20141028

In this version it can only do some easy kNN algorithm on the plane.
'''

from matplotlib import pyplot
from random import random
import numpy as np

'''
This function randomly create data
	`DataSize` denotes to the number of the points.
	`Demension` denotes to the demension of the plane.
	`Interval` is a set of pairs, each pair defines the 
		upperbound and the lowerbound of the data.
	`Type` is a set of types, which points belongs.
'''
def createData(DataSize = 10, Demension = 2, Interval = [], Type = ['A', 'B']):
	data = []
	if Interval == []: Interval = [(0, 1)] * Demension
	for i in range(DataSize):
		point = []
		for x in range(Demension):
			point.append(random() * (Interval[x][1] - Interval[x][0]) + Interval[x][0])
		point.append(Type[int(round(random() * Type.__len__()))])
		point.append(0)		# for distance
		data.append(point)
	return data


'''
This function classify the new element.
'''
def classify(DataSet, NewElem, CalcDistFunc, k = 15):
	DataSize = DataSet.__len__()
	for i in range(DataDistSet.__len__()):
		DataSet[3] = CalcDistFunc(DataSet[i], NewElem)
	DataSet = (DataSet.sort(key = lambda(x: x[3])))[:k]
	TypeDict = {}
	for i in DataSet:
		if i in TypeDict: TypeDict[i]++
		else: TypeDict[i] = 1
	return sorted(TypeDict.items(), key = lambda x: -x[1])[0][0]


