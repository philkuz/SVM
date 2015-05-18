import csv 
from datapoint import DataPoint

class DataSet:
	# Description: The DataSet constructor that takes in either a list of datapoints or a folder location. If it takes both, the datapoints take precedent. Useful initializations of type DataSet will look like this:
		#DataSet(datapoints)
			#OR
		#DataSet(None, "data.txt")
	# "datapoints" is a list of the type DataPoint
	# "filename" is the file location of a dataset in tab delineated form, where the last input is the classification.
	def __init__(self, datapoints = None, filename = None):
		if datapoints is None:
			if filename is None:
				raise ValueError("There are no parameters with datapoints or filename or filename in which to look for datapoints")
			else:
				# TODO
				f = open(filename, 'r')
				datapoints = []
				for line in f:
					ipt = line.split(",")
					vector = map(double, ipt[0].toCharArray())
					classification = (int)ipt[1]

					datapoints.append(DataPoint(vector, classificiation))
		else:
			self.datasets = datapoints


