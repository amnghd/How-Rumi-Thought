import nltk
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

def is_float(string):
  try:
    return float(string) and '.' in string  # True if string is a number contains a dot
  except ValueError:  # String is not a number
    return False

with open('persian.txt', 'r', encoding="utf8") as myfile:
    sw = myfile.read().replace('\n', ' ').replace("\u200c","").replace("\ufeff","").replace("."," ").split(' ')# a list of stop words


with open('shams.txt', 'r', encoding="utf8") as myfile:
    line = myfile.read().replace('\n', ' ').replace(",","").replace(":","").replace("ۀ","ه").replace("-","").replace("،","")
    masnavi = re.split('[\t\s:]+', line)   # a list of stop words

masnavi_nn = [x for x in masnavi if (not is_float(x) or not x.isdigit())] # no number

set_masnavi = set(masnavi_nn)
set_stop_word = set(sw)
actual_words = set_masnavi.difference(set_stop_word)

masnavi_nsw = [x for x in masnavi_nn if x in actual_words] # no stop word


st_in_masnavi= [x for x in masnavi_nsw if x in sw]
print(len(masnavi_nsw))
print(len(masnavi_nn))

# Creating the word frequency distribution
freqdist = nltk.FreqDist(masnavi_nsw)

# Plotting the word frequency distribution
a = freqdist.tabulate(45)

