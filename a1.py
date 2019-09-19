import random
f = open("results.txt", "a+")
lines = open('sowpods.txt').read().splitlines()
word = random.choice(lines).strip()
word = list(word)
#print(word)
count = 0
err_count = 0
missed = ''
string = []
for i in range(0,len(word)):
    string.append('_ ')
while(count != len(word) and err_count != 6):
    print(''.join(string))
    print('missed: ' + missed)
    letter = input()
    guessed = 0
    for q in range(0,len(word)):
        if(letter == word[q]):
            string[q] = letter
            count = count + 1
            guessed = 1
    if guessed == 0:
        err_count += 1
        missed = missed + 'X'
if(count == len(word)):
    print("you win the word was " + ''.join(word))
    f.write(''.join(word) + ' ')
    f.write("guessed ")
    f.write(str(err_count) + '\n')
    f.close()
if(err_count == 6):
    print("you lose the word was " + ''.join(word))
    f.write(''.join(word) + ' ')
    f.write("not guessed ")
    f.write(str(err_count) + '\n')
    f.close()