class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.score_is_equal()
        if self.player1_score >= 4 or self.player2_score >= 4:
            return self.either_player_score_is_four_or_more()

        return self.score_difference_is_between_one_and_three()

    def score_is_equal(self):
        match self.player1_score:
            case 0:
                score = "Love-All"
            case 1:
                score = "Fifteen-All"
            case 2:
                score = "Thirty-All"
            case _:
                score = "Deuce"
        return score

    def either_player_score_is_four_or_more(self):
        score_difference = self.player1_score - self. player2_score

        if score_difference == -1:
            score = "Advantage player2"
        elif score_difference == 1:
            score = "Advantage player1"
        elif score_difference >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def score_difference_is_between_one_and_three(self):
        return self.score_to_tennis_term(self.player1_score) + "-" + self.score_to_tennis_term(self.player2_score)

    def score_to_tennis_term(self, score):
        match score:
            case 0:
                return "Love"
            case 1:
                return "Fifteen"
            case 2:
                return "Thirty"
            case _:
                return "Forty"
   