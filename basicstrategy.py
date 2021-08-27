import random
import os
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
softTotals =   {"A,9": {"2":"S", "3":"S", "4":"S", "5":"S", "6":"S", "7":"S", "8":"S", "9":"S", "10":"S", "A":"S" },
				"A,8": {"2":"S", "3":"S", "4":"S", "5":"S", "6":"Ds", "7":"S", "8":"S", "9":"S", "10":"S", "A":"S" },
				"A,7": {"2":"Ds", "3":"Ds", "4":"Ds", "5":"Ds", "6":"Ds", "7":"S", "8":"S", "9":"H", "10":"H", "A":"H" },
                "A,6": {"2":"H", "3":"D", "4":"D", "5":"D", "6":"D", "7":"H", "8":"H", "9":"H", "10":"H", "A":"H" },
                "A,5": {"2":"H", "3":"H", "4":"D", "5":"D", "6":"D", "7":"H", "8":"H", "9":"H", "10":"H", "A":"H" },
                "A,4": {"2":"H", "3":"H", "4":"D", "5":"D", "6":"D", "7":"H", "8":"H", "9":"H", "10":"H", "A":"H" },
                "A,3": {"2":"H", "3":"H", "4":"H", "5":"D", "6":"D", "7":"H", "8":"H", "9":"H", "10":"H", "A":"H" },
                "A,2": {"2":"H", "3":"H", "4":"H", "5":"D", "6":"D", "7":"H", "8":"H", "9":"H", "10":"H", "A":"H" }
                }
hardTotals =   {"17": {"2":"S", "3":"S", "4":"S", "5":"S", "6":"S", "7":"S", "8":"S", "9":"S", "10":"S", "A":"S" },
				"16": {"2":"S", "3":"S", "4":"S", "5":"S", "6":"S", "7":"H", "8":"H", "9":"H", "10":"H", "A":"H" },
				"15": {"2":"S", "3":"S", "4":"S", "5":"S", "6":"S", "7":"H", "8":"H", "9":"H", "10":"H", "A":"H" },
				"14": {"2":"S", "3":"S", "4":"S", "5":"S", "6":"S", "7":"H", "8":"H", "9":"H", "10":"H", "A":"H" },
				"13": {"2":"S", "3":"S", "4":"S", "5":"S", "6":"S", "7":"H", "8":"H", "9":"H", "10":"H", "A":"H" },
				"12": {"2":"H", "3":"H", "4":"S", "5":"S", "6":"S", "7":"H", "8":"H", "9":"H", "10":"H", "A":"H" },
                "11": {"2":"D", "3":"D", "4":"D", "5":"D", "6":"D", "7":"D", "8":"D", "9":"D", "10":"D", "A":"D" },
                "10": {"2":"D", "3":"D", "4":"D", "5":"D", "6":"D", "7":"D", "8":"D", "9":"D", "10":"H", "A":"H" },
                "9": {"2":"H", "3":"D", "4":"D", "5":"D", "6":"D", "7":"H", "8":"H", "9":"H", "10":"H", "A":"H" },
                "8": {"2":"H", "3":"H", "4":"H", "5":"H", "6":"H", "7":"H", "8":"H", "9":"H", "10":"H", "A":"H" }
                }
lateSurrender = {"17": {"2":"", "3":"", "4":"", "5":"", "6":"", "7":"", "8":"", "9":"S", "10":"S", "A":"S" },
                 "16": {"2":"", "3":"", "4":"", "5":"", "6":"", "7":"", "8":"", "9":"", "10":"S", "A":"" },
                 "15": {"2":"", "3":"", "4":"", "5":"", "6":"", "7":"", "8":"", "9":"", "10":"", "A":"" },
                }



def displayPairs(dispItems):
    # Print the names of the columns.
    print(end='\t\t')
    for key, pairs in dispItems.items():
        for k, v in pairs.items():
            print(k, end='\t')
        break;
    print()
    # print each data item.
    for key, pairs in dispItems.items():
        print()
        print (str(key), end='\t\t')
        for k, v in pairs.items():
            print(v, end='\t')
        print()
            #print(value[i], end=' ')
    print()
    #print (str(key) + " " + "{:<10} {:<10} {:<10}".format(name, age, course))

def testActions(tabletype, hands, info):
    correctcount = 0
    failcount = 0
    pfailcount = 0
    while(True):
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("\n\n" + tabletype)
        print ("{:<30} {:<10} ".format('PLAYER HAND', 'DEALER\'S CARD'))
        displayPairs(hands)
        if(failcount > pfailcount):
            print("PREVIOUS ANSWER INCORRECT!")
            pfailcount += 1
        print("Correct count : " + str(correctcount))
        print("Inorrect count: " + str(failcount) + "\n")
        myCards = random.choice(list(hands.keys()))
        print("You have: " + myCards)
        dealersCard = random.choice(list(hands.get(myCards)))
        print("Dealers card is: " + dealersCard + "\n")
        doesHit = str(hands.get(myCards).get(dealersCard))
        #print("Do you split? " + doesHit )
        print(info)
        user_input = input("Answer: ")
        if(user_input.lower() == doesHit.lower()):
            print("correct")
            correctcount += 1
        else:
            print("Incorrect. Answer is: " + doesHit)
            failcount += 1
        print()

testActions("SPLIT HANDS", pairSplitting, "Y: Split the pair, Y/N: Split if double after split is offered, otherwise do not, N: Don't split the pair")
testActions("SOFT HANDS", softTotals, "H :Hit, S: Stand, D: Double if allowed otherwise hit, Ds: Double if allowed otherwise hit" )
testActions("HARD HANDS", hardTotals, "H: Hit, S: Stand, D: Double if allowed otherwise hit" )
#testSplitting("SOFT HANDS")

#print ("\n\nSOFT HANDS")
#print ("{:<30} {:<10} ".format('PLAYER HAND', 'DEALER\'S CARD'))
#displaySplittingPairs(softTotals)
#print(random.choice(list(pairSplitting.values())))

#print(random.choice(list(pairSplitting[].values())))

