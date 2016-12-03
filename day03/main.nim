import algorithm, re, sequtils, strutils

proc answer1(): int =
  var possible = 0
  for line in lines "input.txt":
    var t = line.strip.split(re"\s+").map(parseInt)
    sort t, system.cmp
    if t[0] + t[1] > t[2]:
      inc possible
  return possible

proc answer2(): int =
  var possible = 0
  var lines: seq[seq[int]] = @[]
  for line in lines "input.txt":
    var t = line.strip.split(re"\s+").map(parseInt)
    lines.add t
  for tri in lines.distribute((lines.len / 3).toInt):
    for i in 0..2:
      var x = @[tri[0][i], tri[1][i], tri[2][i]]
      sort x, system.cmp
      if x[0] + x[1] > x[2]:
        inc possible
  return possible

echo "Answer #1: ", answer1()
echo "Answer #2: ", answer2()
