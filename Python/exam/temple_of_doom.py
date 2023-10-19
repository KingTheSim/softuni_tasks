from collections import deque

tools = deque(int(x) for x in input().split())
substances = deque(int(x) for x in input().split())
challenges = [int(x) for x in input().split()]

while True:
    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break
    if not tools or not substances and challenges:
        print("Harry is lost in the temple. Oblivion awaits him.")
        break
    cur_tool = tools.popleft()
    cur_substance = substances.pop()

    if cur_tool * cur_substance in challenges:
        challenges.remove(cur_substance * cur_tool)
    else:
        tools.append(cur_tool + 1)
        cur_substance -= 1
        if cur_substance > 0:
            substances.append(cur_substance)

if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")
