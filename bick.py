class Bick (object):
    def __init__(self, price, max_speed):
        print "creating a Bick"
       
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):

        print "Bick's price $", self.price
        print "The max speed is", self.max_speed,  "mph"
        print "THe total miles", self.miles, "miles"

    def ride(self):
        print "Riding"
        self.miles += 10

    def revere (self):
        print "reversing"
        if self.miles >5:
            self.miles -=5

Bick1 = Bick( 300, 40)
Bick1.ride()
Bick1.displayInfo()
Bick1.revere()

Bick2 = Bick(400, 20)
Bick2.ride()
Bick2.displayInfo()
Bick2.revere()


       
          
