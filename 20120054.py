t = int(input())


bingo = [2 for i in range(0,5)  for j in range(0,5)]
for i in range(t) :
    for i in range(0,5) :
        bingo[i] = [int(x) for x in input().split()] 
    number = [int(x) for x in input().split()]

    for k in range(len(number)) :
    
        for i in range(0,5) :
            for j in range(0,5) :
                if(bingo[i][j] == number[k]) :
                    bingo[i][j] = 0
                    break
        if((bingo[0][0]==0) and(bingo[0][1]==0) and (bingo[0][2]==0) and (bingo[0][3]==0) and (bingo[0][4]==0)):
            print(k+1)
            break
        elif((bingo[1][0]==0) and(bingo[1][1]==0) and (bingo[1][2]==0) and (bingo[1][3]==0) and (bingo[1][4]==0)):
            print(k+1)
            break
        elif((bingo[2][0]==0) and(bingo[2][1]==0) and (bingo[2][2]==0) and (bingo[2][3]==0) and (bingo[2][4]==0)):
            print(k+1)
            break
        elif((bingo[3][0]==0) and(bingo[3][1]==0) and (bingo[3][2]==0) and (bingo[3][3]==0) and (bingo[3][4]==0)):
            print(k+1)
            break
        elif((bingo[4][0]==0) and(bingo[4][1]==0) and (bingo[4][2]==0) and (bingo[4][3]==0) and (bingo[4][4]==0)):
            print(k+1)
            break
        elif((bingo[0][0]==0) and(bingo[1][0]==0) and (bingo[2][0]==0) and (bingo[3][0]==0) and (bingo[4][0]==0)):
            print(k+1)
            break
        elif((bingo[0][1]==0) and(bingo[1][1]==0) and (bingo[2][1]==0) and (bingo[3][1]==0) and (bingo[4][1]==0)):
            print(k+1)
            break
        elif((bingo[0][2]==0) and(bingo[1][2]==0) and (bingo[2][2]==0) and (bingo[3][2]==0) and (bingo[4][2]==0)):
            print(k+1)
            break
        elif((bingo[0][3]==0) and(bingo[1][3]==0) and (bingo[2][3]==0) and (bingo[3][3]==0) and (bingo[4][3]==0)):
            print(k+1)
            break
        elif((bingo[0][4]==0) and(bingo[1][4]==0) and (bingo[2][4]==0) and (bingo[3][4]==0) and (bingo[4][4]==0)):
            print(k+1)
            break
        elif((bingo[0][0]==0) and(bingo[1][1]==0) and (bingo[3][3]==0) and (bingo[4][4]==0)):
            print(k+1)
            break
        elif((bingo[0][4]==0) and(bingo[1][3]==0) and (bingo[3][1]==0) and (bingo[4][0]==0)):
            print(k+1)
            break
        elif((bingo[0][0]==0) and(bingo[0][4]==0) and (bingo[4][0]==0) and (bingo[4][4]==0)):
            print(k+1)
            break
