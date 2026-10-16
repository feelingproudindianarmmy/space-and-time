n = 4

print("Formula: one calculation")
total = n * (n+1) // 2
print(" total=",total," steps=1 ")

print("Loop: adds one student at a time.")
total = 0
for student in range(1, n + 1):
    total += student
print(" total=", total," steps=", n)

print("Double Loop: couns every single point.")
total = 0
steps = 0
for student in range(1, n + 1):
    for point in range(1, student + 1):
        total += 1
        steps += 1
print(" total=",total, " steps=",steps)

input("Double loop t n = 4 took 10 steps. Wtch it grow. Press Enter")
for i in [10,100,1000]:
    input("n = " + str(n) + "   Press Enter")
    print("   steps=", n * (n+1) // 2)

n = 4

points = list(range(1, n + 1))
print(" List:",points,"   items:",len(points))

input("Predict: what happens to List size an n grows?Press Enter ")
for size in[4,10,100,1000]:
    print(f"n = {size:<5} List uses {size<5} items in memory")