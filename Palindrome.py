def palindrome(inp):
    rev = inp[::-1]
    if inp == rev:
        return True
    else:
        return False
pal = input("Enter Your Palindrome: ")
print(palindrome(pal))
