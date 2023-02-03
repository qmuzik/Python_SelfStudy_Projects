class Songbird:
    def __init__(self, name, song) :
        self.name = name
        self.song = song
        print(self.name, 'Is Born...')

       
    # Displays each varible value 
    def sing(self):
        print(self.name ,'Sings:', self.song)

    # Destructor method for confirmation when instances of the class are destroyed 
    def __del__(self):
        print(self.name, 'Flew Away!\n')