import macros
import strutils

proc compile(input: string, setup: string): NimNode {.compiletime.} =
  var caseBody = newNimNode(nnkCaseStmt)
  caseBody.add parseExpr("pc")
  var pc = 0

  template addCase(text): typed =
    var branch = newNimNode(nnkOfBranch)
    branch.add parseExpr($pc)
    branch.add parseExpr(text)
    caseBody.add branch

  for line in input.split("\n"):
    var i = line.split(" ")
    case i[0]
    of "cpy":
      addCase(i[2] & " = " & i[1])
    of "inc":
      addCase("inc " & i[1])
    of "dec":
      addCase("dec " & i[1])
    of "jnz":
      let n = i[2].parseInt
      addCase("if " & i[1] & " > 0: pc += " & $n & "; continue")
    else:
      discard
    inc pc

  let e = newNimNode(nnkElse)
  e.add parseStmt("discard")
  caseBody.add e

  var loopBody = newStmtList()
  loopBody.add caseBody
  loopBody.add parseExpr("inc pc")

  var stmts = newStmtList()

  template addStmt(text): typed =
    stmts.add parseStmt(text)

  addStmt(setup)
  addStmt("var pc: int")
  var loop = newNimNode(nnkWhileStmt)
  loop.add parseExpr("pc < " & $pc)
  loop.add loopBody
  stmts.add loop

  addStmt "echo a"
  # echo stmts.repr
  result = stmts

macro compileFile(filename: string, setup: string): typed =
  compile(staticRead(filename.strval), setup.strval)

proc answer1 = compileFile("input.txt", "var a, b, c, d: int")
proc answer2 = compileFile("input.txt", "var a, b, c, d: int\nc = 1")
answer1()
answer2()
