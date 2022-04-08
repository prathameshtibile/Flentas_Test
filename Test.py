# Author :- Prathamesh Bajirao Tibile
# Date :- 08-04-2022
# Problem Statement :- Sherlock Holmes is working on a case. One day going through evidence, 
# he finds some scribbled text at  corner of victim's diary. Now Sherlock believes that the scribbled text has something to do with the clue  leading to Murderer, so he decides to find every occurrence of all the permutations of the scribbled text in  the entire book. Since this is a huge task, he needs your help, he needs you to figure out if any permutation of  the scribbled text exists in the given text string, so he can save time with the case. Permutation means any  sequence of the string. 

#Input Format ==> First line contains number of test cases T. Each test case contains two lines, first line contains pattern and  next line contains a text string. All characters in both the strings are in lowercase only [a-z]. 

#Constraints 
#        1≤T≤100 
#        1 ≤ |Pattern| ≤ 1000 
#        1 ≤ |Text String| ≤ 100000 


# Solution ==>

t = int(input("enter the test cases number : "))

for _ in range(t):
    p=input().strip()
    s=input().strip()
    if(p in s):
        print('YES')
    elif(p[::-1] in s):
        print('YES')
    else:
        print('NO')