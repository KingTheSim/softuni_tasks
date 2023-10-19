start = input().split()

longer = ""
shorter = ""
equal = False
if len(start[0]) > len(start[1]):
    longer = start[0]
    shorter = start[1]
elif len(start[0]) < len(start[1]):
    longer = start[1]
    shorter = start[0]
else:
    longer = start[0]
    shorter = start[1]
    equal = True

result = 0
current = 0
for i in range(len(shorter)):
    c = longer[i]
    b = shorter[i]
    result += ord(longer[i]) * ord(shorter[i])
    current = i
if not equal:
    for a in range(current + 1, len(longer)):
        s = longer[a]
        result += ord(longer[a])

print(result)
