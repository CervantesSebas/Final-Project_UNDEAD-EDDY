#Sebastian Cervantes 
#November 26, 2024 
#set options and sequences for chapter 4
import random
import stats
def chapter_4():
    print("")
    print("Chapter 4: THE RAT BRIDGE")
    print("UNDEAD EDDY approaches the RAT BRIDGE")
    options = ("Walk across carefully", "shoot sleeping RATS","RUN ACROSS","Approach the VAMPIRE MANSION")
    while True:
        for index, str in enumerate(options):
            print(f"{index+1}. {str.capitalize()}")
        try:
            choice = int(input("Choose option number from list: "))
            if choice == 1:
                print ("UNDEAD EDDY carefully makes his way through the bridge....")
                stats.ch_berry ["berries"]+=2
                print ("+2 random berries")
                stats.life["life points"]+=2
                print("UNDEAD EDDY MADE IT ACROSS!!")
                print("+2 life point")
                continue

            elif choice == 2:
                print("use berry?")
                berry = int(input("Enter 1 to use berry, enter 2 to not use berry: "))
                if berry==1:
                    print ("A random berry will be absorbed")
                    rando = random.randrange(1,3)
                    if rando == 1:
                        print("fire berry was absorbed")
                        stats.atk["Attack"] += 4 
                    elif rando == 2:
                        print("ice berry was absorbed")
                        stats.atk["Attack"]+= 3
                    elif rando == 3:
                        print("poision berry was absorbed")
                        stats.atk["Attack"]+=5
                        stats.life["life points"]-=1
                    rats = random.randrange(4,6)
                    print("there are", [rats], "RATS")
                    if stats.atk["Attack"]> rats: 
                        print("RATS are killed")
                        continue
                    else:
                        print("EDDY doesn't have enough ATTACK points to kill RATS")
                        print("EDDY has died")
                        stats.life["life points"]==0
                        chapter_4()
                    
                elif berry == 2:
                    print("EDDY was attacked and killed by RATS")
                    stats.life["life points"]==0
                    chapter_4()
    
            elif choice == 3:
                print("THE RATS WOKE UP AND ATTACKED!!")
                stats.life["life points"] == 0
                print("UNDEAD EDDY WAS KILLED BY RATS!")
                chapter_4()
                
                
            elif choice == 4:
                if stats.life["life points"] >= 6:
                    print("You have made it across the RAT BRIDGE")
                    print("UNDEAD EDDY approaches the VAMPIRE MANSION")
                    print("END OF CHAPTER 4")
                    break
                else:
                    print("You can not proceed")
                    chapter_4()
                
        except ValueError:
            print("enter number")
        break
chapter_4()
