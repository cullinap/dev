plain_text = "This is a test. ABC, abc"

encrypted_text = ""

for c in encrypted_text:
    x = ord(c)
    x+=1
    c2 = chr(x)
    encrypted_text = encrypted_text + c2

print(encrypted_text)
