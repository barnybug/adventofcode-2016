def walk(board):
    moves = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}
    answer = ''
    for line in open('input.txt'):
        y = next(i for i, row in enumerate(board) if '5' in row)
        x = board[y].index('5')
        for ch in line.strip():
            dx, dy = moves[ch]
            nx = min(max(x + dx, 0), len(board[0])-1)
            ny = min(max(y + dy, 0), len(board)-1)
            if board[ny][nx] != ' ':
                x, y = nx, ny
        answer += board[y][x]
    return answer

board1 = ['123', '456', '789']
print(walk(board1))

board2 = ['  1  ',' 234 ','56789',' ABC ','  D  ']
print(walk(board2))
