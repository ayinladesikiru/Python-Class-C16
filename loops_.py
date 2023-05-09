for i in range(1, 13):
    print()
    for j in range(1, 13):
        print(f"{i} x {j} = {i * j}", end="\t\t")

names = ['sultan', 'david', 'mariam', 'lateef']
for name in names:
    if name.startswith("j"):
        print("found")
        break
else:
    print("not found")


score = int(input("Enter your score: "))
result = "You fail this course" if score >= 40 else "You passed, congratulations"
