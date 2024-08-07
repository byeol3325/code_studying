array = input()
boom = input()

string_stack = []
n, m = len(array), len(boom)

for i in range(n):
    string_stack.append(array[i])

    if string_stack[-1] == boom[-1] and len(string_stack) >= m and ''.join(string_stack[-m:]) == boom:
        for _ in range(m):
            string_stack.pop()

print(''.join(string_stack)) if len(string_stack) != 0 else print("FRULA")