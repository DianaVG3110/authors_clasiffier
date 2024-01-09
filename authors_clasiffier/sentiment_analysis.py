"""Código para interpretar el sentimiento de una canción"""
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob


def english_analysis(text_file: str):
    """
    text_file (str) : path to the text file to be analyzed
    """

    # Downloading the needed data from NLTK
    nltk.download("punkt", quiet=True)
    nltk.download("stopwords", quiet=True)
    nltk.download("vader_lexicon", quiet=True)

    with open(text_file, "r", encoding="utf-8") as file:
        text = file.read()

    # Tokenización
    words = word_tokenize(text.lower())  # Convierte a minúsculas

    # Eliminación de signos de puntuación y palabras irrelevantes
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word.isalnum() and word not in stop_words]

    # Crear una instancia del analizador de intensidad de sentimiento de NLTK
    sia = SentimentIntensityAnalyzer()

    # Obtener la polaridad del sentimiento
    sentiment_score = sia.polarity_scores(text)

    # Imprimir el resultado
    print("Sentiment Score:", sentiment_score)

    # Interpretar el sentimiento
    if sentiment_score["compound"] >= 0.05:
        print("La canción tiene un sentimiento positivo.")
    elif sentiment_score["compound"] <= -0.05:
        print("La canción tiene un sentimiento negativo.")
    else:
        print("La canción tiene un sentimiento neutro.")


def spanish_analysis(text_file: str):
    """
    text_file (str) : path to the text to be analyzed

    This function uses TextBlob for the analysis
    Then, the output is a score of polarity between -1 and 1
    meaning that if the output is near -1 is a negative take that
    the text is taking in the other hand if is near 1
    the text is possitive, a score near 0 should be interpreted
    as a neutral text.
    """
    with open(text_file, "r", encoding="utf-8") as file:
        text = file.read()

    sentiment = TextBlob(text).sentiment.polarity
    
    if sentiment > 0:
        print("El sentimiento del texto dado es postivo")
    elif sentiment < 0:
        print("El sentimiento del texto dado es negativo")
    else:
        print("El sentimiento del texto dado es neutro")

def analysis(text, language):
    """
    This function analyzes the text parsed with the name `text`
    the language argument can be 'spanish' or 'english'
    """
    if language == "spanish":
        spanish_analysis(text)
    elif language == "english":
        english_analysis(text)
    else: 
        print("This argument is not supported")


if __name__ == "__main__":
    analysis("./data/Adele.txt",language="english")
    analysis("./data/Adele.txt",language="spanish")
