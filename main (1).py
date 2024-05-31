clearConsole = lambda: print('\n' * 150)

Board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

x = 2
winstates = [[0,0,0,1,0,2],[1,0,1,1,1,2],[2,0,2,1,2,2],[0,0,1,0,2,0],[0,1,1,1,2,1],[0,2,1,2,2,2],[0,0,1,1,2,2],[2,0,1,1,0,2]]

global timeout


def checkForWin ():
  i=0
  while i != 8:
    if Board[winstates[i][0]][winstates[i][1]] == Board[winstates[i][2]][winstates[i][3]] and Board[winstates[i][2]][winstates[i][3]] == Board[winstates[i][4]][winstates[i][5]] and Board[winstates[i][0]][winstates[i][1]] == Board[winstates[i][4]][winstates[i][5]] and Board[winstates[i][4]][winstates[i][5]] != 0: #idk how to make this better so it will bee like that
      return [True, str(Board[winstates[i][4]][winstates[i][5]])]
    #print (i)
    i += 1
    
  return [False]

def modBoard(x, y, value):
  int(x)
  int(y)
  if Board[y][x] == 0:
    del Board[y][x]
    Board[y].insert(x,value)
    return False
  else: 
    return True

def rndrGame():
  print (Board[0])
  print (Board[1])
  print (Board[2])
  print('0,0 1,0 2,0\n0,1 1,1 2,1\n0,2 1,2 2,2')

def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

#clearConsole()
#rndrGame()

def turnprnt():
  global x
  if x == 1:
    print ("It is player 2's turn")
    x = 2
  else:
    print ("It is player 1's turn")
    x = 1
global timeout
timeout = 0
def gameloop(msg, swtchtrn,loop,bruh):
  #clearConsole()
  if bruh: timeout = x = 0
  print (msg)
  print ("USE EXACT COORDS")
  if swtchtrn: turnprnt()
  rndrGame()
  move = input()
  move = Convert(move)
  if modBoard(int(move[0]),int(move[2]),x):
    gameloop("INVALID",False,True,False)
  le = checkForWin()
  
  if le[0]:
    m = "PLAYER " + le[1] + " WINS!!!!!!!!"
    gameloop(m,False,False,False)

  if timeout == 9:
    print ("tie")
  print (timeout)

  if loop: gameloop(" ",True,True,False)



gameloop(" ",True,True,True)



