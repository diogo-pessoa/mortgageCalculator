from unittest import TestCase

from cost_of_living_calculator.HouseRent import HouseRent


class TestHouseRent(TestCase):

    def setUp(self):
        print(f"Running test: {self._testMethodName}")
        self.house_rent = HouseRent(1000, 5, 0.04)

    def test_apply_yearly_rate_increase(self):
        print(self.house_rent.current_rent)
        self.house_rent.apply_yearly_rate_increase()
        print(self.house_rent.current_rent)
        self.assertEqual(1040, self.house_rent.current_rent)

    def test_calculate_total_rent(self):

        self.assertEqual(50957.568, self.house_rent.total_rent)

    def test_get_yearly_rate_increase(self):
        rent = 2100
        period = 12
        self.assertEqual(1216, self.house_rent.get_yearly_rate_increase(rent, period))
