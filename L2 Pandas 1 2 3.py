

import pandas as pd
import numpy as np

## Задание 1

authors = pd.DataFrame(
    {
        "author_id": [1,2,3],
        "author_name": ['Тургенев', 'Чехов', 'Островский'],
       }
)

print(authors)

book = pd.DataFrame(
    {
        "author_id": [1,1,1,2,2,3,3],
        "book_title": ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
        "price": [450, 300, 350, 500, 450, 370, 290],
       }
)

print(book)

##Задание 2

authors_price = authors.merge(book)

print(authors_price)

## Задание 3

authors_price = authors_price.sort_values(by = ['price'], ascending=False)

top5 = authors_price.head(5)

print(top5)

## Задание 4



authors_stat = pd.pivot_table(top5,
                              index="author_name",
                              values="price",
                              aggfunc=[np.min,np.max,np.mean])

print(authors_stat)




