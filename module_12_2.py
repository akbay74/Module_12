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

    def test_turn1(self):
        turn_1 = Tournament(90, self.run1, self.run3)
        result = turn_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Первый раунд'] = result

    def test_turn2(self):
        turn_2 = Tournament(90, self.run2, self.run3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Второй раунд'] = result

    def test_turn3(self):
        turn_3 = Tournament(90, self.run1, self.run2, self.run3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Третий раунд'] = result

if __name__ == '__main__':
    unittest.main()