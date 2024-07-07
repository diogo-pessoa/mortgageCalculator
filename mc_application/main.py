from cost_of_living_calculator.HouseSale import HouseSale
from cost_of_living_calculator.HouseBuyMortgageCostCalculator import HouseBuyMortgageCostCalculator

"""

calculating mortgage costs over 5 years period

"""
initial_cost = (36_000 + 7_000)
mortgage_renegotiation_fee = 3_600
renovation_costs = 75_000
admin_fees = 1100
vlt_cost_per_year = 487
mortgage_monthly = 1_300
number_of_years = 5
house_price = 365_000
mortgage_cost = (HouseBuyMortgageCostCalculator(house_price, mortgage_renegotiation_fee,
                                                initial_cost, renovation_costs,
                                                admin_fees, number_of_years,
                                                vlt_cost_per_year, 0))


# print(mortgage_cost.get_total_cost_per_year())
# mortgage_cost.plot_mortgage_cost_per_month_five_years()
# mortgage_cost.plot_total_cost_per_year_stacking()
"""
House Sale
"""

sale_price = 470_000
mortgage_debt = 285_000
real_state_agent_commission = 4_700
solicitor_and_other_costs = 5_000
monthly_mortgage = 1_300
total_investment_when_buying = mortgage_cost.get_total_cost_living_in_mortgage()

house_sale = HouseSale(sale_price, mortgage_debt, real_state_agent_commission,
                       solicitor_and_other_costs, monthly_mortgage,
                       total_investment_when_buying)

print(house_sale)

"""
Rent
initial_rent = 2200
rent_increase = 0.05

table_of_monthly_costs["rent"] = initial_rent
for i in range(1, 61):
    table_of_monthly_costs.loc[i, "rent"] = initial_rent * (1 + rent_increase) ** (
            i // 12)

"""
