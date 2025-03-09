#!/usr/bin/env python3
import re

class MyString:
    """
    A custom string class that extends built-in string functionality.
    """

    def __init__(self, value=""):
        """
        Initializes the MyString object with a string value.
        Ensures only strings are assigned.
        """
        self._value = ""
        self.value = value  # Uses the setter to validate input

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")  # ✅ Print instead of raising an error
        else:
            self._value = new_value

    def is_sentence(self):
        """Checks if the string ends with a period (.)"""
        return self.value.endswith(".")

    def is_question(self):
        """Checks if the string ends with a question mark (?)"""
        return self.value.endswith("?")

    def is_exclamation(self):
        """Checks if the string ends with an exclamation mark (!)"""
        return self.value.endswith("!")

    def count_sentences(self):
        """
        Counts the number of sentences in the string.
        Handles various sentence-ending punctuation marks: ., !, ?
        """
        if not self.value.strip():
            return 0  # Handle empty string case

        # Normalize punctuation
        normalized_value = re.sub(r"[!?]", ".", self.value)

        # Split on '.' and remove empty strings
        sentences = [s.strip() for s in normalized_value.split(".") if s.strip()]

        return len(sentences)
