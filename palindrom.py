def is_palindromes(text):
    left=0
    right=len(text)-1
    while left<right:
        if text[left]!=text[right]:
            return False
        left +=1
        right -=1
    return True
print(is_palindromes("eye"))