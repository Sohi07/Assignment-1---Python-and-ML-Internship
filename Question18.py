def anagram():
    str1=input("Enter the first string: ").upper()
    str2=input("Enter the second string: ").upper()
    str1=sorted(str1)
    str2=sorted(str2)
    if (str1==str2):
        print("The two strings are anagrams")
    else:
        print("The strings are not anagrams")
anagram()
            


