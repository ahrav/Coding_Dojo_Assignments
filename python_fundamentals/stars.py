def draw_stars(arr):
    for i in arr:
        print "*" * i
y = [4, 6, 1, 3, 5, 7, 25]
draw_stars(y)

def draw_stars_two(arr):
    for i in arr:
        if type(i) is int:
            print "*" * i
        else:
            print len(i) * i[0].lower()

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars_two(x)
