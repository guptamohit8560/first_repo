class book():
	def __init__(self,bname,byear,bauthor):
		self.bname= bname
		self.byear=byear
		self.bauthor= bauthor
	def b_name(self):
		self.bname= self.bname + 'mohit'


a= book('ASOIAF',2012,'GRRM')

a.publish=2018

print (a.__dict__)

a.b_name()

print (a.__dict__)

print ("hii mohit")
print (""second time"")
