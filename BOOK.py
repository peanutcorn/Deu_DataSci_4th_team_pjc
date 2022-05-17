from asyncio.windows_events import NULL
import pandas as pd

data1 = {'필드명': ['BOOK_ISBN', 'BOOK_TITLE', 'BOOK_AUTHOR', 'BOOK_PUB', 'BOOK_PRICE', 'BOOK_LINK', 'BOOK_IMAGE', 'BOOK_DESCRIPTION', 'BOOK_PRE'], 
    '설명' : ['ISBN', '제목', '저자', '출판사', '가격', '관련링크', '사진', '도서설명', '존재여부'],
    'Data Type': ['CHAR(13)', 'VARCHAR(100)', 'VARCHAR(30)', 'VARCHAR(30)', 'INT', 'TEXT', 'LONGBLOB', 'VARCHAR(255)', 'BOOLEAN'],
    'Key' : ['0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
    'UNIQUE' : [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
    'NN' : [NULL, '0', '0', '0', NULL, NULL, NULL, NULL, NULL],
    '기본값' : [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, True],
    '기타' : [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL]}
df = pd.DataFrame(data1)

print(df)
df.to_csv("./BOOK.csv", encoding = 'utf-8')