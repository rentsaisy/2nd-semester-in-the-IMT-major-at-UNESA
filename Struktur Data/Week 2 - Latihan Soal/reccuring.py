# Function
def first_recurring_char(s):
    seen = set()
    
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    
    return None  # If no recurring character

# Input
print(first_recurring_char("abcdeaf"))   # a
print(first_recurring_char("abcd"))      # None
print(first_recurring_char("aabbcc"))    # a