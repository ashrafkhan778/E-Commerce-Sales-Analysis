# E-Commerce-Sales-Analysis

# Overview
This project performs an exploratory data analysis (EDA) on an e-commerce sales dataset, specifically focusing on sales during the Diwali season. The analysis covers various aspects of the dataset, including cleaning, visualizations, and extracting meaningful insights using Python libraries such as pandas, numpy, matplotlib, and seaborn.

# Dataset
The dataset used in this project is DiwaliSales.csv, which contains sales records for an e-commerce platform during Diwali. Key attributes in the dataset include customer details, product information, sales figures, and transactional data.

# Dataset Features:
Customer demographics
Product details
Sales amount
Discounts and offers

# Libraries Used


Pandas: For data manipulation and analysis.


NumPy: For numerical computations.


Matplotlib and Seaborn: For data visualization.


# Dataset Information


The dataset is a CSV file containing sales data with the following key columns:

User_ID: Unique customer identifier.


Cust_name: Customer name.


Product_ID: Identifier for products sold.


Gender: Gender of the customer.


Age Group: Customer age group.


State and Zone: Location of the customer.


Occupation: Customer's profession.


Product_Category: Category of the purchased product.


Orders: Number of items ordered.


Amount: Total amount spent.


# Steps in Analysis
1.Data Loading: Load the dataset from a CSV file using Pandas.

2.Data Cleaning: Drop unnecessary columns (Status, Unnamed) and handle missing values in the Amount column.


3.Data Type Conversion: Convert the Amount column to integer type for analysis.


4.Descriptive Statistics: Generate summaries of the data using Pandas describe() function.

# Key Insights
1. Total Sales by Gender

Insight: Female customers contributed more to total sales than male customers.

2. Average Order Amount by Age Group
Insight: The highest average order amount comes from the 51-55 age group.

3. Sales Distribution by Marital Status
Insight: Married individuals tend to spend more on average than singles.

4. Sales by Occupation
Insight: Customers in agriculture spend the most, while those in construction spend the least.

5. Zone-wise Sales
Insight: The Central zone shows the highest sales, followed by Southern and Northern zones.

6. Correlation between Age and Amount Spent
Insight: There is a weak positive correlation between age and the amount spent.

7. Total Orders by Age Group
Insight: Customers aged 26-35 placed the highest number of orders.

# Visualizations
The analysis includes several visualizations such as:

Bar charts showing sales distribution by gender, occupation, and zone.

Scatter plots with regression lines to show correlations.

Horizontal bar charts for top states by sales and top occupations by orders.

How to Run
1. Install necessary libraries
pip install pandas numpy matplotlib seaborn

2.Run the Jupyter notebook or Python script:
python e-commerce_sales_analysis.py

3.Ensure the dataset DiwaliSales.csv is in the same directory as the script.

# Future Improvements
Add more data features to explore additional sales trends.

Implement predictive models for future sales forecasting.

Analyze seasonal trends and discounts impact on sales.

# Contact
For any queries or suggestions, feel free to contact [ashraf.kmcu@gmail.com].









