def createLinesList(f):
    lst = []
    for line in f:
        line = line[:-1]
        lst.append(line)
    return lst

def readPatterns(filename):
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print("Error occured! File '{}' doesn't exist".format(filename))
        exit()
    lst = createLinesList(f)
    return lst
    

def readDictionaries(files):
    dicts = {}
    for filename in files:
        try:
            f = open("dictionaries/" + filename, "r")
        except FileNotFoundError:
            print("Error occured! File 'dictionaries/{}' doesn't exist".format(filename))
            exit()

        dicts.update({filename : createLinesList(f)})
        
        f.close()
    return dicts

if __name__ == "__main__":
    readDictionaries(["hello world"])
