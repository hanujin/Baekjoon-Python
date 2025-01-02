from collections import Counter

word = input().upper()
count = {}

count = Counter(word)

max_count = max(count.values())
most_common = [key for key, value in count.items() if value == max_count]  

if len(most_common) > 1:
    print("?")
else:
    print(most_common[0]) 