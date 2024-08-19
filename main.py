def main():
    getReport()

def getContent():
        with open("github.com/omer-karaduman/bookbot/books/frankenstein.txt") as f:
            file_contents = f.read()
        return file_contents

def countWords(content):
    content = content.split()
    return len(content)

def countChars(content):
    content = content.lower()
    chars = {}
    for char in content:
        if char.isalpha():
            if char in chars:
                chars[char] +=1
            else:
                chars[char] =1 
    return chars

def getReport():
    content = getContent()
    numberOfWords =countWords(content)
    alphaChars = countChars(content)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{numberOfWords} words found in the document.")
    for char in alphaChars:
        print(f"The '{char}' character was found {alphaChars[char]} times")

main()