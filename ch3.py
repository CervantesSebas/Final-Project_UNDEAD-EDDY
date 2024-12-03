#Sebastian Cervantes 
#November 26, 2024 
#set options and sequences for chapter 3
import stats
import random
def chapter_3 ():
    print("")
    print("Chapter 3: THE HAUNTED FOREST")
    print("UNDEAD EDDY enters the HAUNTED FOREST")
    print("Mysterious tree and group of RATS ahead")
    options = ("Collect berries form mysterious tree", "Attack RATS","jump over rats","approach RAT BRIDGE" )
    while True:
            for index, str in enumerate(options):
                print(f"{index+1}. {str.capitalize()}")
            try:
                choice = int(input("Choose option number from list: "))
                if choice == 1:
                    tree = int(input("ENTER 1 to collect berries, ENTER 2 to leave tree alone: "))
                    print (tree)
                    if tree == 1:
                        print("WACKKK")
                        print("the mysterious tree wacked you for taking its berries!!")
                        stats.ch_berry["berries"]+=2
                        stats.life["life points"]==0
                        print("you gained 2 berries, but you have been KILLED")
                        chapter_3()
                    elif tree == 2:
                        print("the tree gave you 1 berry for not being greedy")
                        stats.ch_berry["berries"] += 1 
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
                        rats = random.randrange(2,4)
                        print("there are", [rats], "RATS")
                        if stats.atk["Attack"]> rats: 
                            print("RATS are killed")
                            continue
                        else:
                            print("EDDY doesn't have enough ATTACK points to kill RATS")
                            print("EDDY has died")
                            stats.life["life points"]==0
                            chapter_3()
                    elif berry == 2:
                        print("EDDY was attacked and killed by RATS")
                        stats.life["life points"]==0
                        chapter_3

                
        
                elif choice == 3:
                    print("EDDY jumps over rats")
                    stats.ch_berry["berries"]+=1
                    stats.life["life points"] += 1
                    print("That was nice of EDDY")
                    print("+1 life point, +1 Berry")
                    continue
                    
                elif choice == 4:
                    if stats.life["life points"]>= 6:
                        print("You have made it past the MYSTERIOUS FOREST")
                        print("UNDEAD EDDY journeys to the RAT BRIDGE")
                        print("END OF CHAPTER 3")
                        break
                    else:
                        print("You can not proceed")
                        chapter_3()
                       
                    
            except ValueError:
                print("enter number")
chapter_3()