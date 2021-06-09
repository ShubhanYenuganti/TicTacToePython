def start():
  print("Welcome to Tic Tac Toe")
  res = "result"
  compl = False

  while(compl != True):
    res = input("Please pick a marker X or O: ")
    if (res == 'X' or res == 'O'):
      compl = True
  
  return res

def display_board(board):
  print(board[1] + " | " + board[2] + " | " + board[3])
  print(board[4] + " | " + board[5] + " | " + board[6])
  print(board[7] + " | " + board[8] + " | " + board[9])

def validate_move(pos,name,board):
  if (board[pos] == 'X' or board[pos] == 'O'):
    print("Area is already occupied")
    if (name == "Player 1"):
      player1_move(board)
    else:
      player2_move(board)
  else:
    return True

def update_board(pos,marker,board):
  board[pos] = marker

def player1_move(board, marker):
  print("Player 1's Move")

  player1_pos = "random"
  
  while(player1_pos.isdigit() == False):
    player1_pos = input("Pick a position (1-9): ")

  if(validate_move(int(player1_pos), "Player 1", board)):
    update_board(int(player1_pos), marker, board)
    print('\n'*10)

    display_board(board)
    return True

def player2_move(board, marker):

  print("Player 2's Move")

  player2_pos = "random"
  while(player2_pos.isdigit() == False):
    player2_pos = input("Pick a position (1-9): ")
    
  if(validate_move(int(player2_pos), "Player 2", board)):
    update_board(int(player2_pos), marker, board)
    print('\n'*10)

    display_board(board)
    return True

def win(board, mark):

  return ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[1] == mark and board[5] == mark and board[9] == mark)) 

def draw(board):
  return board.count('X') + board.count('O')

def runner():

  player1_marker = start()
  player2_marker = ""
  if (player1_marker == 'X'):
    player2_marker = 'O'
  else:
    player2_marker = 'X'

  test_board = ['#','1','2','3','4','5','6','7','8','9']

  display_board(test_board)

  while(win(test_board, player1_marker) == False and win(test_board, player2_marker) == False and draw(test_board) != 9):
    player1_move(test_board, player1_marker)
    if(win(test_board, player1_marker) == False and draw(test_board) != 9):
      player2_move(test_board, player2_marker)
      win(test_board, player2_marker)
      draw(test_board)


  if (draw(test_board) == 9):
    print("Tie!")
  elif (win(test_board, player1_marker)):
    print("Player 1 has won!")
  else:
    print("Player 2 has won!")

  play_again = ""
  compl = False

  while (compl == False):
    play_again = input("Play again? (Y/N): ")
    if (play_again == 'Y' or play_again == 'N'):
      compl = True
  
  if (play_again == 'Y'):
    print('\n'*100)
    runner()

runner()
