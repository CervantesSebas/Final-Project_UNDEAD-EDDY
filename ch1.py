#Sebastian Cervantes 
#November 25 
#List the 4 options of chapter 1 

import stats

def chapter_1():
    print("UNDEAD EDDY")
    print("Chapter 1: THE AMBUSH")

    options = ["Collect fire berry", "Collect ice berry", "Collect poision berry","Investigate rustling bush"]

    col = ("berry collected")
    fire = ("Eddy gained +4 damage")
    ice = ("Eddy gained +3 damage")
    pois= ("Eddy gained +5 damage, but -1 life point")

    while True:
        for index, str in enumerate(options):
                    print(f"{index+1}. {str.capitalize()}")
        
        try:
            choice = int(input("Choose option number from list: "))
            if choice == 1:
                aorb = int(input("Enter 1 to absorb, enter 2 to collect: "))
                if aorb == 1:
                    print(fire)
                    stats.atk["Attack"] += 4
                else:
                    print(col)
                    stats.ch_berry["berries"]+= 1
                    continue

            elif choice == 2:
                    aorb = int(input("Enter 1 to absorb, enter 2 to collect: "))
                    if aorb==1:
                        print (ice)
                        stats.atk["Attack"] += 3
                    else:
                        print(col)
                        stats.ch_berry["berries"]+=1
                        continue
        
            elif choice == 3:
                    aorb = int(input("Enter 1 to absorb, enter 2 to collect: "))
                    if aorb==1:
                        print (pois)
                        stats.atk["Attack"]+=5
                        stats.life["life points"] -= 1
                    else:
                        print(col)
                        stats.ch_berry["berries"] +=1
                        continue
                    
            elif choice == 4:
                    print("'SLASHHH!!!'")
                    print("EDDY has been killed....")
                    print("EDDY will get his REVENGE!!")
                    print("END OF CHAPTER 1")
                    break
            else:
                print("Choose a number from list")
                chapter_1()

        except ValueError:
             print("try again")

chapter_1()