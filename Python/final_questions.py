import random

def getColor():
    lstColors = ['Red','Yellow','Blue','Green','Purple','Pink','White','Black']
    color = random.choice(lstColors)
    print("The color is {}!".format(color))

getColor()
