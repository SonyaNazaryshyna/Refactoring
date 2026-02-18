from refactored_yahtzee import Yahtzee 


def test_chance_typical():
    """Перевірка, що метод chance повертає правильну суму для типового набору кісток."""
    game = Yahtzee(2, 3, 4, 5, 6)
    assert game.chance() == 20

def test_yahtzee_true():
    """Перевірка, що Yahtzee повертає 50 при п’яти однакових кубиках."""
    game = Yahtzee(6, 6, 6, 6, 6)
    assert game.yahtzee() == 50

def test_yahtzee_false():
    """Перевірка, що Yahtzee повертає 0, якщо кубики не однакові."""
    game = Yahtzee(1, 2, 3, 4, 5)
    assert game.yahtzee() == 0

def test_sum_of_various():
    """Перевірка, що sum_of правильно рахує суму конкретного числа."""
    game = Yahtzee(1, 2, 2, 3, 3)
    assert game.sum_of(1) == 1
    assert game.sum_of(2) == 4
    assert game.sum_of(3) == 6
    assert game.sum_of(4) == 0 

def test_score_pair_highest_pair():
    """Перевірка, що score_pair повертає найбільшу пару."""
    game = Yahtzee(3, 3, 2, 5, 5)
    assert game.score_pair() == 10  

def test_score_pair_none():
    """Перевірка, що score_pair повертає 0, якщо пар немає."""
    game = Yahtzee(1, 2, 3, 4, 5)
    assert game.score_pair() == 0

def test_two_pair_valid():
    """Перевірка двох пар."""
    game = Yahtzee(2, 2, 3, 3, 5)
    assert game.two_pair() == 10 

def test_two_pair_invalid():
    """Перевірка, що two_pair повертає 0, якщо пар менше двох."""
    game = Yahtzee(1, 1, 2, 3, 4)
    assert game.two_pair() == 0

def test_n_of_a_kind_variants():
    """Перевірка трьох та чотирьох однакових кубиків."""
    game = Yahtzee(2, 2, 2, 2, 5)
    assert game.three_of_a_kind() == 6
    assert game.four_of_a_kind() == 8
    assert game.n_of_a_kind(5) == 0  

def test_straights():
    """Перевірка малих і великих стрейтів."""
    small = Yahtzee(1, 2, 3, 4, 5)
    large = Yahtzee(2, 3, 4, 5, 6)
    assert small.small_straight() == 15
    assert small.large_straight() == 0
    assert large.large_straight() == 20
    assert large.small_straight() == 0

def test_full_house_valid():
    """Перевірка правильного full house."""
    game = Yahtzee(2, 2, 3, 3, 3)
    assert game.full_house() == 13

def test_full_house_invalid():
    """Перевірка, що full house повертає 0 при відсутності повної комбінації."""
    game = Yahtzee(1, 1, 1, 1, 1)
    assert game.full_house() == 0
