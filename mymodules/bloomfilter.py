'''
This Was Authored by:
    - Nir Tuttnauer
    - Tomer Mizrahi
'''

import hashlib

class BloomFilter:
    """
    A probabilistic data structure for efficient membership testing.

    The BloomFilter class provides methods to add items, remove items, and check if an item is present in the filter.

    Args:
        size (int): The size of the bit array used by the filter.
        hash_count (int): The number of hash functions to use.
        PRINT (bool, optional): Whether to print debug information. Defaults to False.

    Attributes:
        size (int): The size of the bit array used by the filter.
        hash_count (int): The number of hash functions used.
        bit_array (list): The bit array representing the filter.
        PRINT (bool): Whether to print debug information.

    Methods:
        add(item): Adds an item to the filter.
        remove(item): Removes an item from the filter.
        contains(item): Checks if an item is present in the filter.
        print_bit_array(): Prints the bit array.

    """

    def __init__(self, size, hash_count, PRINT=False):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size
        self.PRINT = PRINT

    def add(self, item) -> None:
        """
        Adds an item to the Bloom filter.

        Args:
            item: The item to add to the filter.

        """
        if self.PRINT: print(f"Adding item: {item}")
        for seed in range(self.hash_count):
            hash_val = int(hashlib.sha256(str(item).encode() + str(seed).encode()).hexdigest(), 16) % self.size
            if self.PRINT: print(f"Calculated hash value {hash_val} for seed {seed}")
            self.bit_array[hash_val] = 1
            if self.PRINT: print(f"Set bit {hash_val} to 1")

    def remove(self, item) -> None:
        """
        Removes an item from the Bloom filter.

        Args:
            item: The item to remove from the filter.

        """
        if self.PRINT: print(f"Removing item: {item}")
        for seed in range(self.hash_count):
            hash_val = int(hashlib.sha256(str(item).encode() + str(seed).encode()).hexdigest(), 16) % self.size
            if self.PRINT: print(f"Calculated hash value {hash_val} for seed {seed}")
            self.bit_array[hash_val] = 0
            if self.PRINT: print(f"Set bit {hash_val} to 0")

    def contains(self, item) -> bool:
        """
        Checks if an item is present in the Bloom filter.

        Args:
            item: The item to check.

        Returns:
            bool: True if the item may be in the filter, False otherwise.

        """
        if self.PRINT: print(f"Checking if item {item} is in the Bloom Filter")
        for seed in range(self.hash_count):
            hash_val = int(hashlib.sha256(str(item).encode() + str(seed).encode()).hexdigest(), 16) % self.size
            if self.PRINT: print(f"Calculated hash value {hash_val} for seed {seed}")
            if self.bit_array[hash_val] == 0:
                if self.PRINT: print(f"Bit {hash_val} is 0, item is not in the Bloom Filter")
                return False
        if self.PRINT: print(f"All bits are set, item may be in the Bloom Filter")
        return True

    def print_bit_array(self) -> None:
        """
        Prints the bit array of the Bloom filter.

        """
        print(self.bit_array)