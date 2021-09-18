import sys


def linux_interaction():
    # assert ("linux" in sys.platform), "Function will run only on linux"
    print("Doing Something")


try:
    linux_interaction()
except AssertionError as ass_error:
    print(ass_error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print("Cleaning up, irrespective of any exception!")
