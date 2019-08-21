name = 'weLcOmE RajAt'
start,end=0,len(name)-1
temp =''
while start <=end:
    if name[start].isupper():
        temp+=name[start].lower()
    else:
        temp+=name[start].upper()
    start+=1
print temp