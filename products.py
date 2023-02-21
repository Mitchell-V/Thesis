import json
from collections import defaultdict
import nltk
from nltk import tokenize

with open('products.json') as file:
    products = json.load(file)

queries = defaultdict(int)
brand_freq = defaultdict(int)
highlight_freq = defaultdict(int)

prods = {prod['title']: prod for prod in products}
no_descr = 0

for product, properties in list(prods.items()):
    brand_freq[properties['brand']] += 1
    highlight_freq['highlights'] += 1
    #print(properties['description'])
    #print('###')
    #print(properties['highlights'])
    #print('!!!')
    no_descr += 1 if not properties['description'] else 0

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
