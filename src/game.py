import random

words = ["arthur", "please", "give", "good", "mark"]

def find_all_positoins_in_word(word, char_to_find):
    return [pos for pos, char in enumerate(word) if char == char_to_find]

def change_letters_in_positions(word, list_of_positions, letter):
    list_of_letters = list(word)
    for pos in list_of_positions:
        list_of_letters[pos] = letter
    return "".join(list_of_letters)

def step_of_game(answer_word, guessed_word):
    while True:
        input_char = input("Guess a letter:\n")
        if len(input_char) == 1 and input_char.isalpha():
            break
        else:
            print("Please, enter only one letter!")
            continue

    if input_char in guessed_word:
        all_inputs_of_word = find_all_positoins_in_word(guessed_word, input_char)
        changed_word = change_letters_in_positions(answer_word, all_inputs_of_word, input_char)
        return changed_word
    else:
        return answer_word

def run_game():
    random_number = random.randint(0, len(words) - 1)
    guessed_word = words[random_number]
    answer_word = '*' * len(guessed_word)
    count_of_attempt = 0
    while count_of_attempt != 5:
        guessed_step = step_of_game(answer_word, guessed_word)

        if answer_word != guessed_step:
            print('Hit!\n')
        else:
            count_of_attempt = count_of_attempt + 1
            print('Missed, mistake ', count_of_attempt, ' out of 5.')
        answer_word = guessed_step
        print('The word: ', answer_word, '\n')

        if '*' not in answer_word:
            break

    if '*' in answer_word:
        print('You lost!')
    else:
        print('You won!')

if __name__ == '__main__':
    run_game()
