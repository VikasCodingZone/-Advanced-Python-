# Q10. Count vowels in a string

def count_vowels(s):
    vowels = "aeiouAEIOU"
    if s == "":
        return 0
    return (1 if s[0] in vowels else 0) + count_vowels(s[1:])

print(count_vowels("Vikas Kushwaha"))

# Logic:

# Har character check karta hai vowel hai ya nahi
# → fir string ke remaining part pe recursion chalata hai.