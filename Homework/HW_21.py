# Налоговая система

"""
SSC - единый соц взнос
SP - % от прожиточного минимума
"""

class TaxOffice:

    def __init__(self):
        pass

    def formula_1(self, turnover, expenses):
        self.net_profit = turnover - expenses
        if self.net_profit < 1000000 / 4:
            self.SSC = 6500 * 0.22
            self.SP = 2600 * 0.1
            self.tax = self.SSC + self.SP
            print(
                'Entepreneur-1, your turnover: ', turnover, 'uah | your expenses: ', expenses, 'uah', '\n'
                'Your quarterly tax: ', self.tax, 'uah', '\n'
            )
        else:
            self.SSC = 6500 * 0.22
            self.SP = 2600 * 0.1
            self.profit = self.net_profit * 0.15
            self.tax = self.SSC + self.SP + self.profit
            print(
                'Entepreneur-1, your turnover: ', turnover, 'uah | your expenses: ', expenses, 'uah', '\n'
                'For exceeding the income limit, your quarterly tax is: ', self.tax, 'uah', '\n'
            )
            print('----------' * 3, '\n')

    def formula_2(self, turnover, expenses, workers):
        self.net_profit = turnover - expenses
        if self.net_profit < 5000000 / 4:
            self.SSC = 6500 * 0.22 * workers
            self.SP = 6500 * 0.2
            self.tax = self.SSC + self.SP
            print(
                'Entepreneur-2, your turnover: ', turnover, 'uah | your expenses: ', expenses, 'uah', '\n'
                'Your quarterly tax: ', self.tax, 'uah', '\n'
            )
        else:
            self.SSC = 6500 * 0.22 * workers
            self.SP = 2600 * 0.1
            self.profit = self.net_profit * 0.15
            self.tax = self.SSC + self.SP + self.profit
            print(
                'Entepreneur-2, your turnover: ', turnover, 'uah | your expenses: ', expenses, 'uah', '\n'
                'For exceeding the income limit, your quarterly tax is: ', self.tax, 'uah', '\n'
            )
            print('----------' * 3, '\n')

    def formula_3(self, turnover, expenses, workers):
        self.net_profit = turnover - expenses
        if self.net_profit < 7000000 / 4:
            self.SSC = 6500 * 0.22 * workers
            self.SP = self.net_profit * 0.05
            self.tax = self.SSC + self.SP
            print(
                'Entepreneur-3, your turnover: ', turnover, 'uah | your expenses: ', expenses, 'uah', '\n'
                'Your quarterly tax: ', self.tax, 'uah', '\n'
            )
        else:
            self.SSC = 6500 * 0.22 * workers
            self.SP = self.net_profit * 0.05
            self.profit = self.net_profit * 0.15
            self.tax = self.SSC + self.SP + self.profit
            print(
                'Entepreneur-3, your turnover: ', turnover, 'uah | your expenses: ', expenses, 'uah', '\n'
                'For exceeding the income limit, your quarterly tax is: ', self.tax, 'uah', '\n'
            )

class EmployerGroup1(TaxOffice):

    def __init__(self, turnover, expenses):
        self.turnover = turnover
        self.expenses = expenses

    def reporting(self):
        TaxOffice.formula_1(self, self.turnover, self.expenses)


class EmployerGroup2(TaxOffice):

    def __init__(self, turnover, expenses, workers):
        self.turnover = turnover
        self.expenses = expenses
        self.workers = workers

    def reporting(self):
        TaxOffice.formula_2(self, self.turnover, self.expenses, self.workers)


class EmployerGroup3(TaxOffice):

    def __init__(self, turnover, expenses, workers):
        self.turnover = turnover
        self.expenses = expenses
        self.workers = workers

    def reporting(self):
        TaxOffice.formula_3(self, self.turnover, self.expenses, self.workers)

# group 1
emp_1 = EmployerGroup1(50000, 15000)
emp_2 = EmployerGroup1(300000, 35000)
emp_1.reporting()
emp_2.reporting()
# group 2
emp_3 = EmployerGroup2(500000, 40000, 4)
emp_4 = EmployerGroup2(1500000, 130000, 8)
emp_3.reporting()
emp_4.reporting()
# group 3
emp_5 = EmployerGroup3(800000, 150000, 35)
emp_6 = EmployerGroup3(2500000, 400000, 98)
emp_5.reporting()
emp_6.reporting()