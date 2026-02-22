# Function
def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase (optional but recommended)
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # If lengths are different, they can't be anagrams
    if len(str1) != len(str2):
        return False
    
    count = {}
    
    # Count characters in first string
    for char in str1:
        count[char] = count.get(char, 0) + 1
    
    # Subtract counts using second string
    for char in str2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
    
    return True

# Input
print(is_anagram("listen", "silent"))   # True
print(is_anagram("triangle", "integral"))  # True
print(is_anagram("apple", "pale"))  # False