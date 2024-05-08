'''
This Was Authored by:
    - Nir Tuttnauer
    - Tomer Mizrahi
    
Project: Spam Filter System
    - This Project is part of the Advanced Data Structures course.

Description:
    This script/module includes implementation of various advanced data structures: 
    - Bloom Filter is a probabilistic data structure that is used to test whether an element is a member of a set.
    - Skip List is a data structure that allows fast search within an ordered sequence of elements.
    Spam Filter is a system that uses Bloom Filter and Skip List to classify email addresses as spam or not spam.

To Run the Script:
    python main.py

To Run the Script with Debug Information:
    python tests.py
'''

from tests import test_all_filters
import warnings

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    test_all_filters(PRINT=False) # Set PRINT=True to see the internal workings of the filters (USE WITH CAUTION!!!)
