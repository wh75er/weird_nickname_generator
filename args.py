import argparse

parser = argparse.ArgumentParser(description="Exports instagram's posts to vk's public page via VK API token.")

parser.add_argument("-p", metavar="patterns", nargs=1,
                    dest = "patterns",
                    default = "patterns",
                    help = "File with nickname patterns")
parser.add_argument("-d", metavar='dictionaries', nargs='+',
                    dest = "dicts",
                    default = [ "noun",
                                "verb",
                                "pronoun",
                                "adjective",
                                "adverb",
                                "preposition",
                                "conjunction",
                                "determiner",
                                "interjection"
                              ],
                    help = "Dictionaries files") 

args = parser.parse_args()
