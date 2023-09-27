import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation

nltk.download("stopwords")
nltk.download("punkt")

stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = "".join([char for char in text if char not in punctuation])  # Remove punctuation
    words = word_tokenize(text)  # Tokenize the text
    words = [word for word in words if word not in stop_words]  # Remove stopwords
    return " ".join(words)

df["Processed Text"] = df["Transcribed Text"].apply(preprocess_text)



from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity  # Return the polarity score

df["Sentiment Score"] = df["Processed Text"].apply(analyze_sentiment)

