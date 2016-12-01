import future, re, sets, strutils

type Coord = tuple[x: int, y: int]

proc walk(input: string, stopping: (me: Coord) -> bool): int =
  var me: Coord = (x: 0, y: 0)
  var dx, dy, t = 0
  dy = -1

  for m in findAll(input, re"[LR]\d+"):
    case m[0]
      of 'L': t = dx; dx = dy; dy = -t
      else: t = dx; dx = -dy; dy = t
    for i in 1..parseInt(m[1 .. m.high]):
      me.x += dx
      me.y += dy
      if stopping(me):
        return abs me.x + abs me.y

  return abs me.x + abs me.y

var input = readFile "input.txt"
proc neverStop(me: Coord): bool = false
echo "Answer #1: ", walk(input, neverStop)

var places = initSet[Coord]()
proc visited(me: Coord): bool =
  if places.contains(me): return true
  places.incl(me)
  return false
echo "Answer #2: ", walk(input, visited)
