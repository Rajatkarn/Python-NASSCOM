name = raw_input('Enter a String : ')
start,end = 0,len(name)
for var in range(start,end):
    if name[var].isupper():
        print name[var].lower(),
    else:
        print name[var].upper(),
    