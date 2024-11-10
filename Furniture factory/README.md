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
