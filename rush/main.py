#!/usr/bin/env python3
from check_mate import checkmate

def main():
    # ทดสอบกระดาน
    board = """\
.....
..K..
.....
.....
.....\
"""
    checkmate(board)

if __name__ == "__main__":
    main()  