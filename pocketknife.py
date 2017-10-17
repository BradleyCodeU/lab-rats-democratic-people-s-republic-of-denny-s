class PocketKnife():
    #consructor
    # the blade constructor determines whether the knife is open or closed
    #the canOpener con
    def __init__(self, blade, canOpener):
        self.blade = blade
        self.canOpener = canOpener

    #interface accessor
    #returns current item description with variables 
    def get_interface(self):
        if self.blade:
            print("Your pocket knife has a closed standard 3 inch blade attached to it, along with a handy-dandy little can opener.")
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
