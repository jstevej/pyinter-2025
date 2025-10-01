binary_message = input("Enter a binary message: ")
message = ""

for byte in binary_message.split():
    message += chr(int(byte, 2))

print(f"The message is: {message}")

