#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Nov. 10, 2022
# a program that calculates the factorial


def main():
    # variables
    user_num_string = input("Enter any whole number: ")

    # checks if user num is an integer
    try:
        user_num_int = int(user_num_string)

    # if user number is not an integer
    except Exception:
        print("Input invalid! Please enter a WHOLE number!")

    # user imputed an integer
    else:
        # checks if user num is a whole number
        if user_num_int < 0:
            print("Input invalid! Please enter a WHOLE number!")

        # user num is valid
        else:
            counter = 1
            number_factorial = 1
            # calculates the factorial of the user number
            while True:
                number_factorial *= counter
                counter += 1
                # breaks out of the loop
                if counter > user_num_int:
                    break

            # displays final result to user
            print(f"{user_num_int}! = {number_factorial}")


if __name__ == "__main__":
    main()
