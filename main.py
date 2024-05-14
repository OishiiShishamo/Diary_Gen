import pandas as pd
from pathlib import Path
import os
import shutil
import git
import atexit
import sys

def _write():
    print("year>", end="")
    year = input()
    print("month>", end="")
    month = input()
    print("day>", end="")
    day = input()
    print("sleep>", end="")
    sleep = input()
    print("condition>", end="")
    condition = input()
    print("one word>", end="")
    one_word = input()
    df = pd.DataFrame([year, month, day, sleep, condition, one_word])
    df.to_csv("./diary.csv", mode="a", header=False, encoding="utf-8")
    diary_csv = pd.read_csv("./diary.csv")
    

def _read():
    print(pd.read_csv("./diary.csv"))

def main():
    while(1):
        print("読む？書く？(default = 書く)>", end="")
        mode = input()
        match(mode):
            case mode if mode == "書く":
                _write()
            case mode if mode == "読む":
                _read()
            case mode if mode == "exit":
                sys.exit()
            case _:
                _write()

main()