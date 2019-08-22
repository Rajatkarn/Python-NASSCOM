num = (int)(raw_input('Enter a Number : '))
start,temp =1,0
for var in range(start,num+1):
    if num%var ==0:
        temp+=1
if temp == 2:
    print num,'is Prime Number'
else:
    print num,'is not a Prime Number'
    