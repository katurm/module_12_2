import unittest
import runner_2 as r2


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runer_1 = r2.Runner('Усэйн', 10)
        self.runer_2 = r2.Runner('Андрей', 9)
        self.runer_3 = r2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    def test_turn1(self):
        turn_1 = r2.Tournament(90, self.runer_1, self.runer_3)
        result = turn_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn1'] = result

    def test_turn2(self):
        turn_2 = r2.Tournament(90, self.runer_2, self.runer_3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn2'] = result

    def test_turn3(self):
        turn_3 = r2.Tournament(90, self.runer_1, self.runer_2, self.runer_3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn3'] = result