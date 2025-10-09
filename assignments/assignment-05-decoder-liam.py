msg = input("Enter a binary message: ").split()
new_msg = []
for ch in msg:
    int_ch = int(ch, 2)
    str_ch = chr(int_ch)
    new_msg.append(str_ch)
final_msg = "".join(new_msg)
print(final_msg)