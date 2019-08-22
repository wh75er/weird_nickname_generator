from generator import generate
from read_files import readDictionaries, readPatterns
from args import args

if __name__ == "__main__":
    patterns_filename = args.patterns
    dicts_filenames = args.dicts

    dicts = readDictionaries(dicts_filenames)
    patterns = readPatterns(patterns_filename)

    generate(dicts, patterns)
