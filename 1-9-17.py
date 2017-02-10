import time

D = 0
C = 2500000
L = 10000000

startTime = time.time()
totalDogLegs = 4 * D
correct = False
for i in range(C + 1):
    if totalDogLegs + (4 * i) == L:
        correct = True
        break

if correct:
    print("Your calculations are correct Farmer Bob.")
else:
    print("You're wrong, and why don't you count animals rather than their legs anyway??")

print("--- %s seconds ---" % (time.time() - startTime))

