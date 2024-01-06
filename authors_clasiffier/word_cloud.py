"""Functions to create wordclouds from text files"""

import os
from wordcloud import WordCloud


def detect_language(file):
    """detect language as spanish or english, given a file"""
    lang = {"es": "spanish", "en": "english"}
    with open(file, encoding="utf8") as text_file:
        code = detect(text_file.read())
    return lang[code]


def gen_wordcloud(
    file: str, output: str, language="auto", mask=None, width=600, height=600, **kwargs
):
    """
    Generates wordcloud from file
    
    Parmeters:
    file (str): path to text file to be converted
    output (str): path and name of the output JPG file
    language (str): language to take care of stopwords, default to auto
    for autodetecting language, in other case user must put the name
    of language following the names that NLTK stopword function admits.
    mask (str): complete path to mask image
    """
    nltk.download("stopwords", quiet=True)
    if mask is not None:
        filedir = os.path.dirname(__file__)
        maskdir = os.path.join(filedir, mask)
        mask = np.array(Image.open(maskdir))
    if language == "auto":
        language = detect_language(file)
    forbidden_words = list(stopwords.words(language))
    with open(file, encoding="utf8") as text_file:
        text = text_file.read()
        wordcloud = WordCloud(
            width=width, height=height, stopwords=forbidden_words, mask=mask, **kwargs
        )
        wordcloud.generate(text)
        wordcloud.to_file(output)


def truncate_filename(filename: str) -> str:
    """
    function that returns a file name without extension

    Parameters:
    filename (str): name of the file with extension

    Returns:
    str: name of the file without the extension
    """
    return os.path.splitext(filename)[0]


def is_text_file(filename: str) -> bool:
    """
    Check if a file is a text file

    Parameters:
    filename (str): name of the file

    Returns:
    bool: True if the file is a text file
    """
    extension = os.path.splitext(filename)[1]
    return extension == ".txt"


def gen_wordcloud_directory(dirname: str, outputdir: str, **kwargs):
    """
    Iterates through files and generates their wordclouds

    Parameters:
    dirname (str): name of the directory where the text files are
    outputdir (str): path where the generated images needs to be placed
    """
    directory = os.path.dirname(__file__)
    path = os.path.join(directory, dirname)
    output_dir = os.path.join(directory, outputdir)
    for filename in os.listdir(path):
        file = os.path.join(path, filename)
        if is_text_file(file):
            gen_wordcloud(
                file,
                os.path.join(output_dir, truncate_filename(filename) + ".jpg"),
                **kwargs
            )


if __name__ == "__main__":
    gen_wordcloud_directory("../data", "../images", mask="../templates/heart.jpg")
