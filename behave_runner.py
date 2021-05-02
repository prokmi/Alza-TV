from behave.__main__ import main as behave_main
import os

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    behave_main("features")
