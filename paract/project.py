import sys

if (len(sys.argv)<2):
    print('Error, not enought arguments')
    exit(0)

counterOfWords = 0
wordsAndTheirCopies = {}
fileName = sys.argv[1]
with open(fileName, 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

with open(fileName, 'r', encoding='utf-8') as f:
    line = f.readline()
    while line:
        words = line.replace('.', ',').replace('!', ',').replace(';', ',').replace(
            ' ', ',').replace(';', ',').replace('\n', ',').split(',')
        for word in words:
            if (word != ''):
                if (wordsAndTheirCopies.get(word)):
                    wordsAndTheirCopies[word] = wordsAndTheirCopies.get(word)+1
                else:
                    wordsAndTheirCopies[word] = 1
                counterOfWords += 1
        line = f.readline()


with open('results.txt', 'w', encoding='utf-8') as f:
    f.write('count of lines = ' + str(len(lines)) + '\n')
    f.write('count of words = ' + str(counterOfWords) + '\n')
    f.write(' words and their copies:\n')
    for w in wordsAndTheirCopies:
        if (wordsAndTheirCopies.get(w)>1):
            f.write('word is: [' + str(w) + '] count of it: [' +
                str(wordsAndTheirCopies.get(w)) + ']\n')

print('press any key and please check file what called "results.txt"')
a = input()
