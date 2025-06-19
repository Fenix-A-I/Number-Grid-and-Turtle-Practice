"""
Author: Alexandr Iapara
Description: Defines a function draw_grid() that accepts a single integer and prints a square grid of numbers from 1 to the given integer for both rows and columns.
"""

def draw_grid(integer):
    """
    Prints a square grid of numbers from 1 to the given integer.

    The function uses nested for loops. The outer loop iterates over each row,
    printing a newline before each row. The inner loop prints numbers from 1 up to
    the given integer, separated by spaces, on the same line.

    Args:
        integer (int): The size of the grid (number of rows and columns).

    Returns:
        None
    """
    for i in range(integer):
        print(end="\n")
        for j in range(integer):
            print(str(j+1) + ' ', end='')
    print("\n")

def main():
    while True:
        try:
            input_value = int(input("\nEnter a number for the grid size (positive integer): "))
            if input_value <= 0:
                print("\033[91mPlease enter a positive integer.\033[0m")
                continue
            break

        except ValueError:
            print("\033[91mInvalid input. Please enter a valid positive integer.\033[0m")
        except KeyboardInterrupt:
            print("\n\033[93mProgram terminated by user.\033[0m\n")
            return
        except Exception as e:
            print(f"\033[91mAn unexpected error occurred: {e}\033[0m\n")
            return
        
    draw_grid(input_value)

if __name__ == "__main__":
    main()