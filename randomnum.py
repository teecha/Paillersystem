import random
f = open("sensitive.txt","a")
v = 0
while v <= 10:
    for x in range(10):
        z = random.randint(1,101)
    f.write('{}'.format(z))
    v = v+1
f.close
