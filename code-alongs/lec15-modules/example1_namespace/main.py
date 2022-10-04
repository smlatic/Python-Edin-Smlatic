import os, sys

os.system("cls||clear")

print(f"{'='*30}main.py{'='*30}")

# code imported from another module is executed when imported
import module1 as m1

# note __name__ is module1 when ran from outside of module1.py

print(f"\n{'='*30}main.py{'='*30}")
