"""Functions to create wordclouds from text files"""

import os
from wordcloud import WordCloud


def gen_wordcloud(file : str, output : str):
    """
    Generates wordcloud from file
    
    Parmeters:
    file (str): path to text file to be converted
    output (str): path to output JPG file
    """
    try:
        text = open(file, encoding="utf8").read()
    except UnicodeDecodeError:
        text = open(file, encoding="cp850").read()
    wordcloud = WordCloud(width=1280, height=720).generate(text)
    wordcloud.to_file(output)


def truncate_filename(filename : str) -> str:
    """
    function that returns a file name without extension

    Parameters:
    filename (str): name of the file with extension

    Returns:
    str: name of the file without the extension
    """
    return os.path.splitext(filename)


def gen_wordcloud_directory(dirname : str):
    """Iterates through <dirname> files and generates their wordclouds"""
    directory = os.path.dirname(__file__)
    path = os.path.join(directory, dirname)
    output_dir = os.path.join(directory, "../images/")
    for filename in os.listdir(path):
        file = os.path.join(path, filename)
        gen_wordcloud(
            file, os.path.join(output_dir, truncate_filename(filename)[0] + ".jpg")
        )


if __name__ == "__main__":
    gen_wordcloud_directory("../data")
