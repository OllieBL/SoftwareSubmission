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
            try:
                stack.append(redostack[len(stack)])
            except:
                continue
        else:
            stack.append(word)
            redostack.append(word)
            if undid == 1:
                redostack = stack.copy()
                undid = 0
    for i in stack:
        print(i)