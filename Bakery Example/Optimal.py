# Import PuLP
from pulp import *

# Create a problem object
model = LpProblem("Maximize-Profit", LpMaximize)

# Create variables
A = LpVariable("A", lowBound=0)
B = LpVariable("B", lowBound=0)

# Add objective function
model += 20 * A + 40 * B

# Add constraints
model += 0.5 * A + 1 * B <= 30
model += 1 * A + 2.5 * B <= 60
model += 1 * A + 2 * B <= 22

# Solve the problem
model.solve()

# Print the status and the optimal values of the variables
print("Status:", LpStatus[model.status])
print("A =", int(A.varValue))
print("B =", int(B.varValue))