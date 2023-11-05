import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())
    
    def test_search(self):
        self.assertEqual(self.stats.search("Semenko"), PlayerReaderStub().get_players()[0])
    
    def test_searching_for_player_that_does_not_exist(self):
        self.assertIsNone(self.stats.search("Selänne"))    

    def test_searching_for_team(self):
        self.assertEqual(self.stats.team("PIT"), [PlayerReaderStub().get_players()[1]])

    def test_top_with_default_parameter(self):        
        self.assertListEqual(self.stats.top(1), [PlayerReaderStub().get_players()[4], PlayerReaderStub().get_players()[1]])

    def test_top_with_goals(self):        
        self.assertListEqual(self.stats.top(1, SortBy.GOALS), [PlayerReaderStub().get_players()[1], PlayerReaderStub().get_players()[3]])
    
    def test_top_with_assists(self):        
        self.assertListEqual(self.stats.top(1, SortBy.ASSISTS), [PlayerReaderStub().get_players()[4], PlayerReaderStub().get_players()[3]])