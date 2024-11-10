# 🏭 Industrial Resource Allocation Optimizer

## 🌟 Project Overview
The **Industrial Resource Allocation Optimizer** is a solution designed to help businesses in the furniture industry optimize their production processes. By leveraging **Linear Programming** and the **PuLP** library, this tool calculates the optimal quantities of two products—chairs and tables—to maximize profits while considering constraints on available resources such as labor hours, wood, and steel. The tool is equipped with a simple and intuitive **Tkinter** user interface to facilitate easy input and visualization of the results.

This tool is ideal for manufacturers or production planners seeking to streamline their operations and make data-driven decisions to maximize profitability.

## 🔍 Problem Description

A company produces two types of products: **chairs** and **tables**, and has the following resource constraints:
- **Labor hours**: Limited total number of hours available for production.
- **Wood**: Limited quantity of wood available.
- **Steel**: Limited amount of steel available.

### Product Characteristics:
- **Chairs**:  
  - Require 2 hours of labor
  - Require 4 units of wood
  - Require 1 unit of steel
- **Tables**:  
  - Require 3 hours of labor
  - Require 6 units of wood
  - Require 3 units of steel

The goal is to determine how many **chairs** and **tables** should be produced to **maximize profit** while respecting the available resources.

## 📈 Linear Programming Model
The optimization problem can be expressed as:

Maximize:
\[
\text{Profit} = (\text{Profit per Chair} \times \text{Number of Chairs}) + (\text{Profit per Table} \times \text{Number of Tables})
\]

Subject to:
- Labor constraint: \( 2 \times \text{Chairs} + 3 \times \text{Tables} \leq \text{Available Labor Hours} \)
- Wood constraint: \( 4 \times \text{Chairs} + 6 \times \text{Tables} \leq \text{Available Wood} \)
- Steel constraint: \( 1 \times \text{Chairs} + 3 \times \text{Tables} \leq \text{Available Steel} \)

The solution provides the optimal production quantities for chairs and tables, as well as the total profit.

## 🛠️ Technologies Used
- **PuLP**: A Python library for Linear Programming, used to model and solve the optimization problem.
- **Tkinter**: A Python GUI library used to create the user interface for the tool.
- **Python**: The core programming language for the solution.

## 🎮 User Interface
The tool provides an easy-to-use GUI for entering the following input:
- **Profit per Chair**: The profit earned for each chair produced.
- **Profit per Table**: The profit earned for each table produced.
- **Labor Hours Available**: The total number of labor hours available for production.
- **Wood Available**: The total units of wood available for production.
- **Steel Available**: The total units of steel available for production.

Once the input is provided, the user clicks **"Solve"**, and the tool calculates the optimal number of chairs and tables to produce, along with the total profit.

## 🖥️ Code

```python
import pulp
import tkinter as tk
from tkinter import messagebox


def solve_production_plan():
    problem = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

    chairs = pulp.LpVariable("Chairs", lowBound=0, cat="Integer")
    tables = pulp.LpVariable("Tables", lowBound=0, cat="Integer")

    try:
        profit_per_chair = int(chair_profit_entry.get())
        profit_per_table = int(table_profit_entry.get())
        labor_hours_available = int(labor_entry.get())
        wood_available = int(wood_entry.get())
        steel_available = int(steel_entry.get())
    except:
        messagebox.showerror("Error", f"An error occurred: Invalid entry provided :(")

    problem += profit_per_chair * chairs + profit_per_table * tables

    problem += 2 * chairs + 3 * tables <= labor_hours_available
    problem += 4 * chairs + 6 * tables <= wood_available
    problem += chairs + 3 * tables <= steel_available

    problem.solve()
    optimal_chairs = pulp.value(chairs)
    optimal_tables = pulp.value(tables)
    total_profit = pulp.value(problem.objective)

    result_label.config(
        text=f"Number of chairs = {optimal_chairs}\nNumber of tables = {optimal_tables}\nTotal profit = ${total_profit}"
    )


# GUI setup
root = tk.Tk()
root.title("Production Planning Solver")

input_frame = tk.Frame(root)
input_frame.pack(padx=20, pady=20)

chair_profit_label = tk.Label(input_frame, text="Chair Profit:")
chair_profit_label.grid(row=0, column=0)
chair_profit_entry = tk.Entry(input_frame)
chair_profit_entry.grid(row=0, column=1)

table_profit_label = tk.Label(input_frame, text="Table Profit:")
table_profit_label.grid(row=1, column=0)
table_profit_entry = tk.Entry(input_frame)
table_profit_entry.grid(row=1, column=1)

labor_label = tk.Label(input_frame, text="Labor Hours Available:")
labor_label.grid(row=2, column=0)
labor_entry = tk.Entry(input_frame)
labor_entry.grid(row=2, column=1)

wood_label = tk.Label(input_frame, text="Wood Available:")
wood_label.grid(row=3, column=0)
wood_entry = tk.Entry(input_frame)
wood_entry.grid(row=3, column=1)

steel_label = tk.Label(input_frame, text="Steel Available:")
steel_label.grid(row=4, column=0)
steel_entry = tk.Entry(input_frame)
steel_entry.grid(row=4, column=1)

solve_button = tk.Button(root, text="Solve", command=solve_production_plan)
solve_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
```
