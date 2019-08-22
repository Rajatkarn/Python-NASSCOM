name = 'education'
start,end = 0,len(name)
temp =''

for ch in name:
    if ch in ('a','e','i','o','u'):
        if not ch in temp:
            temp+=ch
            
if len(temp)==5:
    print ' All Vowels are Present'
else:
    print ' All Vowels are not Present'