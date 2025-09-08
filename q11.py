txt = "Emma is good. Emma plays chess. Emma is nice."
c = 0
for i in range(len(txt)-3):
    if txt[i:i+4] == "Emma":
        c = c + 1
print("COUNT:", c)
