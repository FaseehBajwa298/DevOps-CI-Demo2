#!/usr/bin/env python3
import sys


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "DevOps-CI-Demo2"
    print(f"Hello, {name}! Feature update is live.")


if __name__ == "__main__":
    main()