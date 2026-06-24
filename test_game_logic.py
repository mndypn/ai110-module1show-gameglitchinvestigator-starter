from logic_utils import check_guess

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