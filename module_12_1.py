import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        t_walk = Runner('Ivan')
        for _ in range(10):
            t_walk.walk()
        self.assertEqual(t_walk.distance, 50)

    def test_run(self):
        t_run = Runner('Pavel')
        for _ in range(10):
            t_run.run()
        self.assertEqual(t_run.distance, 100)

    def test_challenge(self):
        t_walk = Runner('Ivan')
        t_run = Runner('Pavel')
        for _ in range(10):
            t_walk.walk()
            t_run.run()
        self.assertNotEqual(t_walk.walk, t_run.run)

