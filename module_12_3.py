import unittest
from module_12_1 import RunnerTest
from module_12_2 import TournamentTest

tour_TS = unittest.TestSuite()
tour_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
tour_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
ut_run = unittest.TextTestRunner(verbosity=2)
ut_run.run(tour_TS)