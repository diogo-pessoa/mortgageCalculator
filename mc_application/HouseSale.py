class HouseSale:
    """
    when calculating the profit from the house sale (in the context of the of
    investment rates over the years. We also need to consider how much the monthly
    mortgage fee has paid of the debt. Normally about half of the monthly mortgage
    deducts from the debt, the other half is interest.

    """

    def __init__(self, sale_price, real_state_agent_commission_rate=0.01,
                 estimated_sales_costs=5000):
        self.sale_price = sale_price
        self.real_state_agent_commission = sale_price * real_state_agent_commission_rate
        self.solicitor_and_other_costs = estimated_sales_costs

    # TODO - calculate how much of mortgage paid is lost in  #  #  interest, calculate

    #  how much of the mortgage paid is lost in interest
    #  and how much is paid off the debt. This is important

    def get_return_from_sale(self):
        """
        Calculate the return from the house sale.
        :return: Return from the house sale.
        """
        return round(self.sale_price - self.real_state_agent_commission -
                self.solicitor_and_other_costs)
