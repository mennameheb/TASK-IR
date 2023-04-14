from nltk.tokenize import sent_tokenize, word_tokenize
text = "NLTK is a leading platform for building Python programs to work with human language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all, NLTK is a free, open source, community-driven project.."
number = int(input('Choice number '))
if number == 1 :
    #     y = text.split()
    #     print(y)
    print(word_tokenize(text))
elif number == 2 :
    #     y = text.split('.')
    #     print(y)
    print(sent_tokenize(text))
elif number == 3:
    print(text)
# Importing pandas package
import pandas as pd

# Reading a csv file
data = pd.read_csv("C:\Users\orngnal2021\OneDrive\Desktop\منة محمد محيلب\task2\emails.csv", nrows=5) # df = data.head()

# Creating a Dataframe with first 2 rows
df = pd.DataFrame(data)
# Display Dataframe
print("Created DataFrame with first 2 rows of csv file:\n",df)    



