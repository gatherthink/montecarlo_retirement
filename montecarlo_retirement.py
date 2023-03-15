import random
import numpy as np

# inputs

yearly_investment = 106500
years = 7
interest_rate = 0.025
std_dev = 0.075
initial_amount = 0

# simulate multiple scenarios
num_simulations = 50000
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
percentiles = np.percentile(savings, [10, 25, 50, 80])
average = (percentiles[0] + percentiles[1]+ percentiles[2]+percentiles[3]) / 4
pert = ((percentiles[0] - 20000) + (percentiles[2] *4) +percentiles[3]) / 6

# print results
print("Initial investment: $", initial_amount)
print("Yearly investment: $", yearly_investment)
print("Years: ", years)
print("Interest rate: {:.2f}%".format(interest_rate * 100))
print("Standard deviation: {:.2f}%".format(std_dev * 100))
print("10th percentile savings: ${:.2f}".format(percentiles[0]))
print("25th percentile savings: ${:.2f}".format(percentiles[1]))
print("50th percentile savings: ${:.2f}".format(percentiles[2]))
print("90th percentile savings: ${:.2f}".format(percentiles[3]))
print("Average:  ${:.2f}".format(average))
print("PERT:  ${:.2f}".format(pert))
print("estimated income:  ${:.2f}".format(pert * .04))
