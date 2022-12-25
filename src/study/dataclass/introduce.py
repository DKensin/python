from dataclasses import dataclass

@dataclass
class Article:
    title:      str
    author:     str
    language:   str

first_article = Article("dataclass", "toan", "en")
second_article = Article("a demo", "anonymous", "en")

print(first_article)
print(second_article)

print(first_article.author)
print(second_article.author)