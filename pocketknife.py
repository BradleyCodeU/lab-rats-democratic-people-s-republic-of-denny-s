class PocketKnife():
    #consructor with 2 parameters
    def __init__(self, blade, canOpener):
        self.blade = blade #whether the blade is open or closed
        self.canOpener = canOpener #whether the can opener is open or closed

    #interface accessor
    #returns current item description with variables 
    def get_interface(self):
        print("Your pocket knife has a standard 3 inch blade attached to it, along with a handy-dandy little can opener.")
        # Blade if
        if self.blade:
            print("The blade on the knife is currently out, watch where you point that thing!")
            print("You can close the BLADE the pocket knife.")
        else:
            print("The blade on the knife is closed, all is well in the world.")
            print("You can open the BLADE the pocket knife.")

        # Can opener if
        if self.canOpener:
            print("The can opener is open, may all the unopened cans in the world tremble with fear.")
            print("You can close the CAN OPENER on the pocket knife.")
        else:
            print("The can opener is closed, all the unopened cans in the world can sleep easy.")
            print("You can open the CAN OPENER on the pocket knife.")

    #checks for UI keywords, calls other setters
    def check_input(self, command):
        if command == "BLADE" and not self.blade:
            self.bladeToggle()
        if command == "CAN OPENER" and not self.canOpener:
            self.canOpenerToggle()

    #blade mutator
    #toggles the blade switch
    def toggleBlade(self):
        self.blade = not self.blade

    #can opener mutator
    #toggles the can opener switch
    def toggleCanOpener(self):
        self.canOpener = not self.canOpener
        
    #accessors
    def getBlade(self):
        return self.blade

    def getCanOpener(self):
        return self.canOpener
    
