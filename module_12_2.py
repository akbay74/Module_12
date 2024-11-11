from run_tour import Runner, Tournament
from unittest import TestCase

class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run1 = Runner('Усэйн', 10)
        self.run2 = Runner('Андрей', 9)
        self.run3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for t_key, t_value in cls.all_results.items():
            print(f'Забег: {t_key}')
            for key, value in t_value.items():
                print(f'{key}: {value.name}')

    def test_round1(self):
        round_1 = Tournament(90, self.run1, self.run3)
        result = round_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Первый раунд'] = result

    def test_round2(self):
        round_2 = Tournament(90, self.run2, self.run3)
        result = round_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Второй раунд'] = result

    def test_round3(self):
        round_3 = Tournament(90, self.run1, self.run2, self.run3)
        result = round_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Третий раунд'] = result
