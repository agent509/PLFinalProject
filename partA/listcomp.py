def sortby(table,item):
    index = table[0].index(item)
    head=table[0]
    table = table[1::]

    print
    table.sort(key = lambda x:x[index])
    return [head]+table

def select(table,items):
    indices =[table[0].index(i) for i in items]
    return[[x[i] for i in indices] for x in table[1::]]
  

def gettable(filename):

    f = open(filename,'r')
    table = []
  
    for line in f:
        row = line.rstrip('\n').split()
        table.append(row)

    return table

#def join(tab1,tab2,onel):



