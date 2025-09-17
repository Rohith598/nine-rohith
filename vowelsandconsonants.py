def vowels_consonants_count(s):
    vowels=0
    consonants=0
    for i in s.lower():
        if i.isalpha():
            if i in "aeiou":
                vowels+=1
            else:
                consonants+=1
    return vowels,consonants
text="i am rohith"
v,c=vowels_consonants_count(text)
print("vowels:",v)
print("consonants:",c)