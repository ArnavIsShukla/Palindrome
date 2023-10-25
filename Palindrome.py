def palindrome(inp):
    length = len(str(inp))
    i = 0
    for x in inp:
        i += 1
        if not x == inp[length - i]:
            return False
        elif i == round(length / 2):
            return True