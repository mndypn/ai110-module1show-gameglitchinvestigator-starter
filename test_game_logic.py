from logic_utils import check_guess, attempts_remaining, is_out_of_attempts

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_high_low_direction_fixed():
    # Regression test for the reversed direction: a high guess must report
    # "Too High" and a low guess must report "Too Low".
    assert check_guess(75, 30) == "Too High"
    assert check_guess(12, 88) == "Too Low"


def test_fresh_game_shows_full_attempts():
    # Regression for the attempts bug: a brand-new game has used 0 attempts,
    # so Normal (limit 8) must show 8 attempts left, not 7.
    assert attempts_remaining(8, 0) == 8


def test_attempts_remaining_counts_down():
    # After 3 guesses on a limit of 8, the player should have 5 left.
    assert attempts_remaining(8, 3) == 5


def test_not_out_of_attempts_before_limit():
    # On attempt 7 of 8, the game must still be playable.
    assert is_out_of_attempts(7, 8) is False


def test_out_of_attempts_only_at_limit():
    # The game ends exactly when all attempts are used, not one early.
    assert is_out_of_attempts(8, 8) is True