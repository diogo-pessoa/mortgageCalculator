from cost_of_living_calculator.HouseRent import HouseRent
from cost_of_living_calculator.PassiveInvestmentCalc import PassiveInvestmentCalc


class HouseRentScenario:

    @staticmethod
    def __main__():
        rent = 2_100
        rent_increase = 0.04
        house_buy_price_down_payment = 365_000 * 0.10
        mort_renegotiation_fee = 3_600
        house_buy_other_costs = 7_000
        completed_repayment_years = 5
        total_value_of_initial_home_buy = (
                house_buy_price_down_payment + mort_renegotiation_fee + house_buy_other_costs)

        passive_investment_calc = PassiveInvestmentCalc(total_value_of_initial_home_buy,
                                                        completed_repayment_years, 0.04)

        house_rent = HouseRent(rent, completed_repayment_years, rent_increase)
        house_rent_total = house_rent.calculate_total_rent()
        print(f"Total rent paid over 5 years: {house_rent_total:.2f}")
        print(f"Total value of initial home buy (unused): {total_value_of_initial_home_buy:.2f}")
        print(f"Total value of initial home buy (unused) after 5 years: "
              f"{passive_investment_calc.calculate():.2f}")
        print(f"ROI: {passive_investment_calc.calculate() - total_value_of_initial_home_buy:.2f}")


if __name__ == '__main__':
    HouseRentScenario().__main__()
