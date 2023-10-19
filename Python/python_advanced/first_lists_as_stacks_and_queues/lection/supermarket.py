from collections import deque

current_queue = deque()
while True:
    command = input()

    if command == "End":
        print(f"{len(current_queue)} people remaining.")
        break

    elif command == "Paid":
        while current_queue:
            print(current_queue.popleft())

    else:
        current_queue.append(command)
