badlist = open('lastnames.txt', 'r')
newlist = open('lnames.txt' , 'w')


for line in badlist.readlines():
	x = line.split(" ", 1)[0]
	newlist.write(x+"\n")
