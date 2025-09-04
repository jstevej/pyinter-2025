for i in range(1000000):
    message = f"This message contains {i} characters."
    if len(message) == i:
        print(message)
