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

#print(select(gettable('table'),['name']))


    


    


'''
# 1. select * from s_dept;
print "\nselect * from s_dept:", s_dept[1::]

# 2.select last_name, first_name, title, salary from s_emp;
print "\nselect last_name, first_name, title, salary from s_emp: ", [[i[1], i[3],i[6],i[7]] for i in s_emp[1::]]

# 3. select last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40;
print "\nselect last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40: ", [[i[1], i[3],i[6],i[7]] for i in s_emp[1::] if i[7] > 1500 and i[9] > 40]

# 4. select last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by last_name;
print "\nselect last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by last_name: ", sorted([[i[1], i[3],i[6],i[7]] for i in s_emp[1::] if i[7] > 1500 and i[9] > 40], key = lambda x: x[0])

# 5. select last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by salary desc;
print "\nselect last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by salary desc: ", sorted([[i[1], i[3], i[6],i[7]] for i in s_emp[1::] if i[5] > 1500 and i[9] > 40], key = lambda x: int(x[3]), reverse=True)

# 6. select last_name, first_name, title, salary, name from s_emp e join s_dept d on(e.dept_id = d.id);
print "\nselect last_name, first_name, title, salary, name from s_emp e join s_dept d on(e.dept_id = d.id): ", [[i[1], i[3], i[6],i[7],j[1]] for i in s_emp[1::] for j in s_dept[1::] if i[9] == j[0] ]

# 7. select dept_id, avg(salary) from s_emp group by dept_id order by dept_id;
print "\nselect dept_id, avg(salary) from s_emp group by dept_id order by dept_id"
print sorted([(lambda deptno, avgSal: [deptno, avgSal])(department, (lambda l: round(sum(l) / len(l), 2))(map(float,[ e[7] for e in s_emp[1::] if e[9] == department ]))) for department in { d[9] for d in s_emp[1::] }],key=lambda x: x[0])

# 8. select dept_id, avg(salary) from s_emp group by dept_id having avg(salary) < 1500;
print "\nselect dept_id, avg(salary) from s_emp group by dept_id having avg(salary) < 1500"
print filter(None,[(lambda deptno, avgSal:[deptno,avgSal] if (avgSal < 1500) else None)(department, (lambda l: round(sum(l) / len(l), 2))(map(float,[ e[7] for e in s_emp[1::] if e[9] == department ])))for department in { d[9] for d in s_emp[1::] } ])
'''
