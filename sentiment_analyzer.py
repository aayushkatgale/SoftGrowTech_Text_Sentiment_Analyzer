from textblob import TextBlob

#text = input("Enter your text: ")

blob = TextBlob(text)

polarity = blob.sentiment.polarity

if polarity > 0:
    sentiment = "Positive"
elif polarity < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print("Sentiment:", sentiment)
