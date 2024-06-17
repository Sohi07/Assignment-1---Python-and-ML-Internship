def read_and_print_lines():
    print("Enter lines")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    for line in lines:
        print(line)

read_and_print_lines()
