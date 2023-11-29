import nltk
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('wordnet')

stop_words_en = stopwords.words("english")

# Inisialisasi WordNetLemmatizer
stemmer = PorterStemmer()
# Function for text preprocessing
def text_preprocessing(text):
    # Case folding
    text = text.lower()

    # Mention, hashtag, newline, URL, and non-letter removal
    text = re.sub("@[A-Za-z0-9_]+", " ", text)
    text = re.sub("#[A-Za-z0-9_]+", " ", text)
    text = re.sub(r"\\n", " ", text)
    text = re.sub(r"http\S+|www.\S+", " ", text)
    text = re.sub("[^A-Za-z\s']", " ", text)

    # Tokenization
    tokens = word_tokenize(text)

    # Stopwords removal
    tokens = [word for word in tokens if word not in stop_words_en]

    # Stemming
    tokens = [stemmer.stem(word) for word in tokens]

    # Combining Tokens
    text = ' '.join(tokens)

    return text