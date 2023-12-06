"""This file creates wordclouds using text files"""

from wordcloud import WordCloud
from pathlib import Path
import os

def gen_wordcloud(file, output):
    """Generates wordcloud from `file` and saves at `output`"""
    text = open(file).read()
    wordcloud = WordCloud(width = 1280 , height = 720).generate(text)
    wordcloud.to_file(Path(str(output) +  '.jpg'))

def truncate_filename(filename):
    return(Path(filename).stem)

def gen_wordcloud_directory(path):
    p = Path(path)
    output_dir = Path("../images/")
    for filename in os.listdir(path):
        f = Path(filename)
        path_ = p / f
        print(path_)
        gen_wordcloud(path_,
                      output_dir / Path(truncate_filename(filename)))
