class Person:
    
    '"A base class to define person properties"'

    def __init__(self,name):
        self.name = name

    def speak(self,msg = '(Calling The Base Class'):
        print(self.name,msg)