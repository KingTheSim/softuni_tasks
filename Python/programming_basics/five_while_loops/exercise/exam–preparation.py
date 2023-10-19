# user input
fail_target = int(input())
task = input()
total_score = 0
fail_score = 0
failed = False
score_count = 0
last_task = ""

# logic
while task != "Enough":
    score = float(input())
    total_score += score
    if score <= 4:
        fail_score += 1
        if fail_score == fail_target:
            failed = True
            break
    score_count += 1
    last_task = task
    task = input()

aver = total_score / score_count
# code output
if failed:
    print(f"You need a break, {fail_target} poor grades.")
else:
    print(f"Average score: {aver:.2f}")
    print(f"Number of problems: {score_count}")
    print(f"Last problem: {last_task}")
