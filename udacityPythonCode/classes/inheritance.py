
# class name first letter uppercase "P" 
class Parent():
    # constructor 
    def __init__(self, last_name, eye_color):
        print("Parent Constructor called\n")
        self.last_name = last_name
        self.eye_color = eye_color
        
    # super class instance method  
    def show_info(self):
        print('Parent class - show_info instance method self.last_name is -> {}'.format(self.last_name))
        print('Parent class - show_info instance method self.eye_color is -> {}\n'.format(self.eye_color))

# class name first letter uppercase "C"
# "Parent" specified as super class
class Child(Parent):
    # constructor
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor called")
        Parent.__init__(self,last_name,eye_color) # invoke (and populate) super class constructor 
        self.number_of_toys = number_of_toys
        
    # subclass instance method
    # method overriding - same name in super Parent class
    
    def show_info(self):
        print('Child class - show_info instance method self.last_name is -> {}'.format(self.last_name))
        print('Child class - show_info instance method self.eye_color is -> {}'.format(self.eye_color))
        print('Child class - show_info instance method self.number_of_toys is -> {}\n'.format(self.number_of_toys))


print("\nBegin inheritance.py module\n")
# Parent class instance 
billy_cyrus = Parent("Cyrus", "blue")
 
print('billy_cyrus.last_name is -> {}'.format(billy_cyrus.last_name))
print('billy_cyrus.eye_color is -> {}\n'.format(billy_cyrus.eye_color))
billy_cyrus.show_info()

# Child class instance 
miley_cyrus = Child("Cyrus", "Green", 5)

print('miley_cyrus.eye_color is -> {}'.format(miley_cyrus.eye_color))
print('miley_cyrus.last_name is -> {}'.format(miley_cyrus.last_name))
print('miley_cyrus.number_of_toys is -> {}\n'.format(miley_cyrus.number_of_toys))

# Child instance calls inherited super class instance method - when instance method not defined in Child class
miley_cyrus.show_info()

print("End inheritance.py module\n")


