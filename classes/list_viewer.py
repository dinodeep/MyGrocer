'''
list_viewer.py implements a list viewer class for interacting with list elements 1 at a time
'''

import os


def clear():
    ''' clears the terminal screen '''
    os.system("clear")


class ListViewer:

    border = "=" * 50

    def __init__(self, l, name):
        self.list = l
        self.len = len(l)
        self.name = name
        self.idx = 0

        if len(l) == 0:
            print("Length of list must be greater than 0")
            raise RuntimeError

    def view(self):
        ''' prints the current list element '''

        clear()

        # print the headline
        print(self.border)
        print(f"VIEWING {self.name} {self.idx + 1}/{self.len}")
        print(self.border)

        # print the element content
        print(self.list[self.idx])
        print(self.border)

    def update(self):
        ''' 
            updates the ListViewer based on user input 
            returns True, on continuing viewer, False to quit viewer
        '''

        # print and ask for input option
        print("q = quit")
        print("f = forward")
        print("b = backward")
        print(self.border)
        s = input("Enter: ")

        if s == "q":
            return False
        elif s == "f":
            self.idx += 1
        elif s == "b":
            self.idx -= 1

        # clamp index to list range
        self.idx = max(min(self.idx, self.len - 1), 0)

        return True

    def interact(self):
        ''' interact with the list one element at a time '''

        u = True

        while u:
            self.view()
            u = self.update()
