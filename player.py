import os

# runs the actuall running of the game
def play_game(dictionary, previous_guesses, previous_feedback):
    guess = make_new_guess(dictionary, previous_guesses, previous_feedback)
    print("I'll make the guess: ", guess)
    result = input("Please enter the result: ")
    previous_guesses.append(guess)
    previous_feedback.append(result)
    return result

# count all the letters in the guesses we have left to get their frequencies
def count_letters(word):
    letters = {}
    seen = set()
    for i in range(len(word)):
        if word[i] not in seen:
            letters[word[i]] = word.count(word[i])
            seen.add(word[i])
    return (letters)

# find all the possible guesses we can make given the results of all the previous guesses
def possible(test, dictionary, wrong):
        possible = []   
        for i in range(len(dictionary)):
            t = True
            for x in range(len(test)):    
                word = dictionary[i]
                if test[x] != '.':
                    if (not (test[x].upper() in word) or (test[x] == word[x].lower())) or (test[x].isupper() and test[x] != word[x]):
                        t = False
                        break
                if word[x] in wrong:
                    t = False
                    break
            if t == True and not(word in wrong):
                possible.append(word)    
        return (possible)

# find the best guess by calculating the value of each word (the more frequently occuring letters in a word the higher value it holds)
# uses count_letters and value_of_letters to get the value of each word
def best_guess(words, values):
      word_value = {}
      for i in range(len(words)):
          value = 0
          for x in range(len(words[i])):    
              if words[i][x] in values:
                  value += values[words[i][x]]
              else: value += 0.0000000000000000000000000000000000000000000001 #just add some arbitraly large number
          word_value[words[i]] = value
      word_value = {k:v for k,v in sorted(word_value.items(),key=lambda item: item[1], reverse=True)} #find our most valuable word
      return(list(word_value.keys())[0])

# using the frequencies lets find the value of the letters
def value_of_letters(answers):
    wordscont = ''.join(answers)
    lcount = count_letters(wordscont)
    c = {k:v/len(wordscont) for k,v in sorted(lcount.items(),key=lambda item: item[1], reverse=True)}
    return(c)

# the actuall running of the program
def make_new_guess(words, previous_guesses, previous_feedback):
    letters = value_of_letters(words)
    dictionary = words
    # start the process
    if len(previous_guesses) == 0:
        wrong = set()
        firstbest = 'RATED' #just the best guess, no need to calculate anything else
        wrong.add(firstbest)
        return firstbest     
    else:
        # uses the functions we made to solve for the word
        count = len(previous_guesses) - 1
        wrong = set(previous_guesses)
        for i in range(len(previous_guesses)):
            for x in range(5):
                result = previous_feedback[i]
                guess = previous_guesses[i]
                if result[x] == '.':
                    if guess[x] not in result:
                        if guess[x].lower() not in result:
                            wrong.add(guess[x]) 
        dictionary = possible(previous_feedback[count], dictionary, wrong)
        check = previous_feedback[count].replace('.','')
        l = []
        if len(check) == 4 and len(dictionary) > 4 and check.upper() == check:
            pos = previous_feedback[count].find('.')
            for i in range(len(dictionary)):
                l+= dictionary[i][pos]
            nextbest = best_guess(words, value_of_letters(l))
            return nextbest   
        if len(previous_feedback[count-1].replace('.','')) == 4:
            dictionary = possible(previous_feedback[count-1], dictionary, wrong)
        letters = value_of_letters(dictionary)
        nextbest = best_guess(dictionary, letters)
        return nextbest

previous_guesses = []
previous_feedback = []

# get the possible guesses we can make
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = open(os.path.join(location,'words.txt'), 'r')
dictionary = lines.read().upper().replace('"','').split(',')
lines.close()

result = play_game(dictionary, previous_guesses,previous_feedback)
while (result != result.upper() or "." in result):
    result = play_game(dictionary, previous_guesses,previous_feedback)

print("Congrats (You) won!")


