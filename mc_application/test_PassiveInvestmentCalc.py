from unittest import TestCase

from cost_of_living_calculator.PassiveInvestmentCalc import PassiveInvestmentCalc


class TestPassiveInvestmentCalc(TestCase):

    def setUp(self):
        print("Running test: ", self._testMethodName)
        self.interest_calc = PassiveInvestmentCalc(10_000, 5, 0.4)

    def test_apply_yearly_interest_over_period(self):
        self.interest_calc.apply_yearly_interest_over_period()
        self.assertEqual(14343, round(self.interest_calc.current_lump_sum))

    def test_adding_lump_sum(self):
        self.interest_calc.lodge_lump_sum(1000)
        self.assertEqual(11000, self.interest_calc.current_lump_sum)

