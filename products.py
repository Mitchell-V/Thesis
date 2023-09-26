"""
Title: Product data AH
Name: Mitchell Verhaar
Description:
Data set exploration. Keep following data:

- Description(?), Highlights, Title, Volume, Taxonomy
- Aggregrate query products, determine relevancy of product to query to add
- Normalize add ratios in click data
- Literature to find product relevancy?
- Add properties as list
- Train/Val/Test split (80%/10%/10%)

Click data:
- Query
- Product position
- Product ID
- User Interaction
- Search ID
- 
"""

import json
from collections import defaultdict
import nltk
from nltk.stem.snowball import DutchStemmer
from nltk.corpus import stopwords
import string

nltk.download('stopwords')

stemmer = DutchStemmer(ignore_stopwords=True)
stopwords = stopwords.words('dutch')
symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"

with open('products.json') as file:
    products = json.load(file)

queries = defaultdict(int)
brand_freq = defaultdict(int)
highlight_freq = defaultdict(int)
prods = {prod['title']: prod for prod in products}
no_descr = 0
words_doc = defaultdict(set)
tf_idf = defaultdict(int)


doc_count = 0
for product, properties in list(prods.items()):
    brand_freq[properties['brand']] += 1
    highlight_freq['highlights'] += 1
    no_descr += 1 if not properties['description'] else 0

    for prop, text in properties.items():
        print(prop)
        if prop == 'description' or prop == 'highlights':
            prop_clean = ""
            for word in text.split(' '):
                if word not in stopwords:
                    word_clean = stemmer.stem(str.lower(word.translate(str.maketrans('', '', string.punctuation))))
                    if len(word_clean) > 1:
                        words_doc[word_clean].add(doc_count)
                        prop_clean += word_clean
            
    doc_count += 1


#print(sorted(words_doc.items(), key=lambda item: item[1], reverse=True)[:10])
print("Total number of products: ", len(prods.keys()))
print("Number of products with no description: ", no_descr)
print("Number of products with no highlights: ", highlight_freq[''])
print("Number of products with no brand information: ", brand_freq[''])
print(sorted(brand_freq.items(), key=lambda item: item[1], reverse=True))

# for prod in products:
#     prods[prod['title']] = prod
#     for key, val in prod.items():
#         if 'taxonomies' in key:
#             for tax in val:
#                 freq[tax] += 1
#         elif 'images' in key:
#             continue
#         elif 'properties' in key:
#             for prop in val:
#                 freq[prop] += 1
#         elif 'queries' in key:
#             for q in val:
#                 queries[q] += 1
#         else:
#             freq[val] += 1

#print(freq)
#print(sorted(queries.items(), key=lambda item: item[1], reverse=True)[:100])
