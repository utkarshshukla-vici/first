class animal:
    def sound (self):
        print ("animal do speak")
    def make_sound(self,sound, name):
        self.sound = sound
        self.name = name
        print("the sound of",self.name,"is",self.sound)

obj = animal()
obj.make_sound("cat", "meow")
obj.make_sound("dog","bark")
    
    