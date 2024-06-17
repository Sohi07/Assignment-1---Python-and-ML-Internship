def write_to_file():
    text = input("Please enter text: ")
    file_name = "output.txt"
    with open(file_name, "w") as file:
        file.write(text)
    print(f"The text has been written to {file_name}")

write_to_file()
