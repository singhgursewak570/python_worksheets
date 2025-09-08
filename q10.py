# Q10
def classify_temperature(t):
    if t < 15:
        return "Cold"
    elif t >= 15 and t <= 30:
        return "Moderate"
    else:
        return "Hot"

print(classify_temperature(10))
print(classify_temperature(20))
print(classify_temperature(35))

