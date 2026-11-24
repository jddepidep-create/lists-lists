score = []

for i in range(5):
    scores = input("Enter order boi")
    score.append(scores)
print(score)
additional = input("Enter additional order boi")
score.append(additional)
print(score)
priority = input("Enter priority order boi")
score.insert(0,priority)
print(score)
search = input("Enter search boi")
try:
    count = count(search)
    index = search.index(search)
    print(count, index)
except ValueError:
    print("order no find")
cancel = input("Enter cancel order boi")
score.remove(cancel)
print(score)
score.pop()
print(score)
removed = score.index(5)
print(removed)
remain = score.sort(key=str.lower)
print(remain)
final = len(remain)
print(final)



