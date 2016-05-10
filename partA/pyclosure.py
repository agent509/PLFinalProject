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





s1 = csclass()
print
print s1.run('name')
s1.run('$name')('mkaewo9E')
print s1.run('name')
print s1.run('gradeavg')
s1.run('$gradeavg')('66')
print s1.run('gradeavg')
#print s1.data


g1 = group()
print
print "Now printing for g1"
print g1.run('membernames')
print g1.run('gradeavg')
g1.run('$addname')('newname')
print g1.run('membernames')
