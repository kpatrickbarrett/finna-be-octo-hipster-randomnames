import random, linecache

fname = open("fnames.txt", "r")
lname = open("lnames.txt", "r")


#first = fname.readline(random.randint(0,5164))
#last = lname.readline(random.randint(0,88800))

hyphenCheck = random.randint(0,100)
first =  linecache.getline('lnames.txt', (random.randint(0,93963)))
last =  linecache.getline('lnames.txt', (random.randint(0,94000)))
lastHyphen =  linecache.getline('lnames.txt', (random.randint(0,94000)))

if hyphenCheck > 75:
	print((first.rstrip())+" "+(last.rstrip())+"-"+lastHyphen)

else:
	print((first.rstrip())+ " " + last)
