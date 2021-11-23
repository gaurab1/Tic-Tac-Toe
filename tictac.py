t = [['.','.','.'],['.','.','.'],['.','.','.']]
s = [1,2,3,4,5,6,7,8,9]

game = True
ch = 'O'

def render(threex3_list):
    for i in threex3_list:
        for j in i:
            print(j,end = '|')
        print()
        print("------")

def pick(t,k,ch):
    if k == 1:
        t[0][0] = ch
    if k == 2:
        t[0][1] = ch
    if k == 3:
        t[0][2] = ch
    if k == 4:
        t[1][0] = ch
    if k == 5:
        t[1][1] = ch
    if k == 6:
        t[1][2] = ch
    if k == 7:
        t[2][0] = ch
    if k == 8:
        t[2][1] = ch
    if k == 9:
        t[2][2] = ch
    

def checkout(t):
    global game
    if t[0][0] == t[0][1] == t[0][2] == 'X' or t[1][0] == t[1][1] == t[1][2] == 'X' or t[2][0] == t[2][1] == t[2][2] == 'X' or t[0][0] == t[1][0] == t[2][0] == 'X' or t[0][1] == t[1][1] == t[2][1] == 'X' or t[0][2] == t[1][2] == t[2][2] == 'X' or t[0][0] == t[1][1] == t[2][2] == 'X' or t[0][2] == t[1][1] == t[2][0] == 'X':
        render(t)
        print('X wins!')
        game = False
    if t[0][0] == t[0][1] == t[0][2] == 'O' or t[1][0] == t[1][1] == t[1][2] == 'O' or t[2][0] == t[2][1] == t[2][2] == 'O' or t[0][0] == t[1][0] == t[2][0] == 'O' or t[0][1] == t[1][1] == t[2][1] == 'O' or t[0][2] == t[1][2] == t[2][2] == 'O' or t[0][0] == t[1][1] == t[2][2] == 'O' or t[0][2] == t[1][1] == t[2][0] == 'O':
        render(t)
        print('O wins!')
        game = False


while game:
    render(t)
    if len(s) == 0:
        print("Draw Game!")
        break
    else:
        if ch == 'X':
            ch = 'O'
        else:
            ch = 'X'
        print()    
        spot = int(input("Pick number from 0-9 for "+ch+"\n"))
        print()
        s.remove(spot)
        pick(t,spot,ch)
        checkout(t)
        
    
    
        
