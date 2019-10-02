def createdic (t): #Gets num of keys to be in dic
    dictionary = {} #Returns formed dic
    for rep in range (t):
        a = rep + 1
        print(str(a) + " time")
        key = getinput("key")
        value = getinput("value")
        if key in dictionary:
            li = list(dictionary[key])
            li.append(value)
            dictionary[key] = li
        else:
            dictionary[key] = value
    print ("The dictionary given is: ")
    print (dictionary)
    return dictionary


def getinput (thing):
     inp = input("insert " + str(thing) )
     try:
         inp = int(inp)
     except ValueError:
         inp = str(inp)
     return inp
 
    
def checkey(key, dictionary):
    if key in dictionary:
        print("yes")
    else:
        print("no")
        
def sqrdic ():
    li_nums = []
    dictionary = {}
    while True:
        num = input("insert numbers to be keys of dict. When finished type a none-whole-number")
        try:
            gnum = int(num)
        except:
            break
        li_nums.append(gnum)
    for num in li_nums:
        if num in dictionary:
            output = []
            li = [dictionary[num]]
            if dictionary.get(num) is list:
                li = dictionary.get(num)
            li.append(num**2)
            del dictionary[num]
            li = reemovNestings(li,output)
            dictionary.update({num: li})
        else:
            dictionary[num] = num**2
    print ("The dictionary created is:")
    print(dictionary)
    
    
def reemovNestings(l, output): 
    for i in l: 
        if type(i) == list: 
            reemovNestings(i,output) 
        else: 
            output.append(i)
    return output
        
 
def main ():
    dict1 = createdic(3)
    dict2 = sqrdic()    
    checkey("one", dict1)
    
    
if __name__ == "__main__":
    main()
