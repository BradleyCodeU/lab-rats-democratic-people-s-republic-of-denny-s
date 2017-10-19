class CatPhones():
    def __init__(self,color,music,musicOff):
        self.color = color
        self.music = music #0 or 1
        self.musicOff = musicOff #true false
        self.musicOff = True
        self.isOn = False


    def get_interface(self, heldItems,current_room):
        if self.isOn and self.musicOff:
            print("The "+self.color+" cat headphones are swithced on and not playing music "+self.color+" You can TURN "+self.color.upper()+" CAT HEADPHONE MUSIC ON")
        elif self.isOn and not self.musicOff:
            print("The "+self.color+" cat headphones are swithced on, and glowing neon "+self.color.upper()+" you hear some music so you put the headphones on. You can TURN MUSIC OFF")
        else:
            print("The "+self.color+" cat headphones are swithced off. You can PRESS THE ON BUTTON")
        if self.music == 0 and "charger" in heldItems:
            print("You can PRESS THE "+self.color.upper+" PLAY BUTTON.")
        if self.music > 0:
            print("you can TURN MUSIC OFF.")

    def check_input(self,command,heldItems,current_room):
        if command == "PRESS THE "+self.color.upper()+" PLAY BUTTON":
            self.turn_on()
        if command == "TURN MUSIC OFF":
            self.turn_off()
            

    #Accessors
    def get_song(self):
        
    
    #Mutators
    def turn_on(self):
        if not self.isOn:
            
        if self.music == 1 and not self.musicOff:
            self.isOn = True
            print("You click the play button and music starts playing. You are listenting to "+song+" Blitzkrieg Bop by the Ramones.")
        else:
            print("You click the play button but nothing happens. Maybe you need some music?")

                
    def turn_off(self):
        if self.isOn:
            self.isOn=False
            print("You click the power button. The headphones stop playing music.")

                
    def add_music(self,heldItems):
        if self.music < 1 and "music" in heldItems:
            self.music += 1
            print("You put the music in the "+self.color+" Cat headphones.")
            heldItems.remove("music")
            self.musicOff = False
        elif self.music > 0:
            print("The "+self.color+" Cat Headphones already have music.")
        elif not "music" in heldItems:
            print("You aren't holding any music")

            
    
                        

