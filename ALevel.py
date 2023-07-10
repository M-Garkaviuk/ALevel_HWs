import sys
a = [10, 20, 30, 40, 50]
print(sys.argv)
for id, item in enumerate(a):
    a[id] = item + 5

print(a)
