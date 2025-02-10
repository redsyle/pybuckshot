import random, time
debug = False
yourinventory = {
    "medkit": 0,
    "beer": 0,
    "phone": 0,
    "saw": 0,
    "loupe": 0,
    "cigarettas": 0,
    "handcuffs": 0,
    "adrenaline": 0,
    "invertor": 0
}
opponentinventory = {
    "medkit": 0,
    "beer": 0,
    "phone": 0,
    "saw": 0,
    "loupe": 0,
    "cigarettas": 0,
    "handcuffs": 0,
    "adrenaline": 0,
    "invertor": 0
}
listofitems = ["medkit", "beer", "phone", "saw", "loupe", "cigarettas", "handcuffs", "adrenaline", "invertor"]
total_bullets = int(random.randint(2,6)); blank_bullets = int(random.randint(1, total_bullets-1)); live_bullets = int(total_bullets - blank_bullets)
maxslots = 8; poryadok = []; rounds = 0; cuffcount = 0; sawUsed = False; yourturn = True; opponenthealth = 2; yourhealth = 2; youCuffed = bool; isCuffed = bool
def selcom():
    selcom = input("Enter command: ").lower().replace(" ", "")
    if selcom == "use":
        selitem = input("What item you want do use? ").lower().replace(" ", "")
        if selitem == "medkit" and yourinventory["medkit"] > 0: medkit(); yourinventory["medkit"] -= 1
        elif selitem == "beer" and yourinventory["beer"] > 0: beer(); yourinventory["beer"] -= 1
        elif selitem == "phone" and yourinventory["phone"] > 0: phone(); yourinventory["phone"] -= 1
        elif selitem == "saw" and yourinventory["saw"] > 0: saw(); yourinventory["saw"] -= 1
        elif selitem == "loupe" and yourinventory["loupe"] > 0: loupe(); yourinventory["loupe"] -= 1
        elif selitem == "cigarettas" and yourinventory["cigarettas"] > 0: cigarettas(); yourinventory["cigarettas"] -= 1
        elif selitem == "handcuffs" and yourinventory["handcuffs"] > 0: handcuffs(); yourinventory["handcuffs"] -= 1
        elif selitem == "adrenaline" and yourinventory["adrenaline"] > 0: adrenaline(); yourinventory["adrenaline"] -= 1
        else: print("Item not found")
    elif selcom == "shot":
        shot()
    elif selcom == "inventory":
        print("Opponent inventory")
        for xo in opponentinventory.keys():
            bo = opponentinventory[xo]
            if bo != 0:
                print(f"{xo}({bo})")
        print("Your inventory")
        for xy in yourinventory.keys():
            by = yourinventory[xy]
            if by != 0:
                print(f"{xy}({by})")
    elif selcom == "health":
        print(f"Opponent health: {opponenthealth}\nYour health: {yourhealth}")
    else: print("Unknown command!")
def givingitems():
    global opponentinventory, yourinventory
    import random
    for _o in range(3):
        if sum(opponentinventory.values()) == maxslots:
            if debug == True:
                print("Opponent inventory is full (DEBUG)")
                break
        else:
            b = random.randint(0, 7)
            opponentinventory[listofitems[b]] += 1
    for _y in range(3):
        if sum(yourinventory.values()) == maxslots:
            print("Oh.. Your inventory is full")
            break
        else:
            b = random.randint(0, 7)
            yourinventory[listofitems[b]] += 1
    print("Opponent inventory")
    for xo in opponentinventory.keys():
        bo = opponentinventory[xo]
        if bo != 0:
            print(f"{xo}({bo})")
    print("Your inventory")
    for xy in yourinventory.keys():
        by = yourinventory[xy]
        if by != 0:
            print(f"{xy}({by})")
def adrenaline():
    import random
    global opponentinventory, yourinventory
    for xo in opponentinventory.keys():
        bo = opponentinventory[xo]
        if bo != 0:
            print(f"{xo}({bo})")
    stealitem = input("Enter your item: ").lower().replace(" ", "")
    yourinventory["adrenaline"] -= 1
    if opponentinventory[stealitem] == 0:
        print("Item is not exist!")
    else:
        opponentinventory[stealitem] -= 1
        if stealitem == "medkit": medkit()
        elif stealitem == "beer": beer()
        elif stealitem == "phone": phone()
        elif stealitem == "saw": saw()
        elif stealitem == "loupe": loupe()
        elif stealitem == "cigarettas": cigarettas()
        elif stealitem == "handcuffs": handcuffs()
        elif stealitem == "adrenaline": print("Adrenaline cannot be stealed!")
        elif stealitem == "invertor": invertor()
def medkit():
    global yourhealth, opponenthealth
    medrand = random.randint(1,2)
    if medrand == 1: yourhealth += 2; print(f"Luckily! Now health: {yourhealth}")
    elif medrand == 2: yourhealth -= 1; print(f"So bad! Now health: {yourhealth}")
def cigarettas():
    global yourhealth, opponenthealth
    if yourturn == True:
        yourhealth += 1
    else:
        opponenthealth += 1

def phone():
    import random
    f = poryadok[0]
    ranph = random.randint(1, f)
    print(f"{ranph} bullet was", poryadok[f])
def beer():
    if yourturn == True:
        print("You are drinking beer... ")
        time.sleep(0.25)
        print(f"Bullet was.. {poryadok[0]}")
        poryadok.remove(poryadok[0])
    else:
        print("Opponent is drinking beer... ")
        time.sleep(0.25)
        print(f"Bullet was.. {poryadok[0]}")
        poryadok.remove(poryadok[0])
def saw():
    global sawUsed
    print("You are using saw... ")
    sawUsed = True
