class computer():

    password="1234"
    
    
    #constructor and paramiters
    def _init_(self,plug,power,conection,logstate):#constructor
        self.plug=plug #t or f
        self.power=power #on or off
        self.power=conection #on or off

    #getter that returns pc status
    def get_status(self):
        if self.plug==true and self.power==true and self.connection==true:
            print("the computer is ON.")
            time.sleep(10)
            print("please enter your password.")
            on+pluged-up=True
            
        elif self.plug==true and self.power==true:
            print("conect a network")
        elif (self.connection==true):
            print("the display is dark")
    #GETS PASSWORD
    def get_password(self):
        print(self.password)

    #setters
    #change plug state
    def plug(self):
        if (self.plug==True):
            self.plug=False
        else:
            self.plug=True
    #change power state
    def power(self):
        if (self.power==True):
            self.power=False
        else:
            self.power=True
    #change connection state
    def connection(self):
        if (self.connection==True):
            self.connection=False
        else:
            self.connecrion=True
    #changes password
    def password(self,newPass):
        self.password=newPass
    
