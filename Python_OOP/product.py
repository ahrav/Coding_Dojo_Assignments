class product(object):

    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        self.tax = tax
        self.cost = (1 + self.tax) * self.price
        return self

    def return_item(self, reason):
        self.reason = reason
        if self.reason == "defective":
            self.status = "defective"
            self.cost = 0
        elif self.reason == "in box":
            self.status = "for sale"
        elif self.reason == "opened":
            self.status = "used"
            self.cost = self.cost - (self.cost * .20)
        return self

    def display_info(self):
        print "Price: " + str(self.price)
        print "Item Name: " + str(self.item_name)
        print "Weight: " + str(self.weight)
        print "Brand: " + str(self.brand)
        print "Cost: " + str(self.cost)
        print "Status: " + str(self.status)
        return self

product1 = product(5, 'mango', 2, 'kroger', 3)
product1.return_item('opened').display_info()
