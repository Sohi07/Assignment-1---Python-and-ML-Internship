def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")


source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")
copy_file(source_file, destination_file)
