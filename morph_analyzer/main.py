from collections import namedtuple

import pymorphy2
import nltk


"""
Скрипт для частеречевого анализа текста.
Записывает в отдельные файлы слова из текста, которые относятся к конкретнйо чатси речи
"""

nltk.download('punkt')


FILE_NAME = 'text.txt'


WordAndPosPair = namedtuple('WordAndPosPair', 'word pos'.split())


def tokenize(file_name: str) -> str:
    with open(file_name, mode='r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line == '':
                # достигнут конец файла
                break
            tokens = nltk.word_tokenize(line.strip())
            for token in tokens:
                yield token


def get_file_name_to_save_word(file_name: str, pos: str) -> str:
    name, ext = file_name.split('.')
    return f'{name}_{pos}.{ext}'


def write_to_file(word: str, pos: str) -> None:
    with open(get_file_name_to_save_word(FILE_NAME, pos), mode='a', encoding='utf-8') as file:
        file.write(word + '\n')


def main() -> None:
    # множество кортежей вида (слово, часть-речи)
    used_lemmas = set()
    morph = pymorphy2.MorphAnalyzer()
    for token in tokenize(FILE_NAME):
        try:
            lemmas = morph.parse(token)
        except Exception:
            continue

        for lemma in lemmas:
            word_and_POS_pair = WordAndPosPair(lemma.normal_form, lemma.tag.POS)
            if word_and_POS_pair in used_lemmas:
                continue
            used_lemmas.add(word_and_POS_pair)
            write_to_file(word_and_POS_pair.word, word_and_POS_pair.pos)


if __name__ == '__main__':
    main()
