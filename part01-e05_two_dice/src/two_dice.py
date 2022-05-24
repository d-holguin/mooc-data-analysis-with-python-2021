#!/usr/bin/env python3

def main():
    for dice_one in range(1, 7):
        for dice_two in range(1, 7):
            if(dice_one + dice_two == 5):
            	print(f"{dice_one, dice_two}")


if __name__ == "__main__":
    main()
