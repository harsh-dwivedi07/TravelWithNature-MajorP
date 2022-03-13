from textblob import TextBlob

def sentiment_analysis(text):
    edu = TextBlob(text)
    polar = edu.sentiment.polarity

    if polar<0:
        return('Negative')
    elif polar==0:
        return('Neutral')
    else:
        return('Positive')


