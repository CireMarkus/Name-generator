import random

class Namegenertor():
	def __init__(self):
		self.first_names = []
		self.last_names = []
		self.list_populator()
		self.generator()
		
	#populates the list in the name generator class with then names from the files.
	def list_populator(self):
		first_name_file = open('first_name_list.txt','r')
		last_name_file = open('last_name_list.txt','r')

		for first_name in first_name_file.readlines():
			self.first_names.append(first_name)

		for last_name in last_name_file.readlines():
			self.last_names.append(last_name)
			
	#generates a random name from the names in the files.
	def generator(self):
		first = self.first_names[random.randint(0,len(self.first_names)-1)]
		last = self.last_names[random.randint(0,len(self.last_names)-1)]

		print (first.strip('\n') + ' ' + last.strip('\n'))

Namegenertor()