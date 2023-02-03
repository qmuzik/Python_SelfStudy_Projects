class Bird:

    'A base class to define bird properties'

    # Starting value at zero 
    count = 0

    # Defines the initializer class method to initialize an instance varible and increment it by 1
    def __init__(self, chat):

        self.sound = chat
        Bird.count += 1

    # Returns the value of the instance varible 
    def talk(self):
        return self.sound