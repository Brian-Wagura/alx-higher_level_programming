#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text(str): The text to be processed

    Raises:
        TypeError: if text is not a string

    Returns: None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        print(char, end='')
        if char in ['.',',','?',':']:
            print('\n\n', end='')
