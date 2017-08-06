words = "it's thanksgiving day. It's my birthday too!"
print words.find("day")
new_word = words.replace('day', "month")
print new_word

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[-1]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
half_list = len(x)/2
begin_list = x[:half_list]
end_list = x[half_list:]
end_list.insert(0, begin_list)
print end_list
