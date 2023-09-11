
class InstanceCounter(object):
    count = 0 # class attribute, will be accessible to all instances
    def __init__ (self, val): 
        self.val = val 
        InstanceCounter.count +=1 # Increment the value of class attribute, accessible through class name
    # In above line, class ('InstanceCounter') act as an object 
    def set_val(self, newval): 
        self.val = newval
    def get_val(self):
        return self.val
    def get_count(self):
        return InstanceCounter.count

a = InstanceCounter(9)   
b = InstanceCounter(18)
c = InstanceCounter(27)
d = InstanceCounter(64)
for obj in (a, b, c):
    print ('val of obj: %s' %(obj.get_val()))
    print ('count: %s' %(obj.get_count()))
    # Initialized value ( 9, 18, 27)
    # always 3
class myClass: 
    class_attribute = 99
def class_method(self):
    self.instance_attribute = 'I am instance attribute'
print (myClass.__dict__ ) 
