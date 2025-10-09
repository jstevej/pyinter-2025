msg = input("Enter a message: ")
new_msg = []
for ch in msg:
    int_ch = ord(ch)
    bch = format(int_ch, "08b")
    new_msg.append(str(bch))
final_msg = " ".join(new_msg)
print(final_msg)