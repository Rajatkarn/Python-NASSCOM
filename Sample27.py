name = 'Welcome'
start,end =0,len(name)-1
while start<=end:
    if name[start] in ('a','e','i','o','u','A','E','I','O','U'):
        print name[start],
    start+=1