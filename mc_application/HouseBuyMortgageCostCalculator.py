import pandas as pd
from matplotlib import pyplot as plt

from cost_of_living_calculator.MortgageCalculator import MortgageCalculator


class HouseBuyMortgageCostCalculator:

    def __init__(self, house_price, mortgage_renegotiation_fee, house_buy_other_costs,
                 renovation_costs, admin_fees_per_year, number_of_years_repaid,
                 vlt_cost_per_year, monthly_repayment):
        self.monthly_repayment = monthly_repayment
        self.mortgage_calc = MortgageCalculator(house_price)

        # Calculate the number of months paid
        self.months_repaid = number_of_years_repaid * 12

        self.mortgage_renegotiation_fee = mortgage_renegotiation_fee
        self.home_buy_other_costs = house_buy_other_costs
        self.renovation_costs = renovation_costs
        self.admin_fees_living_years = admin_fees_per_year * number_of_years_repaid
        self.vlt_cost_living_years = vlt_cost_per_year * number_of_years_repaid
        self.period_in_months = range(0, self.months_repaid)
        self.table_of_monthly_costs = pd.DataFrame(index=self.period_in_months,
                                                   columns=['mortgage', 'renovation',
                                                            'admin_fees', 'vlt',
                                                            'diluted_lump_sum',
                                                            'mortgage_renegotiation_fee',
                                                            'down_payment', 'total'])
        # Load table with cost_per_month and totals
        self._load_table_cost_per_month()
        self._calculate_total_cost_per_month()

    def _load_table_cost_per_month(self):
        for i in self.period_in_months:
            self.table_of_monthly_costs.loc[
                i, 'mortgage'] = self.monthly_repayment
            self.table_of_monthly_costs.loc[i, 'renovation'] = (
                    self.renovation_costs / self.months_repaid)
            self.table_of_monthly_costs.loc[
                i, 'vlt'] = self.vlt_cost_living_years / self.months_repaid
            self.table_of_monthly_costs.loc[
                i, 'admin_fees'] = self.admin_fees_living_years / self.months_repaid
            self.table_of_monthly_costs.loc[
                i, 'diluted_lump_sum'] = self.home_buy_other_costs / self.months_repaid
            self.table_of_monthly_costs.loc[i, 'mortgage_renegotiation_fee'] = (
                    self.mortgage_renegotiation_fee / self.months_repaid)
            self.table_of_monthly_costs.loc[i, 'down_payment'] = (
                    self.mortgage_calc.down_payment / self.months_repaid)

    def _calculate_total_cost_per_month(self):
        """
        spreading the down payment over the number of months and mortgage
        renegotiation fees.
        :return:
        """
        self.table_of_monthly_costs['total'] = (
                self.table_of_monthly_costs['mortgage'] + self.table_of_monthly_costs[
            'renovation'] + self.table_of_monthly_costs['admin_fees'] +
                self.table_of_monthly_costs['vlt'] + self.table_of_monthly_costs[
                    'diluted_lump_sum'] + self.table_of_monthly_costs[
                    'mortgage_renegotiation_fee'] + self.table_of_monthly_costs[
                    'down_payment'])

    def get_total_cost_per_year(self):
        """
        just an yearly view of the total cost
        :return:
        """
        return round(self.table_of_monthly_costs['total'].max() * 12)

    def get_total_cost_living_in_mortgage(self):
        """
        Get the total cost of the mortgage
        :return:
        """
        return round(self.table_of_monthly_costs['total'].sum())

    def plot_total_cost_per_year_stacking(self):
        """
        Plot the total cost per year, stacked
        :return:
        """
        # Ensure 'year' column exists in the dataframe
        self.table_of_monthly_costs['year'] = (
                                                      self.table_of_monthly_costs.index // 12) + 1

        # Group by year and sum the costs
        yearly_costs = self.table_of_monthly_costs.groupby('year').sum()

        # Plot the stacked bar chart
        yearly_costs.plot(kind='bar', stacked=True)

        plt.title('Total Cost per Year (Stacked)')
        plt.xlabel('Year')
        plt.ylabel('Cost')
        plt.legend(title='Cost Categories')
        plt.show()

    def plot_mortgage_cost_per_month_five_years(self):
        """
        Plot the mortgage cost per month
        :return:
        """
        total_investment_over_60_months = self.table_of_monthly_costs['total'].sum()
        plt.figure(figsize=(10, 5))
        plt.plot(self.table_of_monthly_costs['total'].cumsum())
        # plt.axhline(total_investment_over_60_months, color='r', linestyle='--')
        plt.xlabel('Months')
        plt.ylabel('Cost')
        plt.legend(['Total cost', 'Total cost over 60 months'])
        plt.title('Total investment over 5 years')
        plt.show()

    def __str__(self):
        return self.table_of_monthly_costs.to_string()
