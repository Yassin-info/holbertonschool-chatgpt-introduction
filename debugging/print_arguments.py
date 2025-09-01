#!/usr/bin/python3
import sys

def main():
    """Print all arguments passed to the script, excluding the script name."""
    for arg in sys.argv[1:]:
        print(arg)

if __name__ == "__main__":
    main()
