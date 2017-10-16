class CatEars():
    #static array of colors
    colorList = ["red", "orange", "yellow", "green", "light green", "white", "light blue", "dark blue",  "purple", "black", "ultraviolet", "infrared", "hypergreen"]
    #consructor
    def __init__(self, color, power):
        self.color = color
        self.power = power

    #interface accessor
    #returns current item description with variables 
    def get_interface(self):
        if self.power:
            print("Your cat ears are turned on and glowing a dim " + CatEars.colorList[self.color] + ".")
            print("You can TURN COLOR WHEEL to change the color of your cat ears to " + self.getNextColor() + ".")
            print("You can TURN OFF CAT EARS.")
        else:
            print("Your cat ears are turned off. You can TURN ON CAT EARS.")

    #checks for UI keywords, calls other setters
    def check_input(self, command):
        if command == "TURN ON CAT EARS" and not self.power:
            self.turnOn()
            print("You turn on your CAT EARS. They glow a dim " + CatEars.colorList[self.color] + ".")
        elif command == "TURN OFF CAT EARS" and self.power:
            self.turnOff()
            print("You turn off your CAT EARS.")
        elif command == "TURN COLOR WHEEL":
            print("You turn the color wheel on the cat ears to " + self.getNextColor() + ".")
            self.changeColor()

    
    #color mutator
    #changes to next color
    def changeColor(self):
        self.color += 1
        if self.color == len(CatEars.colorList):
            self.color = 0

    #power mutator
    #turns on power
    def turnOn(self):
        self.power = True

    #power mutator
    #turns off power
    def turnOff(self):
        self.power = False

    #color accessor
    #returns color
    def getColor(self):
        return colorList(self.color)

    #color accessor
    #returns next color
    def getNextColor(self):
        if self.color + 1 == len(CatEars.colorList):
            nextColor = 0
        else:
            nextColor = self.color + 1
        return CatEars.colorList[nextColor]
