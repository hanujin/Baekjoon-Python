def is_groupword(word):
    seen = set()
    previous_char = None
    
    for char in word:
        if char != previous_char:
            if char in seen:
                return False
            seen.add(char)
        previous_char = char
    return True

N = int(input())
words = [list(input()) for _ in range(N)]

count = sum(is_groupword(word) for word in words)
print(count)