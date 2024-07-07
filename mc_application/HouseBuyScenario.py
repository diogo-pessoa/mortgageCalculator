from cost_of_living_calculator.HouseBuyMortgageCostCalculator import HouseBuyMortgageCostCalculator
from cost_of_living_calculator.HouseSale import HouseSale
from cost_of_living_calculator.MortgageCalculator import MortgageCalculator


class HouseBuyScenario:
    def __main__(self):
        house_buy_price = 365_000
        mort_renegotiation_fee = 3_600
        house_buy_other_costs = 7_000
        completed_repayment_years = 15
        renovation_costs = 75_000
        sale_price = 470_000
        admin_fees = 1_100
        vlt_cost_per_year = 487
        self.mortgage_calc = MortgageCalculator(house_buy_price)
        self.mortgage_calc.subtract_early_repayment(40_000)
        self.house_sale = HouseSale(sale_price, 0.01, 5000)

        self.cost_of_living = HouseBuyMortgageCostCalculator(house_buy_price, mort_renegotiation_fee,
                                                             house_buy_other_costs, renovation_costs, admin_fees,
                                                             completed_repayment_years, vlt_cost_per_year,
                                                             self.mortgage_calc.get_monthly_payment())

        total_house_management_costs = (self.cost_of_living.get_total_cost_living_in_mortgage())
        house_sale = self.house_sale.get_return_from_sale()
        debt_with_bank = self.mortgage_calc.get_debt_left_after_years(completed_repayment_years)
        lump_sum_after_full_mortgage_repayment = house_sale - debt_with_bank
        roi = lump_sum_after_full_mortgage_repayment - total_house_management_costs
        print(f"debt after 5 years: {house_sale} - {debt_with_bank}:\n")
        print(f"proceeds after repaying bank:"
              f" {round(lump_sum_after_full_mortgage_repayment)}")
        print(f"management and renovations in 5 years: "
              f"{total_house_management_costs}")

        print(f"Real ROI: {roi}")


if __name__ == '__main__':
    HouseBuyScenario().__main__()
