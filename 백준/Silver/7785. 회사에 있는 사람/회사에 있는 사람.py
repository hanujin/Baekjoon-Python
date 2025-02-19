import sys

company = {}
input = sys.stdin.readline

for _ in range(int(input())):
    people, command = input().split()

    if command == "enter":
        company[people] = True
    else:
        del company[people]

print("\n".join(sorted(company.keys(), reverse=True)))