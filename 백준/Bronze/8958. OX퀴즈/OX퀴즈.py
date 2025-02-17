for _ in range(int(input())):
    s = input()
    score = 0
    streak = 0
    for i in s:
        if i == "O":
            streak += 1
            score += streak
        else:
            streak = 0
    print(score)