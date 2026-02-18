from yahtzee import Yahtzee


class TestYahtzee:

    def test_chance(self):
        assert Yahtzee.chance(1, 2, 3, 4, 5) == 15
        assert Yahtzee.chance(6, 6, 6, 6, 6) == 30
        
    def test_yahtzee(self):
        assert Yahtzee.yahtzee([1, 1, 1, 1, 1]) == 50
        assert Yahtzee.yahtzee([1, 1, 1, 1, 2]) == 0
        
    def test_ones(self):
        assert Yahtzee.ones(1, 2, 1, 4, 1) == 3
        assert Yahtzee.ones(2, 2, 3, 4, 5) == 0

    def test_twos(self):
        assert Yahtzee.twos(2, 2, 2, 4, 5) == 6
        assert Yahtzee.twos(1, 3, 4, 5, 6) == 0

    def test_threes(self):
        assert Yahtzee.threes(3, 3, 3, 3, 3) == 15
        assert Yahtzee.threes(1, 2, 4, 5, 6) == 0

    def test_fours(self):
        game = Yahtzee(4, 4, 2, 5, 4)
        assert game.fours() == 12

    def test_fives_and_sixes(self):
        game = Yahtzee(5, 5, 5, 6, 6)
        assert game.fives() == 15
        assert game.sixes() == 12

    def test_score_pair(self):
        assert Yahtzee.score_pair(3, 3, 4, 5, 6) == 6
        assert Yahtzee.score_pair(3, 3, 4, 4, 6) == 8
        assert Yahtzee.score_pair(1, 2, 3, 4, 5) == 0

    def test_two_pair(self):
        assert Yahtzee.two_pair(3, 3, 5, 5, 6) == 16
        assert Yahtzee.two_pair(1, 1, 2, 3, 4) == 0

    def test_three_and_four_of_a_kind(self):
        assert Yahtzee.three_of_a_kind(2, 2, 2, 4, 5) == 6
        assert Yahtzee.four_of_a_kind(6, 6, 6, 6, 3) == 24

    def test_small_and_large_straight(self):
        assert Yahtzee.smallStraight(1, 2, 3, 4, 5) == 15
        assert Yahtzee.largeStraight(2, 3, 4, 5, 6) == 20
        assert Yahtzee.smallStraight(1, 2, 2, 4, 5) == 0

    def test_fullHouse(self):
        assert Yahtzee.fullHouse(2, 2, 3, 3, 3) == 13
        assert Yahtzee.fullHouse(2, 2, 2, 3, 3) == 12
        assert Yahtzee.fullHouse(2, 2, 2, 2, 3) == 0
    
        