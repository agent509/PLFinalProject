class csclass(object):
    def f(self):
        data = {
            'name': 'CS329E',
            '$name': lambda x: data.update({'name': x}),
            'size': 80,
            '$age': lambda x: data.update({'age': x}),
            'gradeavg': 85,
            '$gradeavg': lambda x: data.update({'gradeavg': x})
        }
        def cf(self, d):
            if d in data:
                return data[d]
            else:
                return None
        return cf
    run = f(1)

class group(csclass):
    def f(self):
        data = {
            'gradeavg': 95,
            '$gradeavg': lambda x: data.update({'gradeavg': x}),
            'membernames': ['Chris', 'Yiran', 'Shawn'],
            '$addname': lambda x: data['membernames'].append(x),
            '$removename': lambda x: data['membernames'].remove(x)
        }
        def cf(self,d):
            if d in data:
                return data[d]
            else:
                return super(group, self).run(d)
        return cf
    run = f(1)


c1 = csclass()
print
print "Class name: ",c1.run('name')
c1.run('$name')('newclass')
print "New Class name: ",c1.run('name')
print "Grade Avg:",c1.run('gradeavg')
c1.run('$gradeavg')('66')
print "New Grade Avg:",c1.run('gradeavg')


g1 = group()
print
print "Now printing for group 1"
print "Grouop Member Names: ",g1.run('membernames')
print "Group grade avg: ",g1.run('gradeavg')
g1.run('$addname')('Joseph')
print "Added a group name: ",g1.run('membernames')
