# -*- coding: utf-8 -*-
from wordcloud import WordCloud
from pathlib import Path
import os


def gen_wordcloud(file, output):
    text = open(file).read()
    wordcloud = WordCloud(width = 1280 , height = 720).generate(text)
    wordcloud.to_file(output + '.jpg')

def truncate_filename(filename):
    return(Path(filename).stem)

def gen_wordcloud_directory(path):
    output_dir = "../images/"
    for filename in os.listdir(path):
        path_ = path + filename
        print(path_)
        gen_wordcloud(path_,
                      output_dir + truncate_filename(filename))


