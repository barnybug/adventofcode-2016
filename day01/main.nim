import re, sets, strutils

var input = readFile "input.txt"
type Coord = tuple[x: int, y: int]
var places = initSet[Coord]()
var me: Coord = (x: 0, y: 0)
var dx, dy, t = 0
var first = true
dy = -1
for m in findAll(input, re"[LR]\d+"):
  case m[0]
    of 'L': t = dx; dx = dy; dy = -t
    of 'R': t = dx; dx = -dy; dy = t
    else: discard
  for i in 1..parseInt(m[1 .. m.high]):
    me.x += dx
    me.y += dy
    if places.contains(me) and first:
      echo "Answer #2: ", abs me.x + abs me.y
      first = false
    else:
      places.incl(me)
echo "Answer #1: ", abs me.x + abs me.y
