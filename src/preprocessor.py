from typing import Self

import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords


class PreProcessor:
    def __init__(self, text: str) -> None:
        self.__text: list[str] = nltk.word_tokenize(text)
        
    def get_processed_text(self) -> str:
        return " ".join(self.__text)
    
    def lowercase_all(self) -> Self:
        self.__text = [word.lower() for word in self.__text]
        return self
        
    def stem(self) -> Self:
        stemmer = PorterStemmer()
        self.__text = [stemmer.stem(word) for word in self.__text]
        return self
    
    def lemmatize(self) -> Self:
        lemmatizer = WordNetLemmatizer()        
        self.__text = [lemmatizer.lemmatize(word) for word in self.__text]
        return self
    
    def remove_stopwords(self) -> Self:
        english_stopwords = set(stopwords.words('english'))       
        self.__text = [word for word in self.__text
                       if word not in english_stopwords]

        return self
    
    def remove_punctuation(self) -> Self:
        self.__text = [word for word in self.__text if word.isalpha()]
        return self
    
    def remove_digits(self) -> Self:
        self.__text = [word for word in self.__text if not word.isdigit()]
        return self
