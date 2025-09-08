# Q4
def count_case(s):
    d = {"UPPER":0, "LOWER":0}
    for ch in s:
        if ch.isupper():
            d["UPPER"] = d["UPPER"] + 1
        elif ch.islower():
            d["LOWER"] = d["LOWER"] + 1
    return d

print(count_case("Robot is Here"))