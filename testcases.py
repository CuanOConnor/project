# Test cases for the regex.py file
# Cuan O'Conchuir

import regex

'''
Testing potential expression strings.
Tests assert whether the expression matches the string.
Uses assert inside a try/except block to print an error on fail but not cause a fatal error
'''
print("************ Test Cases ************")
print("-----Cases to be tested-----")
print("a.b|b* -compared to- bbbbbb")
print("a.b|b* -compared to- bbbbbbx")
print("a.b -compared to- ab")
print("a.b -compared to- xx")
print("----------------------------")
try:
    assert regex.match("a.b|b*", "bbbbbb"), "a.b|b* should match bbbbbb"
    print("a.b|b* should match bbbbbb")
except AssertionError as e:
    print(e)

try:
    assert regex.match("a.b|b*", "bbbbbbx"), "a.b|b* should not match bbbbbbx"
except AssertionError as e:
    print(e)

try:
    assert regex.match("a.b", "ab"), "a.b should match ab"
    print("a.b should match ab")
except AssertionError as e:
    print(e)

try:
    assert regex.match("a.b", "xx"), "a.b should not match xx"
except AssertionError as e:
    print(e)

print("************************************")
