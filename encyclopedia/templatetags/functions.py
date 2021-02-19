"""Useful python functions"""

from django import template

#Registers the template tag
register = template.Library()

#Determines if string1 is a substring of string2
# Pre {len(string1) <= len(string2)
def isSubstring(string1, string2):
    return string1 == string2[0:len(string1)]

#Registers the filter
register.filter('isSubstring', isSubstring)
