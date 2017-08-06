for i in range(1,13):
    print '{:4n}'.format(i),
print("\n")
for j in range(1,13):
    for k in range(1,13):
        print '{:4n}'.format(j * k),
    print("\n")
