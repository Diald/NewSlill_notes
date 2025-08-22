#NUMPY 
import numpy as np 

a = np.array([1,2,3])
#print(a)

b = np.array([[1,2,3,4],[5,6,7,8]]) #2D array / matrix 
#print(b)

#arrays with zeroes or ones 
zeroes = np.zeros((2,3)) # array of size (2,3)
ones = np.ones((2,3)) #array of size(2,3) having only ones

#print(zeroes)
#print(ones)

#RANGE OF NUMBERS 
c = np.arange(0,10,2)
d = np.linspace(0,1, 5)


print(b.shape) #(2,4) which is 2 rows and 4 columns
print(b.ndim) # dimensions which is 2
print(b.size) #total number of elements which is 8 [2*4]
print(b.dtype) #the data type which is int32


#INDEXING AND SLICING 
print(b[0,1]) #the element at 0th row and 1st column or b[0][1]
print(b[:,1]) # the entire second column or 1st column 
print(b[1,:]) # the entire second row or 1st row 
print(b[0:2, 1:3]) # subarray from 0th


#MATHEMATICAL OPERATIONS 
x = np.array([1,2,3])
y = np.array([4,5,6])

print(x+y) #[5 7 9]
print(x-y) #[-3 -3 -3]
print(x*y) # [4 10 18]
print(x/y) # [0.25 0.4 0.5]

print(np.sqrt(x))
print(np.exp(x)) # e ki power x[i]


#MATRIX OPERATIONS - 

a = np.array([[1,2], [3,4]])
b = np.array([[2,0],[1,3]])

#matrix multiplication 
print(a@b) 
print(np.dot(a, b))

print(np.linalg.inv(a)) # inverse of A 
print(np.linalg.det(a)) # determinant of A 
print(np.linalg.eig(a)) # eigen values and eigen vectors


#AGGREGATIONS - Statistics 

arr = np.array([1,2,3,4,5])
print(arr.sum())
print(arr.mean())
print(arr.min())
print(arr.max())
print(arr.std())


# REGEX - regular expressions 
# this is used for pattern matching 

import re 

#basic regex functions

pattern = ""
text = ""
repl = ""
re.search(pattern, text) # finds the first match of the pattern in the given text
re.findall(pattern, text) # finds all the matches of that pattern in the text 
re.match(pattern, text) # matches only from the start of the string or text 
re.sub(pattern, repl, text) # replaces with repl when it finds that it matches with the pattern 
re.split(pattern, text)

# search looks for first element 
# findall looks for all the matches in the string 
# match looks for pattern from the beginning of text 
# sub is used to replace the string that matches the pattern 
# split is used to split sting by pattern

#BASIC PATTERNS IN REGEX 
# . -> any character, eg: a.d -> abcd
# \d -> any digit (0-9), eg: \d ->"5"
# \D -> non digit 
# \w -> word character, eg: \w:"A", "9", "_"
# \W -> non word characters, eg: \W -> "!"
# \s -> whitespaces 
# \S -> non whitespaces 

#QUANTIFIERS 

# * -> 0 or more, eg: go* -> "g", "go", "goo"
# + -> 1 or more, eg: go+ -> "go", "gooo"
# ? -> 0 or 1, eg: colou?r -> "color", "colour"
# {n} -> exactly n, eg: \d{4} ->"2024", "2025"
# {n,} -> n or more, eg: \d{2,} -> "23", "123"
# {n,m} -> between n and m, eg: a{2,4} -> "aa", "aaa", "aaaa"


# ANCHORS 

# ^ -> start of the string, eg: ^Hello matches "Hello world" but not "world Hello"
# $ -> end of string, eg: $world matches "Hello world"
# \b -> word boundary, eg: \bcat\b matches "cat" but not "scatter"

# character sets & groups 

# [abc] -> a, b or c
# [0-9] -> all digits from 0 to 9
# [A-Za-z] -> all words from capital A-Z to small a-z 
# [^abc] -> anything except for a, b or c
# (abc|xyz) -> matches with abc or xyz

import re 

text = "My phone number is 12345-67890 and my email is divya123@example.com"

#to find all digits in the text 
print(re.findall(r'\d+', text))

#to find phone number 
print(re.findall(r'\d{5}-\d{5}', text))

#to find email 
print(re.findall(r'[a-zA-Z0-9._]+@[a-z]+\.[a-z]+',text))

#to replace phone number with xxx 
print(re.sub(r'\d{5}-\d{5}', 'xxxxx-xxxxx', text))



# PANDAS 
# pandas is a lib built over numpy and is used for data cleaning 
# , analysis and manipulation 
# it mainly introduces two main data structures - 
# SERIES - one dimensional labelled array - like a single column table
# DATAFRAME - two dimensional labelled array - like two column table :ps essentially
# both of them are made using dictionaries

# data handling, data cleaning, data transformation, statistical operation 

import pandas as pd 

#SERIES 
s = pd.Series([10,20,30], index=['a','b','c'])
print(s)

#DATAFRAME 
data = {
    'name':['alice', 'bob', 'halsey'],
    'age':[23, 45,30], 
    'city':['mahattan', 'chicago', 'new york']
}
df = pd.DataFrame(data)
print(df)


# some common pandas operations - 

# READING AND WRITING DATA 
