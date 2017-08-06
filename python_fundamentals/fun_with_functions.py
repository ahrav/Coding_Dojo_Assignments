def odd_even():
    for num in range(1,2001):
        if num % 2 == 0:
            print "Number is " + str(num) +". This is an even number."
        else:
            print "Number is " + str(num) +". This is an odd number."
odd_even()

def multiply(arr,num):
    for i in range(len(arr)):
        arr[i] *= num
    return arr
a = [2,4,10,16]
b = multiply(a, 5)
print b

def layered_multiples(arr):
    new_array = []
    for i in range(len(arr)):
        new_array.append([1] * arr[i])
    return new_array

x= layered_multiples(multiply([2,4,5,2],3))
print x
