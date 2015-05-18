from datapoint import DataPoint
from dataset import DataSet
class Machine:
	#"folder" is a string location of the dataset
	def __init__(self, folder):
		self.dataset = DataSet(None, folder)
	def run(self):
		print "nothing"
