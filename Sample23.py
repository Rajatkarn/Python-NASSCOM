name = 'WelCOmE'
start,end = 0,len(name)-1
while start<=end:
    if name[start].islower():
        print name[start]
    start+=1