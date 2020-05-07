import requests
import operator 
import re
import argparse
from bs4 import BeautifulSoup
from collections import Counter 

print("___________.__.__          _________                                       \n\_   _____/|__|  |   _____ \_   ___ \  ____   _____   _____   ____   ____  \n |    __)  |  |  |  /     \/    \  \/ /  _ \ /     \ /     \ /  _ \ /    \ \n |     \   |  |  |_|  Y Y  \     \___(  <_> )  Y Y  \  Y Y  (  <_> )   |  \ \n \___  /   |__|____/__|_|  /\______  /\____/|__|_|  /__|_|  /\____/|___|  /\n     \/                  \/        \/             \/      \/            \/ ")

parser = argparse.ArgumentParser(description='Get 10 most common words from a film script from "imsdb.com"!')
parser.add_argument('-u', action='store', dest='u', metavar='<url>', type=str, help='URL of Script from "imsdb.com"')
parser.add_argument('-b', action='store_true', help='Remove the names of characters above their spoken lines.')
parser.add_argument('-p', action='store_true', help='Remove "pointless" words from being counted. For example: "the", "a", "this"...')
args = parser.parse_args()
 
word_count = {} 
clean_list = []
wordlist = []
pointless_words = ['the', 'a', 'this', 'to', 'you', 'is', 'of', 'in', 'and', 'it', 'what', 'i', 'for', 'that', 'how', 'are', 'your', 'on', 'with', 'but', 'these', 'was', 'from', 'just', 'when']
url = args.u

request = requests.get(url)
response = BeautifulSoup(request.text, 'html.parser')
codetags = response.find_all('b')

if args.b == True:
    for codetag in codetags:
        codetag.extract()

def clean_wordlist(wordlist):
    global clean_list
    symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
    for word in wordlist:
        for i in range (0, len(symbols)): 
            word = word.replace(symbols[i], '')               
        if len(word) > 0: 
            clean_list.append(word) 

for each_text in response.findAll('pre'):
    content = each_text.text
    words = content.lower().split()
    for each_word in words: 
        wordlist.append(each_word)
    clean_wordlist(wordlist)
  
for word in clean_list: 
    if word in word_count: 
        word_count[word] += 1
    else: 
        word_count[word] = 1

c = Counter(word_count)

if args.p == True:
    for element in pointless_words:
        del c[element]

common_words = c.most_common(10)
iteration = 1

for key, value in common_words:
    print(str(iteration) + ") " + key + " - " + str(value))
    iteration += 1