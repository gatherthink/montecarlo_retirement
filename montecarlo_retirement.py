import random
import numpy as np

# inputs

yearly_investment = 105000
years = 7
interest_rate = 0.0845
std_dev = 0.0760
initial_amount = 0

# simulate multiple scenarios
num_simulations = 20000
savings = np.zeros(num_simulations)
for i in range(num_simulations):
    total_savings = initial_amount
    for j in range(years):
        # generate a return for the year based on normal distribution
        year_return = random.normalvariate(interest_rate, std_dev)
        # calculate the return on the current year's investment
        investment_return = (total_savings + yearly_investment) * year_return
        # add the return on investment to the total savings
        total_savings += yearly_investment + investment_return
    savings[i] = total_savings

# calculate percentiles
percentiles = np.percentile(savings, [5, 50, 90])

# print results
print("Initial investment: $", initial_amount)
print("Yearly investment: $", yearly_investment)
print("Years: ", years)
print("Interest rate: {:.2f}%".format(interest_rate * 100))
print("Standard deviation: {:.2f}%".format(std_dev * 100))
print("5th percentile savings: ${:.2f}".format(percentiles[0]))
print("50th percentile savings: ${:.2f}".format(percentiles[1]))
print("90th percentile savings: ${:.2f}".format(percentiles[2]))
