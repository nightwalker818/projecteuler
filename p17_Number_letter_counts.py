# Project Euler --> https://projecteuler.net/problem=17
# Problem 17 : Number letter counts
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# to install inflect (pip install inflect) we will be using the method number_to_words() to convert numbers to words.
# isalpha() This method returns true if all the characters in the string are alphabetic and there is at least one character, false otherwise.

import inflect
p = inflect.engine()
answer = 0
for i in range(1,1001):
  word = p.number_to_words(i)
  for w in word:
  	if w.isalpha():
          answer+=1
print(answer)
