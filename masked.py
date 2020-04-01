from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'constitution.txt')).read()

# 引入分词包jieba
import jieba
wordlist = jieba.cut(text, cut_all=True)
word_space_split = " ".join(wordlist)

# read the mask image
alice_mask = np.array(Image.open(path.join(d, "alice_mask.png")))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask, max_font_size=60, random_state=42, scale=2, stopwords=stopwords, font_path="simkai.ttf")

# generate word cloud
wc.generate(word_space_split)

# show
coloring = np.array(Image.open("alice_mask.png"))
image_colors = ImageColorGenerator(coloring)
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")
plt.figure()
plt.axis("off")
plt.show()

# store to file
wc.to_file(path.join(d, "alice.png"))
