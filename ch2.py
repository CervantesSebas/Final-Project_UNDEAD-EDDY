#Sebastian Cervantes 
#November 26, 2024 
#set options and sequences for chapter 2 
import stats
import random

def chapter_2():
    print("")
    print("Chapter 2: BATS!!")
    print("There is a group of VICIOUS BATS what will UNDEAD EDDY do??")
    options = ("walk forward", "Attack BATS","duck under bats","walk into forest" )
    while True:
        for index, str in enumerate(options):
            print(f"{index+1}. {str.capitalize()}")
        try:
            choice = int(input("Choose option number from list: "))
            if choice == 1:
                print("The BATS attacked Eddy!")
                print("You have FAILED")
                stats.ch_berry["berries"] == 0 
                stats.atk["Attack"]==0
                chapter_2() 
                

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
                    bats = random.randrange(2,4)
                    print("there are", [bats],"BATS")
                    if stats.atk["Attack"]>bats: 
                        print("BATS are killed")
                    else:
                        print("EDDY doesn't have enough ATTACK points to kill BATS")
                        print("EDDY has DIEDD")
                        stats.life["life points"]==0
                elif berry == 2:
                    print("EDDY was attacked and killed by BATS")
                    continue
                
    
            elif choice == 3:
                print("EDDY ducks under bats")
                stats.ch_berry["berries"]+=1
                stats.life["life points"] += 1
                print("That was nice of EDDY")
                print("+1 life point, +1 Berry")
                chapter_2()
                
            elif choice == 4:
                if stats.life["life points"]>=6:
                    print("You killed the bats ")
                    print("UNDEAD EDDY journeys to the MYSTERIOUS FOREST")
                    print("END OF CHAPTER 2")
                    break
                    
                else:
                    print("You can not proceed")
                    chapter_2()
        except ValueError:
            print("enter number")
        break
chapter_2()
