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
dic=histogram(lst2) # dict of crime ID , and repetation of it

"""make dict of Crime Id vs Crime name"""
lst4=list(dic.keys())
for i in range(len(lst1)):
	if lst1[i] in lst4:
		dict[lst1[i]]=lst1[i+1].strip()

"""print table"""
print("{0:25s} {1:25s} {2:1s}".format('Crime type','Crime ID','Crime Count'))
for key,value in dic.items():
	if key in dict.keys():
		print("{0:25} {1:25} {2:1}".format(dict[key],key,dic[key]))
