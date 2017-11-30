class Product(object):
    def __init__(self, Price, ItemName, Weight, Brand):
        print "creating a product"
       
        self.Price = Price
        self.ItemName = ItemName
        self.Weight = Weight
        self.Brand = Brand
        self.Status = "for sale"
        self.tax = self.Price*0.06
        
       
    def Sell(self):
        
        self.Status = "Sold"
        print self.Status

    def AddTax(self):
        print self.Price + self.tax

    def Return(self, reason):
        self.reason = reason
        if reason == "defective":
            self.Status = "defective"
            self.Price==0
        elif reason =="returned in the box":
            self.Status =="for sale"
        elif reason == "returned open":
            self.Status == "Used"
            self.Price =self.Price*0.8
    def displayInfo(self):
        print self.Price
        print self.ItemName
        print self.Weight
        print self.Brand
        print self.Status

cup = Product(10, "AB", 5,"CMD")
cup.Sell()
cup.AddTax()
cup.Return("defective")
cup.displayInfo()

cup2 = Product(10,"AB", 5,"CMD")
cup2.Sell()
cup2.AddTax()
cup2.Return("returned in the box")
cup2.displayInfo()
            
            




        
        
