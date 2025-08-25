stack = []
redostack = []
undid = 0
while True:
    word = input('add words ')
    if word == 'undo':
        stack.pop()
        undid = 1
    else:
        if word == 'redo':
            stack = redostack.copy()
        else:
            stack.append(word)
            redostack.append(word)
            if undid == 1:
                redostack = stack.copy()
                undid = 0
    for i in stack:
        print(i)