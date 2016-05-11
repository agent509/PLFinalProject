def sortby(lis,i):

  lis.sort(key = lambda x:x[i])
  return lis

def select(table,items):
  indices =[table[0].index(i) for i in items]
  return[[x[i] for i in indices] for x in table[1::]]

def gettable(filename):

  f = open(filename,'r')
  table = []
  
  for line in f:
    row = line.split(' ')
    table.append(row)

  return table



