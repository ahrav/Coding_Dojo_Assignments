class hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
        self.bed_num = 0
    def admit(self, name):
        self.name = name
        if len(self.patients) < self.capacity:
            self.patients.append(self.name)
            print "patient has been admitted"
        else:
            print "Hospital is full"
        return self

hospital1 = hospital('kaiser', 25)
hospital1.admit('john')
hospital1.admit('jacob')
print hospital1.patients
