import random
def createdic():
    rndint = lambda x: random.randint(0,x)
    li1 = []
    li2 = []
    for i in range (1000):
        li1.append(rndint(255))
        li2.append(rndint(9))
    return {'trap': li1, 'test': li2}

def normalize (li):
    floli = []
    for i in li:
        num = li[i] / 255
        floli.append(num)
    return floli
def match (test,trap):
    counter = 0
    for i in range (1000):
        num = trap[i]*10 - ((trap[i]*10) % 1)
        if(num == test[i]):
            counter = counter + 1
    match = counter/1000 * 100
    print (match)

dic = createdic()
normalizedtrap = normalize(dic["trap"])
match(dic["test"],normalizedtrap)