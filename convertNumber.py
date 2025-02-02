units = {"ten":10 ,"zero":0, "one":1 , "two":2 , "three":3 , "four":4 , "five":5 , "six":6 , "seven":7 , "eight":8 , "nine":9 ,
          "eleven":11 , "twelve":12 , "thirteen":13 , "fourteen":14 , "fifteen":15 , "sixteen":16 , "seventeen":17 , "eighteen":18 , "nineteen":19 , "twenty":20 ,
            "thirty":30 , 
         "forty":40 , "fifty":50 , "sixty":60 , "seventy":70 , "eighty":80 , "ninety":90}
preMultiply = {"hundred":100 , "thousand":1000 ,"lakh":100000, "million":1000000, "crore":10000000 , "billion":1000000000}





string = input("Enter a number:  \n")
string = string.strip()
words = string.split()
numWords = len(words)
number = 0
index = 0

for word in words:
    word = word.lower()
    if word in units.keys():
        if(index+1 < numWords):
            if words[index+1].lower() not in preMultiply.keys():
                number += units[word] 
        else :
            number += units[word] 
                
        







    if word in preMultiply.keys():
        number += units[words[index-1].lower()]*preMultiply[word]
    index += 1
print(number)