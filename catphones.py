class CatPhones():
    #array of songs
    songList = ["Blitzkreig Bop by the Ramones","Animal I have become by three days grace","Wake me up by Goofy","All star by Shrek","Happy by Ferrel William","Stressed Out by Twentyone Pilots", "Spooky moosic by the ghosts"]
    def __init__(self,color,song,music,musicOff):
        self.color = color
        self.music = music #0 or 1
        self.musicOff = musicOff #true false
        self.musicOff = True #Why do you take a parameter and then force it to true?
        self.isOn = False
        self.song = song #Is this a number?


    def get_interface(self, heldItems,current_room):
        if self.isOn and self.musicOff:
            print("The "+self.color+" cat headphones are swithced on and not playing music "+self.color+" You can TURN "+self.color.upper()+" CAT HEADPHONE MUSIC ON")
            #..."not playing music blue You can TURN BLUE CAT HEADPHONE MUSIC ON"
            #second self.color is out of place, TURN [color] CAT HEADPHONE MUSIC ON isn't recognized as a command
        elif self.isOn and not self.musicOff:
            print("The "+self.color+" cat headphones are swithced on, and glowing neon "+self.color.upper()+" you hear some music so you put the headphones on. You can TURN MUSIC OFF")
        else:
            print("The "+self.color+" cat headphones are swithced off. You can PRESS THE ON BUTTON") #PRESS THE ON BUTTON isn't included in check_input
        if self.music == 0 and "charger" in heldItems:
            print("You can PRESS THE PLAY BUTTON.")
        if self.music > 0:
            print("you can TURN MUSIC OFF.")

    def check_input(self,command,heldItems,current_room):
        if command == "PRESS THE PLAY BUTTON":
            self.turn_on()
            self.get_song() #This method does not exist- and what are you doing with the song name?
        if command == "TURN MUSIC OFF":
            self.turn_off()
            

    #Accessors
    def changeSong(self):
        self.song += 1
        if self.song == len(CatPhones.songList):
            self.color = 0

    def getSong(self):
        #return songList(self.song)
        return CatPhones.songList[self.song] #fixed

    #Mutators
    def turn_on(self):
        if not self.isOn: #This doesn't do anything
            
        if self.music == 1 and not self.musicOff:
            self.isOn = True
            print("You click the play button and music starts playing. You are listenting to "+self.getNextColor() ) #self.getNextColor() does not exist
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

    
            
    
                        

