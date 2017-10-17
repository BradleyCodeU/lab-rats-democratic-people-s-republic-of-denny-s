class PocketKnife():
    #consructor with 2 parameters
    def __init__(self, blade, canOpener):
        self.blade = blade #whether the blade is open or closed
        self.bladeActive = False
        self.canOpener = canOpener #whether the can opener is open or closed
        self.canOpenerActive = False

    #interface accessor
    #returns current item description with variables 
    def get_interface(self):
        if self.blade:
            print("Your pocket knife has a closed standard 3 inch blade attached to it, along with a handy-dandy little can opener.")
            print("You can open the BLADE the pocket knife.")
            print("You can open the CAN OPENER on the pocket knife.")
        else:
            print("Your cat ears are turned off. You can TURN ON CAT EARS.")

    #checks for UI keywords, calls other setters
    def check_input(self, command):
        if command == "BLADE" and not self.blade:
            self.bladeActive()
        if command == "CAN OPENER" and not self.canOpener:
            self.canOpenerActive()

    #blade mutator
    #toggles the blade
    def toggleBlade(self):
        self.blade = True

    #blade mutator
    #closes the blade
    def turnOff(self):
        self.blade = False
