# PyWriter

A Python program to type out a preselected file with keyboard inputs.
This program also adds some organic feel to it by delaying each keystroke by a random value, that can be configured.

## Warning:
This project automatically installs pynput [https://github.com/moses-palmer/pynput] from pip when running the script.
Please make sure, you want to install this library on your computer.

## Usage:

The program can be executed with the following parameters:

Flag | Value Type | Standard Value | Description
---- | ---------- | -------------- | -----------
-f/--file | file | sys.argv[0] | The file you want the program to type out. If this parameter is missing, the script will print itself.
-t/--timeout | int | 5 | Timeout before the program starts typing in seconds.
-m/--mintime | int | 50 | Minimal time between keystrokes in seconds/1000.
-M/--maxtime | int | 150 | Maximal time between keystrokes in seconds/1000.
-r/--raw | optional | False | If this flag is set, the script will type the text out in raw form, instead of trying to fight editor autocomplete on newline.
-l/--license | optional | False | If this flag is set, the program will print out the licenses and libs used and then exit.

## Credit:
Credit goes to moses-palmer. Their Library https://github.com/moses-palmer/pynput is used in this project.
