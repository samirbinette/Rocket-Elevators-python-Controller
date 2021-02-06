
def best_Elevator(optionA ,optionB ,requested ,status ,directionA ,directionB):

    status
    requested
    optionA
    optionB
    directionA
    directionB
    # The conditions for finding the best elevator;
    if status == 'none' and requested == optionA:
        for number in range(requested):
            print(requested)
    elif status == 'none' and requested == optionB:
        for number in range(requested):
            print(requested)
    elif ((status == 'up' or status == 'down') and directionA == 'idle' and optionA < 5 and 5 > requested and optionA > requested) or ((status == 'up' or status == 'down') and  directionA=='idle' and optionA > 5 and requested > 5  and  optionA > requested)or((status == 'up' or status    == 'down' )and directionB == 'moving' and (optionB < 10 or optionB > 0)):
        print("ELEVATOR A IS COMMING 1")
        for requested in range(optionA):
            print(optionA)
            optionA -= 1
            if (optionA == requested - 1):
                break
        print("Door Open")

    elif ((status == 'up' or status == 'down') and directionB == 'idle' and optionB < 5 and requested < 5 and optionB > requested) or (( status == 'up' or status == 'down') and directionB == 'idle' and optionB < 5 and requested <= 5 and optionB < requested) or ((status == 'up' or status == 'down') and directionB == 'idle' and optionB > 5 and requested < 5 and optionB > requested):
        print("Elevator B 2")
        for requested in range(optionB):
            print(optionB)
            optionB -= 1
            if (optionB == requested - 1):
                break
        print("Door Open")
    elif(status == 'up' or status == 'down') and  directionA=='idle'  and optionA < 5 and requested < 5  and  optionA < requested or((status == 'up' or status == 'down') and directionA == 'idle' and optionA > 5 and requested > 5 and optionA < requested):
        print("Elevator A is comming 3")
        for requested in range(optionA):
            print(optionA)
            optionA += 1
            if (optionA == requested + 1):
                break
    elif((status == 'up' or status == 'down') and  directionB =='idle' and optionB > 5 and requested > 5  and  optionB < requested) or ((status == 'up' or status == 'down') and directionB == 'idle' and optionB > 5 and requested > 5 and optionB < requested):
        print("Elevator B is comming to 9")
        for number in range(optionB):
            print(optionB)
            optionB += 1
            if (optionB == requested + 1):
                break
        print("Door Open")
    else:
        print('fail')

    return optionA, optionB, requested, status, directionA, directionB

def thePersonisinside(floor,choice):

    buttomList = [1,2,3,4,5,6,7,8,9,10]
    floor
    choice

    print("choose your destination")
    print(buttomList,'\n your choice is:', choice)

    if choice > 10:
     print("invalid answer")
     return thePersonisinside()
    elif choice < 0:
     print("invalid answer")
     return thePersonisinside()

    else:
        if floor < choice:
            for number in range(10):
               print(floor)
               floor +=1
               if (floor == choice+1):
                  break
        elif floor > choice:
            for number in range(10):
                print(floor)
                floor -=1
                if (floor == choice-1):
                    break

        return floor, choice

def scenario1():
    print("scenario 1")
    print("___________________________________________________________________________________________")
    best_Elevator(2, 6, 3, 'up', 'idle', 'idle')
    print("door close")
    thePersonisinside(3, 7)

    print("door open")

    print('___________________________________________________________________________________________')

def scenario2():
    print('SCENARIO 2')
    print('___________________________________________________________________________________________');
    best_Elevator(10, 3, 1, 'up', 'idle', 'idle')
    print('door close')
    thePersonisinside(1, 6)
    print('door open')
    print('door close')
    print('\n ----------2 minutes later--------------')
    best_Elevator(10, 6, 3, 'up', 'idle', 'idle')
    thePersonisinside(3, 5)
    print('door open')
    print('third person')
    best_Elevator(7, 5, 9, 'down', 'idle', 'idle')
    thePersonisinside(9, 2)

    print('___________________________________________________________________________________________')

def scenario3():
    print('Scenario 3')
    print('___________________________________________________________________________________________')
    best_Elevator(10, 0, 3, 'down', 'idle', 'moving')
    print('door open')
    print('door close')
    thePersonisinside(3, 2)

    print('----------5 minutes later--------------')

    best_Elevator(2, 6, 10, 'up', 'idle', 'idle')
    print('door close')
    thePersonisinside(10, 3)
    print('door open')

    print('___________________________________________________________________________________________')

