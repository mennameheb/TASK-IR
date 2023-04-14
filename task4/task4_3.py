import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize,sent_tokenize

# Reading
with open("activity_botscore.csv", 'r') as h:
    text = h.read()

# word_tokenization
tokenization = word_tokenize(text)
print(tokenization)
#sent_tokenization
tokenization2=sent_tokenize(text)
print(tokenization2)

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokenization if token.lower() not in stop_words]
print(filtered_tokens)

# Stemmming
stemmed_tokens = [PorterStemmer().stem(token) for token in filtered_tokens]
print(stemmed_tokens)
