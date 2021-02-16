import re

import pkg_resources
from symspellpy import SymSpell, Verbosity

import nltk

from functools import lru_cache
from itertools import product as iterprod

#TODO: stick with stmspell defaults more
class Utilities:
    def __init__(self):
        self.sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
        dictionary_path = pkg_resources.resource_filename(
            "symspellpy", "frequency_dictionary_en_82_765.txt")
        self.sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

        try:
            self.arpabet = nltk.corpus.cmudict.dict()
        except LookupError:
            nltk.download('cmudict')
            self.arpabet = nltk.corpus.cmudict.dict()

    #TODO: write more robust regex for musicals
    def cleaned(self, string, is_musical=False):
        string = re.sub('[,.]', '', string).lower()
        if is_musical:
            string = re.sub('\[\w+:]', '', string)
        return string

    def concatenated(self, lst):
        return ', '.join(lst).replace(', ', ' ')

    @lru_cache()
    def recursed(self, s):
        if s in self.arpabet:
            return self.arpabet[s]
        middle = len(s)/2
        partition = sorted(list(range(len(s))), key=lambda x: (x-middle)**2-x)
        for i in partition:
            pre, suf = (s[:i], s[i:])
            if pre in self.arpabet and self.recursed(suf) is not None:
                #TODO: memoize unknown words
                return [x+y for x,y in iterprod(self.arpabet[pre], self.recursed(suf))]
        return None

    def spell_checked(self, term):
        suggestions = self.sym_spell.lookup(term, Verbosity.CLOSEST, max_edit_distance=2)
        if suggestions:
            return suggestions[0].__dict__['_term']


    def phonemes_of(self, term):
        term = term.lower()
        if term not in self.arpabet:
            term = self.recursed(term)
            if term:
                return term[0]
        if not term:
            return ''
        phonemes = self.arpabet[term]
        return phonemes[0]
