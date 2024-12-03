#Sebastian Cervantes 
#November 26, 2024 
#set options and sequences for chapter 4
import random
import stats
def chapter_5():
    print("")
    print("Chapter 5: THE COUNT")
    print("UNDEAD EDDY's FINAL CHALLENGE")
    options = ("defend against BOSS BAT ", "defend against BOSS RAT","defend against THE COUNT","THE END")
    while True:
        for index, str in enumerate(options):
            print(f"{index+1}. {str.capitalize()}")
        try:
            choice = int(input("Choose option number from list: "))
            if choice == 1:
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
                    bossbat = random.randrange(3,4)
                    print("you need",(bossbat),"attack points to kill the BOSS BAT")
                    if stats.atk["Attack"]> bossbat: 
                        print("BOSS BAT has been killed")
                        stats.life["life points"]+=1
                        continue
                    else:
                        print("EDDY doesn't have enough ATTACK points to kill BOSS BAT")
                        print("EDDY has died")
                        stats.life["life points"]==0
                        chapter_5()
                elif berry == 2:
                    print("EDDY was attacked and killed by BOSS BAT")
                    stats.life["life points"]==0
                    chapter_5()

            elif choice == 2:
                if stats.life["life points"]>=6:
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
                        bossrat = random.randrange(4,5)
                        print("you need",(bossrat),"attack points to kill the BOSS RAT")
                        if stats.atk["Attack"]> bossrat: 
                            print("BOSS RAT has been killed")
                            stats.life["life points"]+=2
                            continue
                        else:
                            print("EDDY doesn't have enough ATTACK points to kill BOSS RAT")
                            print("EDDY has died")
                            stats.life["life points"]==0
                            chapter_5()

                    elif berry == 2:
                        print("EDDY was attacked and killed by BOSS BAT")
                        stats.life["life points"]==0
                        chapter_5()
                else:
                    print("BEAT BOSS BAT FIRST")
                    chapter_5()

            elif choice == 3:
                if stats.life["life points"]>=8:
                    print("use berry?")
                    berry = int(input("Enter 1 to use berry, enter 2 to not use berry: "))
                    if berry==1:
                        print ("A random berry will be absorbed")
                        rando = random.randrange(1,3)
                        if rando == 1:
                            print("fire berry was absorbed")
                            stats.atk ["Attack"] += 4 
                        elif rando == 2:
                            print("ice berry was absorbed")
                            stats.atk["Attack"]+= 3
                        elif rando == 3:
                            print("poision berry was absorbed")
                            stats.atk["Attack"]+=5
                            stats.life["life points"]-=1
                        thecount = random.randrange(5,6)
                        print("you need",(thecount),"attack points to kill THE COUNT")
                        if stats.atk["Attack"]> thecount: 
                            print("THE COUNT has been killed")
                            stats.life["life points"]+=8
                            continue
                        else:
                            print("EDDY doesn't have enough ATTACK points to kill THE COUNT")
                            print("EDDY has died")
                            stats.life["life points"]==0
                            chapter_5 ()
                    elif berry == 2:
                        print("EDDY was attacked and killed by BOSS BAT")
                        stats.life["life points"]==0
                        chapter_5()
                else:
                    print("BEAT BOTH BOSSES FIRST!!")
                    chapter_5()

            elif choice == 4:
                if stats.life["life points"]>=12:
                    print("EDDY HAS GOT HIS REVENGEEE!!")
                    print("CONGRATULATIONS YOU BEAT UNDEAD EDDY")
                    print("END OF CHAPTER 5")
                    break
                else:
                    print("BEAT ALL BOSSES TO FINISH UNDEAD EDDY!!")
                    chapter_5()
        except ValueError:
            print("enter number")
        break
chapter_5()
