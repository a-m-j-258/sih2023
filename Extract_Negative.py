# Filter rows with negative sentiment
negative_reviews = df[df['Sentiment'] == 'Negative']

# Extract the transcribed text from negative reviews
sentences = negative_reviews['Transcribed Text'].tolist()

# Print the extracted negative sentences
for sentence in sentences:
    print(sentence)
