class MathDojo(object):
    def __init__(self):
        self.number = 0

    def add(self, *nums):
        for num in nums:
            if type(num) == list or type(num) == tuple:
                for val in num:
                    self.number += val
            else:
                self.number += num
        return self

    def subtract(self, *nums):
        for num in nums:
            if type(num) == tuple or type(num) == list:
                for val in num:
                    self.number -= val
            else:
                self.number -= num
        return self
md = MathDojo()
print md.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).number
