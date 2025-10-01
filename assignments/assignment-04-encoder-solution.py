message = input("Enter a message: ")
binary_message = ""

for ch in message:
    binary_message += format(ord(ch), "08b") + " "

print(f"Your message in binary is: {binary_message}")
