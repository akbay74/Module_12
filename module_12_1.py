import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        t_walk = Runner('Ivan')
        for _ in range(10):
            t_walk.walk()
        self.assertEqual(t_walk.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        t_run = Runner('Pavel')
        for _ in range(10):
            t_run.run()
        self.assertEqual(t_run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        t_walk = Runner('Ivan')
        t_run = Runner('Pavel')
        for _ in range(10):
            t_walk.walk()
            t_run.run()
        self.assertNotEqual(t_walk.walk, t_run.run)

