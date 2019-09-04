from memento import Data

d = Data()
repeats = 10

for i in range(repeats):
    d.save()
    d.numbers.append(i)
d.save()
print(d.numbers)

print("below is how undo works")
# Undo
for i in range(repeats):
    d.undo()
    print(d.numbers)
