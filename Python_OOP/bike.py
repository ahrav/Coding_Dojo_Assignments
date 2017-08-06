class bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.init_miles = 0

    def displayinfo(self):
        print self.price
        print self.max_speed
        print self.init_miles
        return self

    def ride(self):
        self.init_miles += 10
        print "Riding {} miles".format(self.init_miles)
        return self

    def reverse(self):
        self.init_miles -= 5
        if self.init_miles > 0:
            print "Reversing {} miles".format(self.init_miles)
        elif self.init_miles == 0:
            print "Haven't moved"
        else:
            print "Went "+ str(abs(self.init_miles)) + " miles in opposite direction"
        return self

user1 = bike(22, '25mph')
user2 = bike(25, '30mph')
user3 = bike(50, '50mph')
user1.ride()
user1.ride()
user1.ride()
user1.reverse()
user1.displayinfo()

user2.ride().ride().reverse().reverse().displayinfo()
user3.reverse().reverse().reverse().displayinfo()
