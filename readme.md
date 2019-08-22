# Weird Nickname Generator

This generator is time saver for sign up forms. It allows you quickly form unique nickname with interesting patterns and dictionaries( you can enter your own patterns and dictionaries)

## Table of Contents

* [Patterns](#patterns)
* [Dictionaries](#dictionaries)
* [Usage](#usage)

## Patterns

The pattern of your nickname should look like this:

```
sometext_of_symbols{noun[0]}_{verb[0]}_{noun[1]}
```

You need to follow python's format syntax. The words in {} brackets mean names of dictionary files. You need to pass those filenames to the args of program(or use predefined filenames)

Also, you can store patterns in file separated by *next line* symbol

## Dictionaries

You can create your dictionaries by finding words you want and store them to the file with *filename* separated by *next line* symbol. Example for file with *filename* looks like this:

*filename*:

```
word1
word2
word3
```

python main.py -d *filename* *dictionary2* -p patterns

will upload all words from dictionary with filename

## Usage

To start program
> python main.py

Then use special hotkeys:
'n' - next nickname
'p' - previous nickname
'q' - quit
