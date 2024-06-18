import string
def remove_punctuation(string1):
    translator = str.maketrans('', '', string.punctuation)
  
    return string1.translate(translator)
input_string = input("Enter the string")
cleaned_string = remove_punctuation(input_string)
print("Original string:", input_string)
print("String without punctuation:", cleaned_string)
