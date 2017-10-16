class PocketKnife():
    #constant array of colors
    colorList = ["shiny red", "plain black", "brown wood-like", " dull gunmetal"]
    #consructor
    # the blade constructor determines whether the knife is open or closed
    def __init__(self, color, blade):
        self.color = color
        self.blade = blade

    #interface accessor
    #returns current item description with variables 
    def get_interface(self):
        if self.blade:
            print("Your pocket knife has a " + colorList[self.color] + " type shine to it.")
            print("You can close the BLADE the pocket knife.")
        else:
            print("Your cat ears are turned off. You can TURN ON CAT EARS.")

    #checks for UI keywords, calls other setters
    def check_input(self, command):
        if command == "BLADE" and not self.blade:

    #blade mutator
    #opens the blade
    def turnOn(self):
        self.blade = True

    #blade mutator
    #closes the blade
    def turnOff(self):
        self.blade = False

    #color accessor
    #returns color
    def getColor(self):
        return colorList(self.color)

    #color accessor
    #returns next color
    def getNextColor(self):
        if self.color + 1 == len(colorList):
            nextColor = 0
        else
            nextColor = self.color + 1
        return colorList(nextColor)
