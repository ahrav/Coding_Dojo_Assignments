## part 1 write code that prints all odd numbers from 1 to 1000, use for loop
for num in range(1,1000):
    if num % 2 != 0:
        print num
    else:
        continue

## print all multiple of 5 from 5 to 1000,000
for num in range(5, 1000000, 5):
    print num

# print sum of all values in the list
a = [1, 2, 5, 10, 255, 3]
total = 0
for char in a:
    total+= char
print total

# print the average of the values
a = [1, 2, 5, 10, 255, 3]
total = 0
for char in a:
    total += char
avg = total / len(a)
print avg
