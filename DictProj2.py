def createdict (t):
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
 
    
def PrintDic(dictionary):
    print("\n",dictionary,"\n")
    
def sortDictionaryKeys (dictionary):
    sortedic = {}
    li = sorted (dictionary.keys())
    for i in li:
        sortedic[i] = dictionary[i]
    return sortedic

def sortDictionaryValues (dictionary):
    sortedic = {}
    li = []
    a = 0
    for i in dictionary:
        li.append(dictionary[i])
    li.sort()
    for i in dictionary:
        sortedic[i] = li[a]
        a = a +1
    return sortedic

def aptPrintDic (dictionary):
    liVal = []
    liKey = []
    ValSorted = False
    KeySorted = False
    for i in dictionary:
        liVal.append(dictionary[i])
    sliVal = sorted (liVal)
    if (sliVal == liVal):
        ValSorted = True
    for i in dictionary:
        liKey.append(i)
    sliKey = sorted (liKey)
    if(sliKey == liKey):
        KeySorted = True
    if(KeySorted != ValSorted):
        if(KeySorted):
            print("Dictionary keys sorted alphabetically: ",dictionary)
        else:
            print("Dictionary values sorted numerically: ",dictionary)
    else:
        print("Dictionary values sorted numerically and keys sorted alphabetically  : ",dictionary)
    


def main():
    test = createdict(3)
    test = sortDictionaryKeys(test)
    PrintDic(test)
    test = sortDictionaryValues(test)
    PrintDic(test)
    aptPrintDic(test)
    
      
if __name__=="__main__":       
    main() 
    
    
    