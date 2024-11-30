def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(countWords(file_contents), " words found in the document")
        charCount = countChars(file_contents)
        sortedCharCount = sortDict(charCount)
        printCharCount(sortedCharCount)
        print(" --- End report --- ")


def countWords(text):
    return len(text.split())

def countChars(text):
    lowWords = text.lower()
    words = [*lowWords]
    charCount = {}
    for c in words:
        if c in charCount:
            charCount[c] += 1
        else:
            charCount[c] = 1
    return charCount        


def sortDict(charDict):
    chars = []
    for c in charDict:
        subDict = {"char": c, "count": charDict[c]}
        chars.append(subDict)
    chars.sort(reverse=True, key=sort_on)
    return chars

def sort_on(dict):
    return dict["count"]

def printCharCount(charDictArray):
    for c in charDictArray:
        character = c["char"]
        count = c["count"]
        if character.isalpha():
            print("The ", character, " character was found ", count, " times")


main()