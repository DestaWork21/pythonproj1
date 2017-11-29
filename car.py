class Car (object):
    def __init__(self, price, speed, Fuel, mileage):
        print "creating a Bick"
       
        self.price = price
        self.speed = speed
        self.Fuel = Fuel
        self.mileage = mileage
        
        if self.price > 10000:
            
            self.tax =0.15

        else:
            self.tax = 0.12



    def display_all(self):
        print "Price: $", self.price
        print "Speed: ", self.speed
        print "Fuel: ", self.Fuel
        print "Mileage: ", self.mileage 
        print "Tax: ", self.tax

        
        
car1 =Car(2000, "35mph", "Fuel", "15mpg") 
car1.display_all()

car2 =Car(2000, "5mph", "Not Fuel", "105mpg") 
car2.display_all()

car3 =Car(2000, "15mph", "Kind of Fuel", "95mpg") 
car3.display_all()

car4 =Car(2000, "15mph", "Kind of Fuel", "95mpg") 
car4.display_all()

car5 =Car(2000, "45mph", "Fuel", "25mpg") 
car5.display_all()

car6 =Car(2000000, "35mph", "Empty", "15mpg") 
car6.display_all()

        






       
          
