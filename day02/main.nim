import strutils, tables

type Pos = tuple[x: int, y: int]
var moves = {'L': (x: -1, y: 0), 'R': (x: 1, y: 0), 'U': (x: 0, y: -1), 'D': (x: 0, y: 1)}.toTable

proc walk(board: seq[string]): string =
  var answer = ""
  var start: Pos
  var lookup = initTable[Pos, char]()
  for y, line in pairs board:
    for x, ch in pairs line:
      lookup[(x,y)] = ch
      if ch == '5':
        start = (x, y)

  for line in lines "input.txt":
    var pos = start
    for ch in line:
      var d = moves[ch]
      var n = (pos.x + d.x, pos.y + d.y)
      if lookup.contains(n):
        pos = n

    add answer, board[pos.y][pos.x]
  answer

let board1 = @["123", "456", "789"]
echo "Answer #1: ", walk(board1)

let board2 = @["  1  "," 234 ","56789"," ABC ","  D  "]
echo "Answer #2: ", walk(board2)
