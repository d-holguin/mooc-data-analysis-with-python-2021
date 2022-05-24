#!/usr/bin/env python3

import math


def main():

    shape_list_strs = ["triangle", "rectangle", "circle"]
    while(True):
        user_shape_input = input(
            "Choose a shape (triangle, rectangle, circle):")
        if user_shape_input == "":
            break
        if user_shape_input not in shape_list_strs:
            print("Unknown shape!")
            continue
        if user_shape_input == "rectangle":
            user_width_input = input(
                "Give width of the rectangle:")
            user_height_input = input(
                "Give height of the rectangle:")
            print(
                f"The area is {int(user_width_input) * int(user_height_input)}")
        if user_shape_input == "triangle":
            user_base_input = input(
                "Give base of the triangle:")
            user_height_input = input(
                "Give height of the triangle:")
            print(
                f"The area is {int(user_base_input) * int(user_height_input) / 2.00}")
        if user_shape_input == "circle":
            user_radius_input = float(input(
                "Give base of the triangle:"))
            print(
                f"The area is {math.pi * user_radius_input * user_radius_input}")


if __name__ == "__main__":
    main()
