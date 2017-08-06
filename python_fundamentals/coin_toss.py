import random
def coin_toss(number):
    heads = 0
    tails = 0
    for i in range(0,number):
        random_num = random.randint(1,2)
        if random_num == 1:
            heads += 1
            print "Attempt #" + str(i) + ": throwing a coin... It's a head!...  Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
        else:
            tails += 1
            print "Attempt #" + str(i) + ": throwing a coin... It's a tail!...  Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"

coin_toss(100)
