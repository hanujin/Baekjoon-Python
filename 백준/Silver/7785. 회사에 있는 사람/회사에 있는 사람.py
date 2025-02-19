company = set()

for _ in range(int(input())):
    people, command = input().split()

    if command == "enter":
        company.add(people)
    elif command == "leave":
        company.discard(people)

print("\n".join(sorted(company, reverse=True)))