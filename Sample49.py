def Table():
    num = (int)(raw_input('enter a Number :'))
    start , end = 1,11
    for i in range(start , end):
        print num,'*',i,'=',num*i
        
def Even_Odd():
    num = (int)(raw_input('enter a Number :'))
    if num%2==0:
        print num,'is Even Number'
    else:
        print num,'is Odd Number'

Table()
Even_Odd()