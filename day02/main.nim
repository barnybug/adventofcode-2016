import strutils, tables

type Pos = tuple[x: int, y: int]
var moves = {'L': (x: -1, y: 0), 'R': (x: 1, y: 0), 'U': (x: 0, y: -1), 'D': (x: 0, y: 1)}.toTable

proc walk(board: seq[string]): string =
  var answer = ""
  var start: Pos
  for y, line in pairs board:
    start.x = line.find "5"
    if start.x != -1:
      start.y = y
      break

  for line in lines "input.txt":
    var pos = start
    for ch in line:
      var d = moves[ch]
      var nx = pos.x + d.x
      var ny = pos.y + d.y
      if nx >= 0 and ny >= 0 and ny < len(board) and nx < len(board[0]) and board[ny][nx] != ' ':
        pos = (x: nx, y: ny)

    add answer, board[pos.y][pos.x]
  answer

let board1 = @["123", "456", "789"]
echo "Answer #1: ", walk(board1)

let board2 = @["  1  "," 234 ","56789"," ABC ","  D  "]
echo "Answer #2: ", walk(board2)
