name = 'Wel2come1Surya345'
start =0
end = len(name)-1
while start <=end:
    if name[start].isdigit():
        print name[start],
    start+=1
print ''
print '************************************'    
start =0
while start <=end:
    if name[start].isalpha():
        print name[start],
    start+=1