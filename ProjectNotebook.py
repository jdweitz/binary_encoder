#!/usr/bin/env python
# coding: utf-8

# # Project Description

# 
# My project is a binary encoder and decoder. I developed a formula in which every letter of the alphabet can be represented as a set of five digits of 1s and 0s (the math behind only needing five digits is based on the possible combinations of these two numbers for 26 letters). I implement this formula with the use of the encrypt and encode methods. 
# 
# The input for encode must be a string of letters, which can be lowercase or capitalized. The application for this is for phrases and letters to be encoded into a form of binary. The purpose of the encrypt method is to convert the given letter into its capitalized form, if needed, and then turn that letter into its respective numerical value. Because the alphabet is 26 letters long, the range of these numerical values is (0,25). 
# *Note: The encrypt method can be called on an integer, but this integer must be within the range given above for accuracy.
# 
# The input for decode is a string of length 5 with a combination of 1s and 0s, and is applicable with the returned value of encode(letter). A string of capitalized letters will be returned.
# *Note: You can guess a random combination of 5 1s and 0s but that will not always produce a string of letters in return, which is why it is recommended to follow what is explained above for accuracy.

# ## Project Code
# 
# If it makes sense for your project, you can have code and outputs here in the notebook as well.

# In[1]:


from my_module.functions import(encrypt, encode, decode)


# In[2]:


print("The encoding of 'abc' is " + encode('abc'))
print("The decoding of '000000000100010' is " + decode('000000000100010'))


# #### Extra Credit (*optional*)
# 
# 1. I have had no Python experience prior to this course. I have used Java in a high school class.
# 2. My project challenged me to interpret a relationship between letters and binary numbers. This prompted me to translate this relationship into Python expressions, which required a good bit of logic.
