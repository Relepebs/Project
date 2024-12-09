class BookStore():
	def __init__(self):

		self._Books = {} 
		self._Name = "n"
		self._Author = "n"
		self._Price = float(0)
		self._Cash = float(2000)


	def add(self):
		self._Name = input("Enter Name of book: ").upper()
		self._Author = input("Enter Author's name: ").upper()
		if self._Author:
			self._Price = input("Price $: ")
			self._Books[self._Name] = {'Author': self._Author, 'Price': self._Price}
			print (self._Books)
		
			
	def sell(self):
		self._Name = input("enter the name of the book you would like to sell: \n").upper()
		if self._Name in self._Books:
			self._Books.pop(self._Name)
	def values(self):
		for a in self._Books:
			print(a , self._Books[a]["Author"] )
			print(self._Books [a]["Price"])

	def 
	
		


	

	


	def qui(self, foop):
		self._foop = False
		return self._foop




'''import os
	filepath = os.getcwd()
	def MakeFile(file_name):
			temp_path = filepath + file_name
	with open("file._name", "w") as f:
			f.write('def print_success(): print "success"'')
			print ("Saved file")'''









"""class TAX():
    def __int__ (self):
       
        self._list = 0
        self._author = "n"
        self._name = "n"
        self._price = float(0)
    def add(self):
        self._rele = {}
        self._name= input("Enter book name:")
        self._author= input("Author:")
        self._price= input("Price:$")
        print(self._name)
        self._rele[self._name] = {}
        

    def sell(self):
        self._name = input("Name of book to sell:")
        self._price = input("Price:$")"""