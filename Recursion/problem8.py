# Q8. Palindrome Check (string same hai ya nahi)

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("madam"))
print(is_palindrome("vikas"))


# Logic:

# Compare first aur last character
# Agar same hai → beech ka part check karo
# Agar different hai → False

# Real Life:

# Mirror me dekho — left aur right dono sides same honi chahiye (palindrome mirror logic).