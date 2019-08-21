name = 'WElCome RaJaT'
start,end =0,len(name)-1
while start <= end:
    if name[start].isupper():
        print name[start].lower(),
    else:
        print name[start].upper(),
    start+=1