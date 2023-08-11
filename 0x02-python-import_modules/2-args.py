#!/usr/bin/python3
if __name__ == "__main__":
    main()
    """prints the number of and the list of its arguments"""
    import sys

def main():
    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print(f"{argc} arguments:")

    for i, arg in enumerate(argv, 1):
        print(f"{i}: {arg}")
