haystack = "hello"
needle = "ll"

needle_length = len(needle)
starting_letter = needle[0]

print(haystack[2:needle_length+2])

for i, char in enumerate(haystack):
    if char == starting_letter and haystack[i:needle_length] == needle:
        print(i)

print(-1)

