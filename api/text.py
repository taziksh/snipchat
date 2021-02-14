import re

import pkg_resources
from symspellpy import SymSpell, Verbosity

import nltk

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

    def cleaned(self, string):
        return re.sub('[,.]', '', string).lower()

    def spell_checked(self, term):
        suggestions = self.sym_spell.lookup(term, Verbosity.CLOSEST, max_edit_distance=2)
        if suggestions:
            return suggestions[0].__dict__['_term']


    #TODO: spell_check won't always work
    def phonemes_of(self, term):
        term = term.lower()
        if term not in self.arpabet:
            term = spell_checked(term)
        return self.arpabet[term][0]
