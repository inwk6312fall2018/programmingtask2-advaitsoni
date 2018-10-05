"""Can you list the crimes according to the dates? 
Can you order them by most recent crime first and display it? """

lst_words=[]	#contains all words
lst_data=[]	#contains tuple of location,crime id, crime name
file = open('crime.txt')

#to store all words in lst_words
for line in file:
	line=line.strip()
	for word in line.split(','):
		lst_words.append(word)

#to store tuple of location, crime id, crime name, date
i=14
while i<len(lst_words)-4:
	lst_data.append((lst_words[i],lst_words[i+1],lst_words[i+2],lst_words[i+3]))
	i+=9

#print most recent crime first 	
print("{0:35s} {1:35s} {2:10s} {3:1s}".format("Date","location","crime ID","Crime type"))
for i in sorted(lst_data)[::-1]:
		print("{0:35} {1:35} {2:10} {3:1}".format(i[0],i[1],i[2],i[3]))
