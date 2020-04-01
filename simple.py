from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'constitution.txt')).read()

# 引入分词包jieba
import jieba
wordlist = jieba.cut(text, cut_all=True)
word_space_split = " ".join(wordlist)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
wordcloud = WordCloud(background_color="black", max_words=2000, max_font_size=60, random_state=42, scale=2, font_path="simkai.ttf").generate(word_space_split)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()
