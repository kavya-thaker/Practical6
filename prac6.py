#20CE146-Kavya Thaker
#Practical 6
'''AIM: You are given n words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
See the sample input/output for clarification. '''
'''Sample Input 
4 
bcdef 
abcdefg 
bcde 
bcdef'''
'''Sample Output 
3 
2 1 1 '''
'''Explanation: There are 3 distinct words. Here, "bcdef" appears twice in the input at the first and last positions. 
The other words appear once each. 
The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.'''

import collections;

n = int(input())   #input of words
d = collections.OrderedDict()
'''An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted. 
It preserves the order in which the keys are inserted.'''
for i in range(n):
    word = input()
    if word in d:
        d[word] +=1   #if the word occurs more than once then the number of that word would get incremented
    else:
        d[word] = 1   #if the word occurs only once then the output will be 1

print(len(d));

for k,v in d.items():     #k = keys , v = values
    print(v,end = " ");