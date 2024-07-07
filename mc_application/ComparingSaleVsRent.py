from cost_of_living_calculator.HouseBuyMortgageCostCalculator import HouseBuyMortgageCostCalculator
from cost_of_living_calculator.HouseRent import HouseRent
from cost_of_living_calculator.HouseSale import HouseSale
from cost_of_living_calculator.MortgageCalculator import MortgageCalculator
from cost_of_living_calculator.PassiveInvestmentCalc import PassiveInvestmentCalc


class ComparingSalesVsRent:

    @staticmethod
    def __main__():
        house_buy_price = 365_000
        mort_renegotiation_fee = 3_600
        house_buy_other_costs = 7_000
        completed_repayment_years = 5
        renovation_costs = 75_000
        sale_price = 470_000
        admin_fees = 1_100
        vlt_cost_per_year = 487

        mortgage_calc = MortgageCalculator(house_buy_price)
        monthly_mortgage_payment = mortgage_calc.get_monthly_payment()
        # House management / renovation costs
        house_buy_costs = HouseBuyMortgageCostCalculator(house_buy_price, mort_renegotiation_fee, house_buy_other_costs,
                                                         renovation_costs, admin_fees, completed_repayment_years,
                                                         vlt_cost_per_year, monthly_mortgage_payment)

        ############## House Sale ##############

        house_sale = HouseSale(sale_price, 0.01, 5000)

        ############## House Rent ##############
        # House Rent
        rent = 2_100
        rent_increase = 0.04

        house_rent = HouseRent(rent, completed_repayment_years, rent_increase)

        house_rent_total = house_rent.total_rent

        ################### Passive Investment ###########

        house_buy_price_down_payment = 365_000 * 0.10
        total_value_of_initial_home_buy = (
                house_buy_price_down_payment + mort_renegotiation_fee + house_buy_other_costs)
        passive_investment_calc = PassiveInvestmentCalc(total_value_of_initial_home_buy, completed_repayment_years,
                                                        0.04)

        ############## Print Results ##############

        print("-" * 50)
        print("House Rent Costs")
        print(f"Total rent paid over 5 years: {house_rent_total:.2f}")
        print(f"Total value of initial home buy (unused): {total_value_of_initial_home_buy:.2f}")
        print(f"return on investment of unused down_payment: "
              f"{passive_investment_calc.calculate():.2f}, delta: "
              f"{passive_investment_calc.calculate() - total_value_of_initial_home_buy:.2f}")

        print("-" * 50)
        print("House Buy Costs")

        total_house_management_costs = (house_buy_costs.get_total_cost_living_in_mortgage())
        debt_with_bank = mortgage_calc.get_debt_left_after_years(completed_repayment_years)

        print(f"management and renovations in 5 years: "
              f"{total_house_management_costs}")
        print("-" * 50)
        print("House Sales Costs")
        house_sale = house_sale.get_return_from_sale()

        lump_sum_after_full_mortgage_repayment = house_sale - debt_with_bank
        roi = lump_sum_after_full_mortgage_repayment - total_house_management_costs
        print(f"proceeds after repaying bank:"
              f" {round(lump_sum_after_full_mortgage_repayment)}")
        print(f"balance after 5 years(house sale - debt with bank): {house_sale} - {debt_with_bank}:\n")
        print(f"Real ROI: {roi}")

        print("-" * 50)

        print("Comparing Rent vs Buy")
        print(f"Rent (5yrs): {house_rent_total:.2f}")
        print(f"Buy (5yrs): {house_buy_costs.get_total_cost_living_in_mortgage()}")
        print(f"Cost of living in mortgage per year: {round(house_buy_costs.get_total_cost_per_year())}")
        print(f"Cost of living in mortgage per month: {house_buy_costs.get_total_cost_per_year() / 12}")
        print(f"Cost of living in mortgage per year: {round(house_rent.total_rent / 5)}")
        print(f"Cost of living in mortgage per month: {round(house_rent.total_rent / 5 / 12)}")
        print(f"Cost of living in mortgage per year: {round(house_rent.total_rent / 5)}")

        print("-" * 50)
        print("Investing lump sum after sales")
        print(f"Proceeds after repaying bank: {round(lump_sum_after_full_mortgage_repayment)}")
        home_sale = PassiveInvestmentCalc(lump_sum_after_full_mortgage_repayment, 1, 0.10)
        monthly_returns = round((home_sale.calculate() - lump_sum_after_full_mortgage_repayment) / 12)
        print(f"return on investment for 1 year: {home_sale.calculate() - lump_sum_after_full_mortgage_repayment:.2f}")
        print(f"return on investment for 1 month: {monthly_returns:.2f}")


if __name__ == '__main__':
    ComparingSalesVsRent().__main__()
