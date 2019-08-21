name = 'We$lc#om!e@'
start,end=0,len(name)-1
while start <=end:
    if not name[start].isalpha():
        print name[start]
    start+=1
