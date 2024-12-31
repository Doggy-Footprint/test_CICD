# string_utils.py

import re

def find_pattern(text, pattern):
    """
    Finds all occurrences of a pattern in the given text.
    
    Args:
        text (str): The input string to search in.
        pattern (str): The regex pattern to search for.
    
    Returns:
        list: A list of all matches, or an empty list if no matches are found.
    """
    return re.findall(pattern, text)