def loupe():
    print("You are using loupe... "); time.sleep(0.3)
    if poryadok[0]: print("Bullet is.."); time.sleep(0.1); print("live..")
    else: print("Bullet is.."); time.sleep(0.1); print("blank..")

def invertor(): #ЧХ прописан
    if yourturn == True:
        print("You are using invertor... ");
        time.sleep(0.3)
        if poryadok[0] == True:
            poryadok[0] = not poryadok[0]
        else:
            poryadok[0] = not poryadok[0]
    else:
        print("Opponent is using invertor... ");
        time.sleep(0.3)
        for i in range(len(poryadok)):
            if poryadok[i] == True:
                poryadok[i] = not poryadok[i]
            else:
                poryadok[i] = not poryadok[i]
def handcuffs(): #ЧХ прописан
    global cuffcount, yourturn, isCuffed, youCuffed
    if isCuffed == True:
        print("Handcuffs already used!")
    else:
        if yourturn == True:
            isCuffed == True and youCuffed == False
        else:
            isCuffed == True and youCuffed == True
def shot():
    global yourturn, opponenthealth, yourturn, yourhealth, sawUsed
    print(poryadok)
    if yourturn == True:
        time.sleep(0.2)
        print("Shotting..")
        time.sleep(0.3)
        turnselect = input("You or opponent?")
        turnselect = turnselect.lower().replace(" ", "")
        if poryadok[0] == True and turnselect == "you":
            time.sleep(0.2)
            print("Shotted!")
            if sawUsed == True:
                yourhealth -= 2
                sawUsed = False
                poryadok.remove(poryadok[0])
                yourturn = not yourturn
            else:
                yourhealth -= 1
                poryadok.remove(poryadok[0])
                yourturn = not yourturn
        elif poryadok[0] == False and turnselect == "you":
            if sawUsed == True: sawUsed == False
            time.sleep(0.2)
            print("Oops.. Bullet is blank")
            poryadok.remove(poryadok[0])
        elif poryadok[0] == True and turnselect == "opponent":
            time.sleep(0.2)
            print("Shotted!")
            if sawUsed == True:
                opponenthealth -= 2
                sawUsed = False
                poryadok.remove(poryadok[0])
                yourturn = not yourturn
            else:
                opponenthealth -= 1
                poryadok.remove(poryadok[0])
                yourturn = not yourturn
        elif poryadok[0] == False and turnselect == "opponent":
            if sawUsed == True: sawUsed == False
            time.sleep(0.2)
            print("Oops.. Bullet is blank")
            yourturn = not yourturn
            poryadok.remove(poryadok[0])
        time.sleep(0.5)
    else:
        if yourturn == False:
            variation = random.randint(1,2)
            if variation == 1:
                print("Shotting..")
                time.sleep(0.5)
                print("Opponent selected: you")
                if poryadok[0] == True:
                    time.sleep(0.5)
                    print("Shotted!")
                    poryadok.remove(poryadok[0])
                    yourhealth -= 1
                else:
                    time.sleep(0.5)
                    print("Bullet is blank..")
                    poryadok.remove(poryadok[0])
                    yourturn = not yourturn
            else:
                time.sleep(0.5)
                print("Opponent selected: opponent")
                if poryadok[0] == True:
                    time.sleep(0.5)
                    print("Shotted!")
                    opponenthealth -= 1
                    poryadok.remove(poryadok[0])
                else:
                    time.sleep(0.5)
                    print("Bullet is blank..")
                    time.sleep(0.5)
                    print("Opponent selected: you")
                    if poryadok[0] == True:
                        time.sleep(0.5)
                        print("Shotted!")
                        yourhealth -= 1
                        poryadok.remove(poryadok[0])
                    else:
                        time.sleep(0.5)
                        print("Bullet is blank..")
                        poryadok.remove(poryadok[0])
                        yourturn = not yourturn
print(f"Заряженных: {live_bullets}")
print(f"Пустых: {blank_bullets}")
print(f"Всего: {total_bullets}")
for l in range(live_bullets):
    poryadok.append(True)
for b in range(blank_bullets):
    poryadok.append(False)
givingitems()
while True:

    random.shuffle(poryadok)
    if opponenthealth == 0:
        time.sleep(1)
        print("You are win!"); exit()
    if yourhealth == 0:
        time.sleep(1)
        print("You are lose!"); exit()
    if not poryadok:
        rounds += 1
        youCuffed = False
        yourturn = True
        total_bullets = int(random.randint(2, 6))
        blank_bullets = int(random.randint(1, total_bullets - 1))
        live_bullets = int(total_bullets - blank_bullets)
        print(f"Заряженных: {live_bullets}")
        print(f"Пустых: {blank_bullets}")
        print(f"Всего: {total_bullets}")
        for l in range(live_bullets):
            poryadok.append(True)
        for b in range(blank_bullets):
            poryadok.append(False)
        random.shuffle(poryadok)
    if isCuffed == True:
        if yourturn == True and youCuffed == True:
            print("It's your turn, but you are cuffed..")
            yourturn = not yourturn
            cuffcount += 1
            shot()
        elif yourturn == True and youCuffed == False:
            cuffcount += 1
            selcom()
        elif yourturn == False and youCuffed == True:
            cuffcount += 1
            shot()
        elif yourturn == False and youCuffed == False:
            yourturn = not yourturn
            print("Opponent is cuffed. Your turn")
            shot()
    else:
        if yourturn == True:
            selcom()
        elif yourturn == False:
            print("It's not your turn!")
            shot()
        if cuffcount == 2:
            cuffcount = 0
            isCuffed = False
        if rounds == 2:
            givingitems()
            rounds = 0
