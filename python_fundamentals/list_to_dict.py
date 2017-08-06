def make_dict(arr1, arr2):
    list_zip = zip(arr1, arr2)
    new_dict = dict(list_zip)
    print new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

make_dict(name, favorite_animal)
