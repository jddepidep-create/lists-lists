score = []

for i in range(1,6):
    scores = int(input("Enter quiz boi"))
    score.append(scores)

print(score)
count = len(score)
total = sum(score)
avr = total / count
high = max(score)
low = min(score)
print(count)
print(total)
print(f"avr:{avr:.2f}")
print(high)
print(low)
order = sorted(score)
print(order)