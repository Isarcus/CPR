import cpr_parser
import sys

def bold(text: str) -> str:
    """
    Simple function to make text appear bold in terminals that implement ANSI escape codes
    """

    return f"\033[1m{text}\033[0m"

def print_help():
    """
    Print the general help menu for using the CPR utility
    """

    print(" * * * CPR Help Menu * * * ")
    print(" -> Usage: {}".format(bold("CPR [src] [dst] [srcdir1] <srcdir2> ...")))
    print(" -> Note: dir1 and dir2 refer to optional directories to recursively search for .cpp files.\n")

def main():
    argc = len(sys.argv)

    # Probably asking for help in this case
    if argc == 2:
        if sys.argv[1] == '-h':
            print_help()
        else:
            print("Incorrect usage!")
            print(" -> Use {} to display the help menu!".format(bold("CPR - h")))
            return
    # Need >=4 args for this utility to so anything meaningful
    elif argc < 4:
        print(f"Incorrect number of args: {argc}\n")
        print(" -> Use {} to display the help menu!".format(bold("CPR - h")))
        return
    
    # Assume all good from this point on
    for arg in sys.argv[3:]:
        cpr_parser.recurse(arg)

if __name__ == '__main__':
    main()
