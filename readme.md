# Weird Nickname Generator

This generator is time saver for sign up forms. It allows you quickly form unique nickname with interesting patterns and dictionaries( you can enter your own patterns and dictionaries)

## Table of Contents

* [Patterns](#patterns)
* [Dictionaries](#dictionaries)

## Patterns

The pattern of your nickname should look like this:

```
sometext_of_symbols{noun}_{verb}_
```

You need to follow python's format syntaxis. The words in {} brackets mean names of dictionaries files. You need to pass that filenames to the args of program

Also, you can store patterns in file seperated by *next line* symbol

## Dictionaries

You can create your dictionaries by finding words you want in dictionary in the web. Then you do it, just create file with *filename* and store words into it seperated by *next line* symbol. Example for file with *filename* looks like this:

*filename*:

```
word1
word2
word3
```

python main.py -d *filename* *dictionary2* -p patterns

will upload all words from dictionary with filename
