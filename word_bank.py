import pandas
import random


class WordBank:

    def __init__(self):
        self.word_list = None
        self.current_index = None
        self.current_word = None

        try:
            self.update_wordlist()
        except FileNotFoundError:
            self.reset_bank()
        self.random_word()

    def update_wordlist(self):
        """Updates word list to only contain words in words_to_learn.csv"""
        word_dataframe = pandas.read_csv("./data/words_to_learn.csv")

        word_list = [{"English": row["English"], "French": row["French"]}
                     for (index, row) in word_dataframe.iterrows()]
        self.word_list = word_list

    def reset_bank(self):
        """Places all words in original file french_words.csv into words_to_learn.csv
        and word list"""
        word_dataframe = pandas.read_csv("./data/french_words.csv")

        word_list = [{"English": row["English"], "French": row["French"]}
                     for (index, row) in word_dataframe.iterrows()]
        self.word_list = word_list
        self.update_datafile()

    def update_datafile(self):
        """Updates words_to_learn.csv by placing all words in word list into file"""
        french_word_list = [word["French"] for word in self.word_list]
        english_word_list = [word["English"] for word in self.word_list]
        word_dict = {
            "French": french_word_list,
            "English": english_word_list,
        }
        word_df = pandas.DataFrame(word_dict)
        word_df.to_csv("./data/words_to_learn.csv")

    def remove_current_word(self):
        self.word_list.pop(self.current_index)
        self.update_datafile()
        self.update_wordlist()

    def random_word(self):
        self.current_index = random.randint(0, len(self.word_list) - 1)
        self.current_word = self.word_list[self.current_index]
        print(self.current_index, self.current_word)
        return self.current_word

    def check_out_of_cards(self):
        return len(self.word_list) <= 0
