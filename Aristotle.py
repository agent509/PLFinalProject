class substance(object):
    def f(self):
        data = {
            'name': 'Rita',
            '$name': lambda x: data.update({'name': x}),
            'age': 67,
            '$age': lambda x: data.update({'age': x})
        }
        def cf(self, d):
            if d in data:
                return data[d]
            else:
                return None
        return cf
    run = f(1)

s1 = substance()
print
print s1.run('name')
s1.run('$name')('Phil')
print s1.run('name')
print s1.run('age')
s1.run('$age')('66')
print s1.run('age')
print s1.run('dob')
# print s1.data

class animal(substance):
    #def run(self, a): return super(animal, self).run(a)
    def f(self):
        data = {
            'name': 'Animal',
            '$name': lambda x: data.update({'name': x})
        }
        def cf(self, d):
            if d in data:
                return data[d]
            else:
                return super(animal, self).run(d)
        return cf
    run = f(1)

a1 = animal()
print
print "Now printing for a1"
print a1.run('name')
print a1.run('age')
print a1.run('dob')