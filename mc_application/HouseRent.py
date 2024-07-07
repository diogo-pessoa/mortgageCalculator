class HouseRent:

    def __init__(self, monthly_rent, years_renting, yearly_rate_increase=0.04):
        self.monthly_rent = monthly_rent
        self.yearly_rate_increase = yearly_rate_increase
        self.rate_increase_per_month = yearly_rate_increase / 12
        self.rent_period_months = years_renting * 12
        self.years_renting = years_renting
        self.current_rent = self.monthly_rent
        self.total_rent = 0
        self.calculate_total_rent()

    def apply_yearly_rate_increase(self):
        """
        Apply rent increase based on yearly rate increase
        :return: increase monthly rent
        """
        print(f"Current rent: {self.current_rent:.2f}")
        print(f"Applying yearly rate increase of {self.yearly_rate_increase:.2f}")
        self.current_rent += (self.current_rent * self.yearly_rate_increase)

    def get_yearly_rate_increase(self, current_rent, period_in_years=1):
        """
        Get yearly rate increase
        :return: yearly rate increase
        """
        current_rent += self.current_rent
        if period_in_years <= 1:
            return current_rent + current_rent * self.yearly_rate_increase
        while period_in_years > 0:
            current_rent += current_rent * self.yearly_rate_increase
            period_in_years -= 1
        return self.get_yearly_rate_increase(current_rent, period_in_years)

    def calculate_total_rent(self):
        """
        Calculate total rent for the period
        :return: total rent
        """
        total_rent = 0
        for i in range(0, self.years_renting):
            total_rent += self.current_rent * 12
            self.apply_yearly_rate_increase()
        self.total_rent = total_rent
