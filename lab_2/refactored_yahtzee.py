class Yahtzee:
    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [d1, d2, d3, d4, d5]

    def chance(self):
        return sum(self.dice)

    def yahtzee(self):
        return 50 if len(set(self.dice)) == 1 else 0

    def sum_of(self, n):
        return sum(x for x in self.dice if x == n)
    
    def score_pair(self):
        pairs = [x for x in set(self.dice) if self.dice.count(x) >= 2]
        return max(pairs) * 2 if pairs else 0

    def two_pair(self):
        pairs = [x for x in set(self.dice) if self.dice.count(x) >= 2]
        if len(pairs) >= 2:
            top_two = sorted(pairs, reverse=True)[:2]
            return sum(top_two) * 2
        return 0
    
    def n_of_a_kind(self, n):
        for die in set(self.dice):
            if self.dice.count(die) >= n:
                return die * n
        return 0
    
    def three_of_a_kind(self):
        return self.n_of_a_kind(3)

    def four_of_a_kind(self):
        return self.n_of_a_kind(4)
    
    def small_straight(self):
        return 15 if set(self.dice) == {1, 2, 3, 4, 5} else 0

    def large_straight(self):
        return 20 if set(self.dice) == {2, 3, 4, 5, 6} else 0
    
    def full_house(self):
        counts = [self.dice.count(i) for i in set(self.dice)]
        if sorted(counts) == [2, 3]:
            pair = next(x for x in set(self.dice) if self.dice.count(x) == 2)
            three = next(x for x in set(self.dice) if self.dice.count(x) == 3)
            return pair * 2 + three * 3
        return 0