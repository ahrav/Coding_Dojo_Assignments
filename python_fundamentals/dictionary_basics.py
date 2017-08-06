my_dictionary = {"name": "Ahrav Dutta", "age": "23", "country of birth": "India", "Favorite Language": "Python"}

for key,data in my_dictionary.iteritems():
    print "My", key, "is", data

def print_dictionary(dictionary):
    for key,data in dictionary.iteritems():
        print key,data
print_dictionary(my_dictionary)
