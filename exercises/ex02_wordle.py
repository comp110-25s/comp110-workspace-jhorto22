
"""Making a wordle!!"""


__author__: str = "730759854"




def contains_char(word: str, letter: str) -> bool:
    """Figuring out if the letter is in the word"""
    # Making sure the letter guess is only 1 letter
    assert len(letter) == 1, f"len('{letter}') is not 1"
    idx: int = 0
    while idx < len(word):
        if letter == word[idx]:
            return True
        else:
            idx = idx + 1
    # If the letter is not in the word
    return False




def emojified(guess: str, secret: str) -> str:
    """Making colored emojis for the wordle"""
    assert len(guess) == len(secret), "Guess must be the same length as secret"

    # Setting up our emoji colors; White box means a letter does not exist in the word
    WHITE_BOX: str = "\U00002B1C"
    # Green box means the letter is in the word and the correct place
    GREEN_BOX: str = "\U0001F7E9"
    # Yellow box means the letter is in the word in the wrong place
    YELLOW_BOX: str = "\U0001F7E8"

    idx: int = 0
    conclusion: str = ""

    # Comparing guess with secret
    while idx < len(guess):
        if guess[idx] == secret[idx]:
            conclusion = conclusion + GREEN_BOX
        else:
            if contains_char(secret, guess[idx]):
                conclusion = conclusion + YELLOW_BOX
            else:
                conclusion = conclusion + WHITE_BOX
        idx = idx + 1
    return conclusion




def input_guess(expected_length: int) -> str:
    """Making sure the word has the correct length """
    conclusion: str = input(f"Enter a {expected_length} character word: ")
    while expected_length != len(conclusion):
        conclusion: str = input(f"That wasn't {expected_length} characters! Try again: ")
    return conclusion




def main(secret: str) -> None:
    """The entrypoint of the program"""
    turns_taken: int = 0
    # Makes sure there is only up to 6 turns
    while turns_taken < 6:
        print(f"=== Turn {turns_taken + 1} /6 ===")
        # Where we get the guess
        guess = input_guess(len(secret))
        # Where we get the emoji to produce for the guess
        conclusion = emojified(guess, secret)
        print(conclusion)
        # Guess being correct means the person wins
        if guess == secret:
            print(f"You won in {turns_taken + 1}/6 turns!")
            return
        turns_taken = turns_taken + 1
    # Ran out of turns and did not guess correctly
    print("X/6 - Sorry, try again tomorrow!")




if __name__ == "__main__":
    main(secret="codes")



