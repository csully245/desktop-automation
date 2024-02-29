import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Requires two args: filename and set code")
    else:
        filename = sys.argv[1]
        set_code = sys.argv[2]
        with open(filename, "r") as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            if line == "\n" or line[0] == "#":
                continue
            lines[i] = line[0:-1] + f" ({set_code})\n"
        with open(filename, "w") as file:
            file.writelines(lines)
