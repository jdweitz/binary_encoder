"""A collection of functions for doing my project."""

def encrypt(val):
    """Converts an integer into a string of binary.
    
    Parameters
    ----------
    val: integer
        An integer that is in the range of 0 to 25; 
        the alphabet is 26 letters long.
        
    Returns
    -------
    encrypted: string
        A string of length five of binary that 
        represents the integer inputted.
    """
    encrypted = ''
    
    # Will loop through this 5 times.
    for n in range(0, 5):
        
        remainder = val % 2
        
        val = val // 2
        
        # Converts the remainder into a string and 
        # adds it to the front of 'encrypted'.
        encrypted = str(remainder) + encrypted 

    return encrypted


def encode(string_of_letters):
    """Converts a string of letters into a form of binary.

    Parameters
    ----------
    string_of_letters: string
        A string that is composed of any combination 
        of letters and no spaces.

    Returns
    -------
    encrypted_word: string
        A string of binary that represents each letter in 
        the form of a combination of five '1s' and '0s'.
    """
    encrypted_word = ''

    #Capitalizes all letters in the string.
    capitalized_letters = string_of_letters.upper() 

    for letter in capitalized_letters:
        
        #Converts the value into a range of 0 to 25, 
        #depending on the letter.
        num = ord(letter) - 65 

        #Calls the 'encrypt' method on the new number created.
        encoded_num = encrypt(num)

        encrypted_word += encoded_num

    return encrypted_word


def decode(group):
    """Converts a string of binary into a string of capitalized letters

    Parameters
    ----------
    group: string
        A string of binary that is a multiple of 5.

    Returns
    -------
    decoded_message: string
        A string of capitalized letters that 
        represent a group of 5 '0s' and '1s'.
    """
    decoded_message = ''

    # Loops through each grouping of five digits
    for block in range(0, len(group) // 5):

        number = 0

        #Loops though each index within the five-digit grouping
        for location_val in range(0, 5):

            index = block * 5 + location_val 

            number += 2 ** (4 - location_val) * int(group[index])

        #65 is added to the number to return it to the alphabet range
        character = chr(number + 65)

        decoded_message = decoded_message + character

    return decoded_message