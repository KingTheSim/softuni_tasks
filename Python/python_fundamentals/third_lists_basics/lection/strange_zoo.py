tail= input()
body = input()
head = input()

whole = [tail, body, head]
whole[0], whole[2] = whole[2], whole[0]

print(whole)
