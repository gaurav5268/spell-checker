import os
import re
import string
from collections import Counter

class SpellChecker:
    def __init__(self, file_path):
        with open(file_path, 'r', encoding='ISO-8859-1') as f:
            self.file = f.readlines()
        self.vocab = self.process_data()
        self.word_count_dict = self.get_count()
        self.probs = self.get_probs()

    def process_data(self):
        words = []
        for line in self.file:
            line = line.strip().lower()
            word = re.findall(r'\w+', line)
            words.extend(word)
        return set(words)

    def find_wrong_word(self, sentence):
        wrong_words = []
        words = re.findall(r'\b\w+\b', sentence)  # Extract words with hyphens
        for word in words:
            # Remove punctuation from the word
            word_no_punct = word.strip(string.punctuation)
            if word_no_punct and word_no_punct.lower() not in self.vocab:
                wrong_words.append(word)
        return wrong_words


    def delete_letter(self, word, verbose=False):
        delete_l = []
        split_l = [(word[:i], word[i:]) for i in range(len(word))]
        delete_l = [s[0] + s[1][1:] for s in split_l]
        return delete_l

    def switch_letter(self, word, verbose=False):
        switch_l = []
        split_l = [(word[:i], word[i:]) for i in range(len(word))]
        for s in split_l:
            if len(s[1]) > 2:
                temp = s[0] + s[1][1] + s[1][0] + s[1][2:]
            elif len(s[1]) == 2:
                temp = s[0] + s[1][1] + s[1][0]
            elif len(s[1]) == 1:
                continue
            switch_l.append(temp)
        return switch_l

    def replace_letter(self, word, verbose=False):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        replace_l = []
        split_l = [(word[:i], word[i:]) for i in range(len(word))]
        for s in split_l:
            if len(s[1]) == 1:
                for l in letters:
                    if l != s[1][0]:
                        temp = l
                        replace_l.append(s[0] + temp)
            elif len(s) > 1:
                for l in letters:
                    if l != s[1][0]:
                        temp = l + s[1][1:]
                        replace_l.append(s[0] + temp)
        replace_set = set(replace_l)
        replace_l = sorted(list(replace_set))
        return replace_l

    def insert_letter(self, word, verbose=False):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        insert_l = []
        split_l = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        for s in split_l:
            for l in letters:
                insert_l.append(s[0] + l + s[1])
        return insert_l

    def edit_one_letter(self, word, allow_switches=True):
        edit_one_set = set()
        insert_l = self.insert_letter(word)
        delete_l = self.delete_letter(word)
        replace_l = self.replace_letter(word)
        switch_l = self.switch_letter(word)

        if allow_switches:
            ans = insert_l + delete_l + replace_l + switch_l
        else:
            ans = insert_l + delete_l + replace_l

        edit_one_set = set(ans)
        return edit_one_set

    def edit_two_letters(self, word, allow_switches=True):
        edit_two_set = set()
        one_edit = self.edit_one_letter(word)
        ans = []
        for w in one_edit:
            ans.append(w)
            ans.extend(self.edit_one_letter(w))
        edit_two_set = set(ans)
        return edit_two_set

    def get_count(self):
        return Counter(self.vocab)

    def get_probs(self):
        probs = {}
        total = 1
        for word in self.word_count_dict.keys():
            total = total + self.word_count_dict[word]

        for word in self.word_count_dict.keys():
            probs[word] = self.word_count_dict[word] / total
        return probs

    def get_corrections(self, word, n=2, verbose=False):
        suggestions = []
        n_best = []

        if word in self.probs.keys():
            suggestions.append(word)
        for w in self.edit_one_letter(word):
            if len(suggestions) == n:
                break
            if w in self.probs.keys():
                suggestions.append(w)
        for w in self.edit_two_letters(word):
            if len(suggestions) == n:
                break
            if w in self.probs.keys():
                suggestions.append(w)

        best_words = {}

        for s in suggestions:
            best_words[s] = self.probs[s]

        best_words = sorted(best_words.items(), key=lambda x: x[1], reverse=True)
        n_best = best_words
        return n_best

    def get_correct_word(self, word, n):
        corrections = self.get_corrections(word, n, verbose=False)
        if len(corrections) == 0:
            return word

        final_word = corrections[0][0]
        final_prob = corrections[0][1]
        for i, word_prob in enumerate(corrections):
            if word_prob[1] > final_prob:
                final_word = word_prob[0]
                final_prob = word_prob[1]
        return final_word

    def autocorrect(self, sentence):
        print("Input sentence : ", sentence)
        wrong_words = self.find_wrong_word(sentence)
        print("Wrong words : ", wrong_words)
        correct_words = []
        for word in sentence.strip().lower().split(" "):
            if word in wrong_words:
                correct_word = self.get_correct_word(word, 15)
                word = correct_word
            correct_words.append(word)
        print("Output Sentence : ", " ".join(correct_words).capitalize())

    def autocorrect_sentence(self, sentence):
        corrected_words = []

        for word in sentence.strip().split():
            # Extract punctuation from the word
            word_no_punct = word.strip(string.punctuation)
            
            if word_no_punct.lower() not in self.vocab:
                corrected_word = self.get_correct_word(word_no_punct, 15)
                
                # Add back the punctuation to the corrected word
                corrected_word = word.replace(word_no_punct, corrected_word)
                corrected_words.append(corrected_word)
            else:
                corrected_words.append(word)

        corrected_sentence = " ".join(corrected_words).capitalize()
        return corrected_sentence



if __name__ == "__main__":
    spell_checker = SpellChecker("C:\\Users\\Gravity\\Desktop\\New folder\\corpusdata.txt")
    sentence_to_check = "he is good at footbal."
    
    print("Input sentence:", sentence_to_check)
    wrong_words = spell_checker.find_wrong_word(sentence_to_check)
    print("Wrong words:", wrong_words)

    if wrong_words:
        corrected_sentence = spell_checker.autocorrect_sentence(sentence_to_check)
        print(f"Corrected sentence: {corrected_sentence}")
    else:
        print("No misspelled words found.")