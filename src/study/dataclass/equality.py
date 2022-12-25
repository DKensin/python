from dataclasses import dataclass

@dataclass
class DataclassArticle:
    title:      str
    author:     str
    language:   str

class NormalArticle:
    def __init__(self, title, author, language):
        self.title = title
        self.author = author
        self.language = language

first_normal_article = NormalArticle("dataclass", "anonymous", "en")
second_normal_article = NormalArticle("dataclass", "anonymous", "en")

first_dataclass_article = DataclassArticle("dataclass", "anonymous", "en")
second_normal_article = DataclassArticle("dataclass", "anonymous", "en")

print("Dataclass equal: ", first_dataclass_article == second_normal_article)
print("Normalclass equal: ", first_normal_article == second_normal_article)