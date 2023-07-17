#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.set_value(value)

  def get_value(self):
    return self.get_value

  def set_value(self,value):
    if isinstance(value,str):
        self._value = value
    else:
      print("The value must be a string.")

  value = property(get_value,set_value,)

  def is_sentence(self):
    sentence = list(self._value)
    if sentence[-1]==".":
      return True
    return False

  def is_question(self):
    sentence = list(self._value)
    if sentence[-1]=="?":
      return True
    return False

  def is_exclamation(self):
    sentence = list(self._value)
    if sentence[-1]=="!":
      return True
    return False

  def count_sentences(self):
    count = 0
    sentences = list(self._value)
    previous = ""
    for i in range(len(sentences)):
      if sentences[i] in [".","?","!"]:
        if sentences[i] != previous:
          count +=1
      previous = sentences[i]
    return count
