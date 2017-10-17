class computer():
    #constructor and paramiters
    def _init_(self,plug,power,conection,logstate):#constructor
        self.plug=plug #t or f
        self.power=power #on or off
        self.connection=False
        self.logstate=False
    

    #getter that returns pc status
    def get_status(self):
        if self.plug==true and self.power==true and self.connection==true:
            print("the computer is ON.")
            time.sleep(10)
            print("please enter your password.")
        elif self.plug==true and self.power==true:
            print("conect a network")
        elif (self.connection==true):
            print("the display is dark")
    #setter to log on change must be in main.py
    def logon (self,password):
        self.password=password
        
        
