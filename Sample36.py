name = raw_input('Enter a String : ')
start,end,temp = 0,len(name),0
for var in range(start,end):
    if name[var] in ('a','e','i','o','u'):
        temp+=1
if temp>0:
    print 'Vowels are Present'