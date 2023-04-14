import pandas as pd
from  nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
ps = PorterStemmer()
sb = SnowballStemmer('english')
user_choice = int(input('please, enter your choice :'))
if user_choice == 4:
    var = int(input('choose Snowball or Porter?:'))
if var == 1:
    print(ps.stem('programming'))
elif var == 2:
    print(sb.stem('programming'))    

