def definitionrequest():
  from PyDictionary import PyDictionary

  word1 = input ("Which word would you like to define?>\n")
  dictionary=PyDictionary()
  print (dictionary.meaning(word1))