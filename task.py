file=open('Crime.csv')
lst1=[]	#to store all words
lst2=[]
dict={}	#take crime id as key and crime name as value

def histogram(s):
	"""to check number of repetation of s in string"""
	d={}
	for c in s:
		d[c]=1+d.get(c,0)
	return d

"""make list of all words"""
for line in file:
	line.strip()
	for i in line.split(','):
		lst1.append(i)

"""make list of all the crime ID"""
i=16
while i<len(lst1):
	lst2.append(lst1[i])
	i+=9
lst3=histogram(lst2) # dict of crime ID , and repetation of it

"""make dict of Crime Id vs Crime name"""
lst4=list(lst3.keys())
for i in range(len(lst1)):
	if lst1[i] in lst4:
		dict[lst1[i]]=lst1[i+1].strip()

"""print table"""
print("Crime Type",end=' '*15)
print("Crime ID",end=' '*17)
print("Crime Count",end='\n')
for key,value in lst3.items():
	if key in dict.keys():
		print(dict[key],end=' '*(25-len(dict[key])))
		print(key,end=' '*(25-len(key)))
		print(lst3[key],end='\n')
