prime_sum = 0
non_prime_sum = 0

while True:
    comm = input()
    if comm == "stop":
        break
    else:
        comm = int(comm)

    if comm < 0:
        print("Number is negative.")
        continue
    elif comm == 0:
        continue
    counter = 0
    for n in range(1, comm + 1):
        if comm % n == 0:
            counter += 1

    if counter == 2:
        prime_sum += comm
    else:
        non_prime_sum += comm

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
