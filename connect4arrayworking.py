#this file will work with a 2d array
# ____________________
#|F1|F2|F3|F4|F5|F6|F7|
#|E1|E2|E3|E4|E5|E6|E7|
#|D1|D2|D3|D4|D5|D6|D7|
#|C1|C2|C3|C4|C5|C6|C7|
#|B1|B2|B3|B4|B5|B6|B7|
#|A1|A2|A3|A4|A5|A6|A7|

#win conditions  
#horizontally 4 per Row x6 equal 24
#vertically 3 per column x7 equal 21
#diagonally 1 2 3 3 2 1  x2because mirror equal 24
## array2d[row][column]
import sys
import time #we need this for pause



width=7           #widthfrom[0-6]
height=6          #height[0-5]
array2d=[[0 for x in range (width)] for y in range (height)]#created board
columnCapacity=[0 for x in range(width)] #used in coulumnCapacity function


#intializeboard as '_'
sety=0         #this is a counter of current height
while (sety<(height)):
    setx=0
    while(setx< (width)):
       # print("sety loop[%s][%s]"%(sety, setx))
        array2d[sety][setx]='_'
        setx=setx+1       #move to the right
    sety= sety+1        #move up one 


#Testing position
#array2d[1][1]= 4
#array2d[2][0]=2
#array2d[5][0]=6

#function draws the board and gets values from array2d
def drawboard():
    print("               |_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" %(array2d[5][0], array2d[5][1], array2d[5][2], array2d[5][3], array2d[5][4], array2d[5][5], array2d[5][6]))
    print("               |_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" %(array2d[4][0], array2d[4][1], array2d[4][2], array2d[4][3], array2d[4][4], array2d[4][5], array2d[4][6]))
    print("               |_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" %(array2d[3][0], array2d[3][1], array2d[3][2], array2d[3][3], array2d[3][4], array2d[3][5], array2d[3][6]))
    print("               |_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" %(array2d[2][0], array2d[2][1], array2d[2][2], array2d[2][3], array2d[2][4], array2d[2][5], array2d[2][6]))
    print("               |_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" %(array2d[1][0], array2d[1][1], array2d[1][2], array2d[1][3], array2d[1][4], array2d[1][5], array2d[1][6]))
    print("               |_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|_%s_|" %(array2d[0][0], array2d[0][1], array2d[0][2], array2d[0][3], array2d[0][4], array2d[0][5], array2d[0][6]))
    print("                 0   1   2   3   4   5   6 ")

#Column is the current coulmn they are trying to drop a chip into
#Marker is either an X or an O
#this drops a chip in the next availble top row
def dropChip(column, marker):
    row=0
    while( array2d[row][column]=='X' or array2d[row][column]=='O' ):
        row= row+1
    
    array2d[row][column] = marker


def isColumnFull(column):
    #columnCapacity=[0,0,0,0,0]
    print ("myCloumnCapacity%s%s%s%s%s" %(columnCapacity[0],columnCapacity[1],columnCapacity[2],columnCapacity[3],columnCapacity[4]))
    if (columnCapacity[column]==5):
        return True
    else:
        return False
    


# we pass 1 or 2, and we pass marker X or O
def winCondition(player,letter):
    letter
    print("NOTE:win condition called and marker is %s" % (letter))
    upshift=0
    while(upshift<=5):
        rightshift=0
        while(rightshift <= 3):#make them equal to marker
            #print("we are checking array2d[%d][%d]" %((upshift),(rightshift) )) #array2d[upshift][1 + rightshift]   array2d[upshift][2 + rightshift]  array2d[upshift][3 + rightshift])")
            if((((array2d[upshift][0+ rightshift]== letter)and array2d[upshift][1+ rightshift]==letter) and array2d[upshift][2+ rightshift]==letter) and array2d[upshift][3 + rightshift]==letter):    
                print("player %d wins horizontally!!!!" %(player))
                time.sleep(1)
            rightshift=rightshift+1
        upshift= upshift+1
        #print("NOTE:upshift is now %d" % (upshift))


    #we will check vertical win
    print("we are entering win condition vertical check")
    upshift=0
    while(upshift<=2):
        rightshift=0
        while (rightshift<=6):
            #print("we are checking array2d[%d][%d]"% (upshift,rightshift))
            if(  (array2d[0+ upshift][rightshift]== letter)and(array2d[1+ upshift][rightshift]==letter)and(array2d[2+ upshift][rightshift])and(array2d[3+ upshift][rightshift]==letter)):
                  print("player %d wins vertically!!!!"%(player))
                  #do something to terminate
            rightshift=rightshift+1
        upshift=upshift+1

    #we will check diagonal upright wins
    upshift=0
    while(upshift<=2):
        rightshift=0
        while(rightshift<=3):
            if( (((array2d[0+ upshift][0+ rightshift]==letter) and (array2d[1+ upshift][1+ rightshift]==letter) and (array2d[2+ upshift][2+ rightshift]==letter)) and (array2d[3+ upshift][3+ rightshift]==letter))):
                print("Player %d wins diagonally upright!!! " % player)
                time.sleep(2)
            rightshift= rightshift+1
        upshift= upshift+1

    #upleft win condition
    upshift=0
    while(upshift<=2):
        leftshift=0
        while(leftshift<=3):
            if( (((array2d[0+ upshift][6 - leftshift]== letter) and (array2d[1+ upshift][5- leftshift]== letter)) and (array2d[2+upshift][4-leftshift]==letter))and (array2d[3+upshift][3- leftshift]==letter)):
                print("Player  %d wins diagonally downright!!!!" % player)
                time.sleep(2)
            leftshift=leftshift+1
        upshift=upshift+1

def main():
    isColumnFull(4)
    drawboard()
    turn=1
    overfill=[0]*7
    #print("overfill[%d][.][.][%d]" % (overfill[0],overfill[6]))
    while(turn<42):
        print("NOTE: The current turn is %d." %(turn))
        if(turn% 2 == 1):
            marker='X'
            ##this is for overfill
            overfilled=True
            while(overfilled==True):
                number = int (input("Hello player 1, Where would you like to drop your piece?\n"))
                if(number==0 or number==1 or number==2 or number==3 or number==4 or number==5 or number==6):
                    overfill[number]=overfill[number]+1
                    if(6 < overfill[number]):
                        print("This Colomn is filled. try again..")
                        overfilled=True
                    else:
                        overfilled=False
                #out of range taken care of here
                else:
                    print("Column is out of range. try again..")
                    overfilled=True

            dropChip(number, marker)
            drawboard()
            winCondition(1, marker)
            turn= turn+1


        else:
            marker='O'
            number = int (input("Hello player 2 Where would you like to drop your piece?\n"))
            dropChip(number, marker)
            drawboard()
            winCondition(2, marker)
            turn= turn+1
main()
