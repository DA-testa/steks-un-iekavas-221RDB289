# python3
# Autors: Gundars Pelle 6. grupa

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            # Process closing bracket, write your code here
            if are_matching(opening_brackets_stack[-1][0], next):
                opening_brackets_stack.pop()
            else:
                return i + 1


def main():
    text = input()
    if text.startswith('I'):
        text = input()
    elif text.startswith('F'):
        f = open(input(), 'r')
        text = f.read()
        f.close()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch:
        print(mismatch)
    else:
        print('Success')


if __name__ == "__main__":
    main()
