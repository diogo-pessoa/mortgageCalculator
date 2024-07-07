class PassiveInvestmentCalc:
    def __init__(self, initial_investment, years, yearly_rate, monthly_investment=0):
        self.initial_investment = initial_investment
        self.monthly_investment = monthly_investment
        self.years = years
        self.months = years * 12
        self.yearly_rate = yearly_rate
        self.monthly_rate = yearly_rate / 12
        self.current_lump_sum = initial_investment

    def calculate(self):
        total_investment = self.initial_investment
        total_return = total_investment * ((1 + self.yearly_rate) ** self.years)
        return total_return

    def apply_monthly_rate_increase(self):
        """
        Apply the monthly rate increase to the current lump sum
        :return:
        """
        self.current_lump_sum += self.current_lump_sum * self.monthly_rate

    def apply_yearly_interest_over_period(self):
        for i in range(1, 12):
            self.apply_monthly_rate_increase()

    def lodge_lump_sum(self, lump_sum):
        self.current_lump_sum += lump_sum
