"""Test for my functions."""

from functions import encrypt, encode, decode

def test_encrypt():
    
    assert(callable(encrypt))
    assert(encrypt(0) == '00000')
    assert(encrypt(25) == '11001')
    assert(len(encrypt(12)) == 5)
    
def test_encode():
    
    assert(callable(encode))
    assert(encode('a') == encode('A') == '00000')
    assert(len(encode('abc')) == 15)
    assert(encode('z') == '11001')
    
def test_decode():
    
    assert(callable(decode))
    assert(decode('00000') == 'A')
    assert(decode('1011100001') == 'XB')
    assert(len(decode('00001')) == 1)