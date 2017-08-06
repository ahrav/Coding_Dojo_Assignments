import types
my_list = ['magical unicorns',19,'hello',98.98,'world']
strings = ""
sum = 0
for char in my_list:
    if isinstance(char, (int,float)):
        sum += char
    elif isinstance(char, str):
        strings += " "+char
    else:
        continue
print strings
print sum
