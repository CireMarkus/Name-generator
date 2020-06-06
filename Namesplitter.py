class Namesplitter():
	def __init__(self,filename):
		self.raw_name_data = open(str(filename)+'.txt','r')
		self.first_names = []
		self.last_names = []
		self.get_names_from_file()
		self.quick_sort(self.first_names,0,len(self.first_names)-1)
		self.quick_sort(self.last_names,0, len(self.last_names)-1)
		self.write_names_to_files()
		self.raw_name_data.close()


	def get_names_from_file(self):
		for fullnames in self.raw_name_data:
			name  = fullnames.split()
			self.first_names.append(name[0])
			self.last_names.append(name[1])

	def insertion_sort(self):
		for index in range(1,len(self.first_names)):
			search_index = index
			insert_value = self.first_names[index]

			#while loop is only entered if the search_index is not the first value of the list
			# and if the value below the current search index is less than the insert value. 
			# This algorithm is effectifly traversing the list backwards and seeing if it can sort the values.
			while search_index > 0 and self.first_names[search_index-1] > insert_value:
				self.first_names[search_index] = self.first_names[search_index-1]
				search_index-=1

			self.first_names[search_index] = insert_value

		for index in range(1, len(self.last_names)):
			search_index = index
			insert_value = self.last_names[index]

			while search_index > 0 and self.last_names[search_index-1] > insert_value: 
				self.last_names[search_index] = self.last_names[search_index-1]
				search_index-=1
			self.last_names[search_index] = insert_value

	def selction_sort(self):
		#The algorithm goes through each element in the list and compares it to 
		# all of the elements in the list after it. 
		for i in range (len(self.first_names)):
			for j in range (i+1, len(self.first_names)):
				#If any of the elements in the list after the index are smaller than the value
				# at the index then the elements are swapped. 
				#This is a very inefficent form of the bubblesort in my opinion. 
				if self.first_names[j]<self.first_names[i]:
					temp = self.first_names[i]
					self.first_names[i] = self.first_names[j]
					self.first_names[j] = temp

	def quick_sort(self,unsorted_array,first,last):
		if last - first <= 0:
			return 
		else:
			partition_point=self.partition(unsorted_array,first,last)
			self.quick_sort(unsorted_array,first,partition_point-1)
			self.quick_sort(unsorted_array,partition_point+1,last)

		
	def partition(self,unsorted_array,first_index,last_index):
		pivot = unsorted_array[first_index]
		pivot_index = first_index
		index_of_last_element = last_index

		less_than_pivot_index = index_of_last_element
		greater_than_pivot_index = first_index+1

		while True: 
			while unsorted_array[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
				greater_than_pivot_index +=1

			while unsorted_array[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
				less_than_pivot_index -= 1

			if greater_than_pivot_index < less_than_pivot_index:
				temp =unsorted_array[greater_than_pivot_index]
				unsorted_array[greater_than_pivot_index] =unsorted_array[less_than_pivot_index]
				unsorted_array[less_than_pivot_index] = temp	
			else:
				break
		unsorted_array[pivot_index] = unsorted_array[less_than_pivot_index]
		unsorted_array[less_than_pivot_index] = pivot
		return less_than_pivot_index


	def write_names_to_files(self):
		first_name_file = open('first_name_list.txt','w')
		last_name_file = open('last_name_list.txt','w')

		for first_name in self.first_names:
			first_name_file.write(first_name + '\n')
		first_name_file.close()
		for last_name in self.last_names:
			last_name_file.write(last_name+'\n')
		last_name_file.close()


Namesplitter('Namelist')