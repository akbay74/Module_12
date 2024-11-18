import unittest
import logging
from tournament import Runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding="utf-8",
                    format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            t_walk = Runner('Ivan', -5)
            for _ in range(10):
                t_walk.walk()
            self.assertEqual(t_walk.distance, 50)
            logging.info('test_walk выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            t_run = Runner(1111, 5)
            for _ in range(10):
                t_run.run()
            self.assertEqual(t_run.distance, 100)
            logging.info('test_run выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

if __name__ == '__main__':
    unittest.main()