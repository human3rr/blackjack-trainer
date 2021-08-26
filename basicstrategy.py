import random
pairSplitting= {"A,A": {"2":"Y", "3":"Y", "4":"Y", "5":"Y", "6":"Y", "7":"Y", "8":"Y", "9":"Y", "10":"Y", "A":"Y" },
                "T,T": {"2":"N", "3":"N", "4":"N", "5":"N", "6":"N", "7":"N", "8":"N", "9":"N", "10":"N", "A":"N" },
                "9,9": {"2":"Y", "3":"Y", "4":"Y", "5":"Y", "6":"Y", "7":"N", "8":"Y", "9":"Y", "10":"N", "A":"N" },
                "8,8": {"2":"Y", "3":"Y", "4":"Y", "5":"Y", "6":"Y", "7":"Y", "8":"Y", "9":"Y", "10":"Y", "A":"Y" },
                "7,7": {"2":"Y", "3":"Y", "4":"Y", "5":"Y", "6":"Y", "7":"Y", "8":"N", "9":"N", "10":"N", "A":"N" },
                "6,6": {"2":"Y/N", "3":"Y", "4":"Y", "5":"Y", "6":"Y", "7":"N", "8":"N", "9":"N", "10":"N", "A":"N" },
                "5,5": {"2":"N", "3":"N", "4":"N", "5":"N", "6":"N", "7":"N", "8":"N", "9":"N", "10":"N", "A":"N" },
                "4,4": {"2":"N", "3":"N", "4":"N", "5":"Y/N", "6":"Y/N", "7":"N", "8":"N", "9":"N", "10":"N", "A":"N" },
                "3,3": {"2":"Y/N", "3":"Y/N", "4":"Y", "5":"Y", "6":"Y", "7":"Y", "8":"N", "9":"N", "10":"N", "A":"N" },
                "2,2": {"2":"Y/N", "3":"Y/N", "4":"Y", "5":"Y", "6":"Y", "7":"Y", "8":"N", "9":"N", "10":"N", "A":"N" }
                }
def displaySplittingPairs(pairSplitting):
    # Print the names of the columns.
    print ("\n\nSPLIT HANDS")
    print ("{:<30} {:<10} ".format('PLAYER HAND', 'DEALER\'S CARD'))

    print(end='\t\t')
    for key, pairs in pairSplitting.items():
        for k, v in pairs.items():
            print(k, end='\t')
        break;
    print()
    # print each data item.
    for key, pairs in pairSplitting.items():
        print()
        print (str(key), end='\t\t')
        for k, v in pairs.items():
            print(v, end='\t')
        print()
            #print(value[i], end=' ')
    print()
    #print (str(key) + " " + "{:<10} {:<10} {:<10}".format(name, age, course))

while(True):
    displaySplittingPairs(pairSplitting)
    myCards = random.choice(list(pairSplitting.keys()))
    print("cards you have: " + myCards)
    dealersCard = random.choice(list(pairSplitting.get(myCards)))
    print("Dealers card is: " + dealersCard)
    doesHit = str(pairSplitting.get(myCards).get(dealersCard))
    print("Do you split? " + doesHit )
    user_input = input("Do you split? Y,N,Y/N : ")
    if(user_input.lower() == doesHit.lower()):
        print("correct")
    else:
        print("Incorrect. Answer is: " + doesHit)
    print()

#print(random.choice(list(pairSplitting.values())))

#print(random.choice(list(pairSplitting[].values())))

