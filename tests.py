'''
This Was Authored by:
    - Nir Tuttnauer
    - Tomer Mizrahi
'''

import random
from mymodules.spamfilter import SpamFilterA, SpamFilterB, SpamFilterC


def test_spam_filter(num = 3, PRINT=False):
    
    filter_systems = {
        1: SpamFilterA,
        2: SpamFilterB,
        3: SpamFilterC
    }
    
    filter_system = filter_systems.get(num, None)
    if filter_system is not None:
        filter_system = filter_system(PRINT=PRINT)
    
    # Generate 500,100 different email addresses
    email_addresses = set()
    while len(email_addresses) < 500100:
        email_addresses.add(str(random.randint(100000000, 999999999)) + "@example.com")

    # Populate the spam list with 100 addresses
    spam_addresses = random.sample(email_addresses, 100)
    for address in spam_addresses:
        filter_system.add_spam(address)
        email_addresses.remove(address)

    # Filter out 10 spam addresses and verify
    for _ in range(10):
        address = random.choice(spam_addresses)
        if not filter_system.is_spam(address):
            print(f"Error: {address} is not classified as spam.")
    
    # Test the system against the remaining 500,000 addresses
    false_positives = 0
    for address in email_addresses:
        if filter_system.is_spam(address):
            false_positives += 1
    if num==1:
        print("---------------------Results---------------------")
        print(f"Number of false positives: {false_positives}")
        print("-------------------------------------------------")
        print(f"Passed The Error Limit With Minimal Space? {false_positives//(len(email_addresses)+1) < 0.001}")
        print("-------------------------------------------------")
    if PRINT: 
        filter_system.bloom_filter.print_bit_array()
        print("-------------------------------------------------")
    if num == 2 and PRINT:
        filter_system.skip_list.print_list()
        print("-------------------------------------------------")
        print(len(filter_system.skip_list))
    

def test_all_filters(PRINT=False):
    test_spam_filter(1, PRINT=PRINT)
    test_spam_filter(2, PRINT=PRINT)
    test_spam_filter(3, PRINT=PRINT)
    print("")
    print("---------------------THANK-U-<3---------------------")
    print("")
    
def TestMain():
    test_all_filters(PRINT=True)
    
if __name__ == "__main__":
    TestMain()