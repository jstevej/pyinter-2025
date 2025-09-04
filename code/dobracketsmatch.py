while True:
    statement = input("Enter a statement: ")
    stack = []
    brackets = {"(": ")", "[": "]", "{": "}"}
    matched = True

    for ch in statement:
        if ch in brackets:
            stack.append(ch)
        elif ch in brackets.values():
            if len(stack) == 0 or brackets[stack.pop()] != ch:
                matched = False
                break

    if matched and len(stack) == 0:
        print("Brackets match")
    else:
        print("Brackets don't match")
