'''
This Was Authored by:
    - Nir Tuttnauer
    - Tomer Mizrahi
'''

import random

class SkipNode:
    """
    Represents a node in a Skip List.

    Attributes:
        value: The value stored in the node.
        forward: A list of references to the next nodes in each level of the Skip List.
    """

    def __init__(self, value=None, level=0):
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    """
    SkipList is a data structure that allows for efficient searching, insertion, and removal operations.
    It is a probabilistic data structure that uses multiple layers of linked lists to achieve fast search times.
    """

    def __init__(self, max_level, PRINT=False):
        """
        Initializes a SkipList object.

        Parameters:
        - max_level (int): The maximum level of the SkipList.
        - PRINT (bool): Optional. If True, enables printing of debug information during operations.
        """
        self.max_level = max_level
        self.head = SkipNode()
        self.level = 0
        self.len = 0
        self.PRINT = PRINT
    
    def __len__(self) -> int:
        return self.len

    def random_level(self) -> int:
            """
            Generates a random level for a node in the skip list.

            Returns:
                int: The randomly generated level.
            """
            level = 0
            while random.random() < 0.5 and level < self.max_level:
                level += 1
            return level

    def insert(self, value) -> None:
        """
        Inserts a new node with the given value into the SkipList.

        Args:
            value: The value to be inserted.

        Returns:
            None

        Raises:
            None
        """

        # Create a new node with a random height
        new_node = SkipNode(value, self.random_level())

        # Update the max height of the SkipList if needed
        self.max_level = max(self.max_level, len(new_node.forward))

        # Ensure the head node's forward list has enough elements
        while len(self.head.forward) < len(new_node.forward):
            self.head.forward.append(None)

        # Find the update positions for the new node
        update = [None] * (self.max_level + 1)
        current = self.head

        for i in range(self.level, -1, -1):
            if self.PRINT: print(f"Checking level {i}")
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
            if self.PRINT: print(f"Level {i}: {current.value}")

        # Check if the value already exists in the SkipList
        current = current.forward[0]
        if current is None or current.value != value:
            # Insert the new node
            for i in range(len(new_node.forward)):
                if i > self.level:
                    if self.PRINT: print(f"Skipping level {i}")
                    break
                if i < len(update):
                    new_node.forward[i] = update[i].forward[i]
                    update[i].forward[i] = new_node
                    if self.PRINT: print(f"Updated forward pointer at level {i}")
            if len(new_node.forward) > self.level:
                self.level = len(new_node.forward) - 1
                if self.PRINT: print(f"Updated level: {self.level}")
            # Increment the length of the SkipList
            self.len += 1

    def search(self, value) -> bool:
        """
        Searches for a given value in the skip list.

        Args:
            value: The value to search for.

        Returns:
            True if the value is found in the skip list, False otherwise.
        """
        current = self.head

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]

        current = current.forward[0]

        if current is not None and current.value == value:
            return True
        return False

    def remove(self, value) -> None:
        """
        Removes the first occurrence of the specified value from the SkipList.

        Args:
            value: The value to be removed from the SkipList.

        Returns:
            None

        Raises:
            None
        """
        update = [None] * (self.max_level + 1)
        current = self.head

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current and current.value == value:
            for i in range(len(current.forward)):
                if update[i].forward[i] == current:
                    update[i].forward[i] = current.forward[i]
            self.level = self.calculate_new_level(update)
        # Decrement the length of the SkipList
        self.len -= 1
    
    def print_list(self) -> None:
            """
            Prints the values of the skip list in each level.

            The values are printed in each level of the skip list, starting from the highest level
            and going down to the lowest level. Each level is printed on a separate line, with the
            level number followed by a colon. The values in each level are separated by a space.

            Example output:
            Level 3: value1 value2 value3
            Level 2: value4 value5
            Level 1: value6 value7 value8 value9
            Level 0: value10 value11

            """
            for level in range(self.level, -1, -1):
                print(f"Level {level}: ", end="")
                current = self.head
                while current.forward[level]:
                    value = current.forward[level].value
                    print(value.split("@")[0], end=" ")
                    current = current.forward[level]
                print()
