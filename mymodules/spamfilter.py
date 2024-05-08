'''
This Was Authored by:
    - Nir Tuttnauer
    - Tomer Mizrahi
'''

from mymodules.bloomfilter import BloomFilter
from mymodules.skiplist import SkipList

class SpamFilter:
    def __init__(self):
        pass

    def add_spam(self, spam):
        raise NotImplementedError("Subclasses must implement this method")

    def is_spam(self, message):
        raise NotImplementedError("Subclasses must implement this method")
   
class SpamFilterA(SpamFilter):
    """
    A class representing a spam filter.

    Attributes:
        bloom_filter_size (int): The size of the bloom filter.
        bloom_filter_hashes (int): The number of hash functions to use in the bloom filter.
        PRINT (bool): A flag indicating whether to print debug information.
        spam_addresses (set): A set of spam addresses.
        max_spam_addresses (int): The maximum number of spam addresses to store.
        bloom_filter (BloomFilter): An instance of the BloomFilter class.

    Methods:
        __init__(self, bloom_filter_size=1438, bloom_filter_hashes=10, PRINT=False): Initializes the SpamFilterA object.
        add_spam(self, address): Adds a spam address to the filter.
        is_spam(self, address): Checks if an address is spam.

    """

    def __init__(self, bloom_filter_size=1438, bloom_filter_hashes=10, PRINT=False):
        super().__init__()
        self.bloom_filter = BloomFilter(bloom_filter_size, bloom_filter_hashes, PRINT=PRINT)
        self.spam_addresses = set()
        self.max_spam_addresses = 100
        print("")
        print("-----------------------TEST-----------------------")
        print("SpamFilterA: Bloomfilter")
        print("")
        
    def add_spam(self, address):
        """
        Adds a spam address to the filter.

        Args:
            address (str): The spam address to add.

        Returns:
            None

        """
        if len(self.spam_addresses) < self.max_spam_addresses:
            self.spam_addresses.add(address)
            self.bloom_filter.add(address)
        else:
            print("Spam list is full, can't add new address.")

    def is_spam(self, address):
        """
        Checks if an address is spam.

        Args:
            address (str): The address to check.

        Returns:
            bool: True if the address is spam, False otherwise.

        """
        return address in self.spam_addresses or self.bloom_filter.contains(address)

class SpamFilterB(SpamFilter):
    """
    A spam filter that uses a Bloom filter and a skip list to efficiently detect spam addresses.

    Args:
        bloom_filter_size (int): The size of the Bloom filter.
        bloom_filter_hashes (int): The number of hash functions to use in the Bloom filter.
        PRINT (bool): Whether to print debug information.

    Attributes:
        bloom_filter (BloomFilter): The Bloom filter used to store spam addresses.
        skip_list (SkipList): The skip list used to store spam addresses.
        max_spam_addresses (int): The maximum number of spam addresses that can be stored.
        spam_addresses (set): The set of spam addresses that have been added.
        PRINT (bool): Whether to print debug information.

    Methods:
        add_spam(address): Adds a spam address to the filter.
        is_spam(address): Checks if an address is spam.

    """

    def __init__(self, bloom_filter_size=1438, bloom_filter_hashes=10, PRINT=False):
        super().__init__()
        self.bloom_filter = BloomFilter(bloom_filter_size, bloom_filter_hashes, PRINT=PRINT)
        self.skip_list = SkipList(max_level=16, PRINT=PRINT)
        self.max_spam_addresses = 100
        self.spam_addresses = set()
        self.PRINT = PRINT
        print("")
        print("-----------------------TEST-----------------------")
        print("SpamFilterB: Bloomfilter and then skiplist")
        print("")

    def add_spam(self, address):
        """
        Adds a spam address to the filter.

        If the number of spam addresses is less than the maximum allowed, the address is added to both the skip list and the Bloom filter.
        If the number of spam addresses has reached the maximum, the address is not added and a message is printed if PRINT is True.

        Args:
            address (str): The spam address to add.

        """
        if len(self.spam_addresses) < self.max_spam_addresses:
            self.skip_list.insert(address)
            self.bloom_filter.add(address)
        else:
            if self.PRINT: print("Spam list is full, can't add new address.")

    def is_spam(self, address):
        """
        Checks if an address is spam.

        First, the Bloom filter is checked to see if the address is likely to be spam.
        If the address is likely to be spam, the skip list is searched to confirm if it is indeed spam.

        Args:
            address (str): The address to check.

        Returns:
            bool: True if the address is spam, False otherwise.

        """
        if self.bloom_filter.contains(address):
            return self.skip_list.search(address)
        return False
    
class SpamFilterC(SpamFilter):
    """
    A class that represents a spam filter.

    Attributes:
        bloom_filter_size (int): The size of the bloom filter.
        bloom_filter_hashes (int): The number of hash functions to use in the bloom filter.
        PRINT (bool): A flag indicating whether to print debug information.
        spam_addresses (set): A set of spam addresses.
        max_spam_addresses (int): The maximum number of spam addresses to store.
        bloom_filter (BloomFilter): The bloom filter used for spam address detection.
    """

    def __init__(self, bloom_filter_size=1438, bloom_filter_hashes=10, PRINT=False):
        super().__init__()
        self.bloom_filter = BloomFilter(bloom_filter_size, bloom_filter_hashes, PRINT=PRINT)
        self.spam_addresses = set()
        self.max_spam_addresses = 100
        print("")
        print("-----------------------TEST-----------------------")
        print("SpamFilterC: Bloomfilter with deletion of old addresses")
        print("")

    def add_spam(self, address) -> None:
        """
        Adds a spam address to the filter.

        If the number of spam addresses exceeds the maximum limit, the oldest address is removed.

        Args:
            address (str): The spam address to add.
        """
        if len(self.spam_addresses) < self.max_spam_addresses:
            self.spam_addresses.add(address)
            self.bloom_filter.add(address)
        else:
            self.bloom_filter.remove(self.spam_addresses.pop(0))
            self.spam_addresses.add(address)
            self.bloom_filter.add(address)
            
    def is_spam(self, address) -> bool:
        """
        Checks if an address is classified as spam.

        Args:
            address (str): The address to check.

        Returns:
            bool: True if the address is classified as spam, False otherwise.
        """
        return address in self.spam_addresses or self.bloom_filter.contains(address)
    