num , start = (int)(raw_input('Enter a Number : ')),1
print 'Factors of',num,'is :',
for var in range (start,num+1):
    if num%var ==0:
        print var,