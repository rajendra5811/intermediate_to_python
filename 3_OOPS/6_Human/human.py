class Human:
    def _init_(self, n, o):
        self.name = n
        self.occupation = o
    
    def do_work(self):
        if self.occupation ==  "tennis player":
            print(self.name, "plays tennis")
        elif self.occupation == "actor":
            print(self.name, "shoots a film")
    
    def speaks(self):
        print( self.name, "says how are u?")

tom = Human("tom cruise", "actor")
tom.do_work()
tom.speaks()

maria = Human("maria sharapova","tennis player")
maria.do_work()
maria.speaks()