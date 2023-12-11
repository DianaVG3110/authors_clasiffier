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
    with open(file, encoding="utf8") as text_file:
        text = text_file.read()
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


def gen_wordcloud_directory(dirname : str, outputdir : str):
    """Iterates through files and generates their wordclouds
    
    Parameters:
    dirname (str): name of the directory where the text files are
    outputdir (str): path where the generated images needs to be placed
    """
    directory = os.path.dirname(__file__)
    path = os.path.join(directory, dirname)
    output_dir = os.path.join(directory, outputdir)
    for filename in os.listdir(path):
        file = os.path.join(path, filename)
        gen_wordcloud(
            file, os.path.join(output_dir, truncate_filename(filename)[0] + ".jpg")
        )


if __name__ == "__main__":
    gen_wordcloud_directory("../data","../images")
