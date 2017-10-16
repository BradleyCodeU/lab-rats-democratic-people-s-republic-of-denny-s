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
            print("you can activate the relay system.")
        elif self.plug==true and self.power==true:
            print("conect a network")
        elif (self.connection==true):
            print("the display is dark")
    #setter to log on(hacking skill/luck)
    def logon(self):
        
