"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    count = 0       # track the # of paragraphs that satisfy select()
    for i in range(len(paragraphs)):
        if select(paragraphs[i]):
            count += 1
        if count == k + 1:
            return paragraphs[i]
    # Exceed the length of PARAGRAPHS
    return ""

    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def in_topic(p):
        words = split(lower(remove_punctuation(p)))
        for t in topic:
            if t in words:
                return True
        else:
            return False
    return in_topic
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    # If reference is empty
    numerator = 0
    denominator = len(typed_words)
    if denominator == 0:
        return 0.0
    for i in range(min(len(typed_words), len(reference_words))): 
        if typed_words[i] == reference_words[i]:
            numerator += 1
    return 100 * numerator / len(typed_words)
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    return (len(typed) / 5) / (elapsed / 60)
    # END PROBLEM 4


###########
# Phase 2 #
###########


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    # Case 1: user_word is contained in valid_words.
    if user_word in valid_words:
        return user_word
    # Case 2: Computer the differences between user_word and all valid words.
    diffs = [diff_function(user_word, word, limit) for word in valid_words]
    # Case 2.1: If lowest_diff is greater than limit.
    if min(diffs) > limit:
        return user_word
    # Case 2.2: Find the index of the first lowest valid word.
    else:
        index, lowest_diff = 0, diffs[0]
        for i in range(1, len(diffs)):
            if diffs[i] < lowest_diff:
                index = i
                lowest_diff = diffs[i]
        return valid_words[index]
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    def helper(start, goal, diff):
        # Indicator for the recursion to go either direction.
        indicator = int(start[0] != goal[0])
        # Additional parameter DIFF tracks the differences in recursion procedure and stop it once DIFF reaches LIMIT.
        if diff > limit:
            return limit + 1
        # Base Case: The either length of the words is 1.
        elif 1 in [len(start), len(goal)]:
            abs_diff = abs(len(start) - len(goal))
            return abs_diff + indicator
        # Recursion Case
        else:
            return helper(start[1:], goal[1:], diff + indicator) + indicator

    return helper(start, goal, diff=0) 
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    assert False, 'Remove this line'

    if ______________: # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END

    elif ___________: # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END

    else:
        add_diff = ... # Fill in these lines
        remove_diff = ...
        substitute_diff = ...
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    def get_progress(typed, prompt, n):
        if typed == [] or typed[0] != prompt[0]:
            return n
        else:
            return get_progress(typed[1:], prompt[1:], n + 1)
    ratio = get_progress(typed, prompt, 0) / len(prompt)
    send({"id": user_id, "progress": ratio})
    return ratio
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    def get_time_diff(time):
        """Given a list of timestamps, return a list of the corresponding time differences"""
        return [time[i + 1] - time[i] for i in range(len(time) - 1)]
    times = [get_time_diff(tpp) for tpp in times_per_player]
    return game(words, times)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    words = [[] for pi in player_indices]
    # for each word in words:
    for wi in word_indices:
        # get the word
        word = word_at(game, wi)
        # get the time of all players typing this word
        times_of_word = [time(game, pi, wi) for pi in player_indices]
        # get the index (player_num) of the lowest value in times
        player_num = times_of_word.index(min(times_of_word))
        # put the word in the player_num'th list
        words[player_num] += [word]
    return words
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)