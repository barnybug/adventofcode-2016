def board_buttons(board):
    buttons = {}
    board = board.split('\n')
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            button = {}
            if j > 0:
                button['L'] = row[j-1]
            if j < len(row)-1:
                button['R'] = row[j+1]
            if i > 0:
                button['U'] = board[i-1][j]
            if i < len(board)-1:
                button['D'] = board[i+1][j]
            button = {k: v for k, v in button.items() if v != ' '}
            buttons[col] = button
    return buttons

def walk(board):
    buttons = board_buttons(board)
    answer = ''
    for line in open('input.txt'):
        pos = '5'
        for ch in line:
            if ch in buttons[pos]:
                pos = buttons[pos][ch]
        answer += pos
    return answer

board1 = '123\n456\n789'
print(walk(board1))

board2 = '  1  \n 234 \n56789\n ABC \n  D  '
print(walk(board2))
