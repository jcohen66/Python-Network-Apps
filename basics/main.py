# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Prfess Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_xmas_tree():
    for leaf in [*range(10)] + [2]:
        print(f'{"X" * (leaf * 2 + 1):^30}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_xmas_tree()

