import types
vars = 45
isinstance(vars, (int))
if vars >= 100:
    print "thats a big number"
else:
    print "that's a small number"

strings = "experience is simply the name we give to our mistakesssssssssss"
isinstance(strings, (str))
if strings >= 100:
    print "thats a long string"
else:
    print "thats a short string"

lists = [1,2,3,4,5,6,7,8,9,0,9,8,7]
isinstance(lists, list)
if lists >= 10:
    print "thats a long list"
else:
    print "thats a short list"
