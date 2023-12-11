"""This file creates wordclouds using text files"""

from wordcloud import WordCloud
import os

def gen_wordcloud(file, output):
    """Generates wordcloud from `file` and saves at `output.jpg`"""
    try:
        text = open(file).read()
    except:
        text = open(file, encoding="cp850").read()
    wordcloud = WordCloud(width = 1280 , height = 720).generate(text)
    wordcloud.to_file(output)

def truncate_filename(filename):
    return os.path.splitext(filename)

def gen_wordcloud_directory(dirname):
    dir = os.path.dirname(__file__)
    path = os.path.join(dir,dirname)
    output_dir = os.path.join(dir, "../images/")
    for filename in os.listdir(path):
        file = os.path.join(path,filename)
        gen_wordcloud(file,
                      os.path.join(output_dir,truncate_filename(filename)[0] + '.jpg'))

if __name__ == "__main__":
    gen_wordcloud_directory("../data")