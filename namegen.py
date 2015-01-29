import random, linecache

fname = open("fnames.txt", "r")
lname = open("lnames.txt", "r")


#first = fname.readline(random.randint(0,5164))
#last = lname.readline(random.randint(0,88800))

first =  linecache.getline('lnames.txt', (random.randint(0,93963)))
last =  linecache.getline('lnames.txt', (random.randint(0,94000)))

print((first.rstrip())+ " " + last)