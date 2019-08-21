name = raw_input('Enter a Name :')
start = 0
end = len(name)-1
while end>=start:
    print name[end],
    end-=1
    