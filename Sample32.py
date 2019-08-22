name = 'Welcom3 t0 Py7hon and Jav4'
start,end,uc,lc,d,sc = 0,len(name)-1,0,0,0,0
while start <=end:
    if name[start].isupper():
        uc+=1
    if name[start].islower():
        lc+=1
    if name[start].isdigit():
        d+=1
    if not name[start].isalnum():
        sc+=1
    start+=1
print 'Number of UpperCase Characters : ',uc
print 'Number of LowerCase Characters : ',lc
print 'Number of Digit Characters : ',d
print 'Number of Special Characters : ',sc