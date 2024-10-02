#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv("DiwaliSales.csv", encoding='ISO-8859-1')


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


df.drop(['Status','unnamed1'], axis =1, inplace =True)


# In[7]:


df.head()


# In[8]:


df.isnull().sum()


# In[9]:


df.shape


# In[10]:


df.dropna(inplace=True)


# In[11]:


df.shape


# In[12]:


# changing Data types


# In[13]:


df['Amount'] = df['Amount'].astype('int')
df['Amount'].dtype


# In[14]:


df.columns


# In[15]:


df.describe()


# In[16]:


# Now EDA


# 1. Total sales amount by gender
# 

# In[17]:


total_sales_by_gender = df.groupby('Gender')['Amount'].sum()
print(total_sales_by_gender)


# In[18]:


plt.figure(figsize=(8, 5))
total_sales_by_gender.plot(kind='bar', color=['blue', 'pink'])
plt.title('Total Sales by Gender')
plt.xlabel('Gender')
plt.ylabel('Total Sales Amount')

# Show the graph
plt.show()


# # Insight:
# The Female category (labeled as "F") has a significantly higher total sales amount, depicted by a taller blue bar.
# The Male category (labeled as "M") shows a comparatively lower total sales amount, represented by a shorter pink bar.

# In[19]:


# 2. Average order amount by age group


# In[20]:


total_sales_by_gender = df.groupby('Gender')['Amount'].sum()
print(total_sales_by_gender)


# In[21]:


Average_order_amount_by_age_group = df.groupby ('Age Group')['Amount'].mean()
print(Average_order_amount_by_age_group)


# In[22]:


plt.figure(figsize=(8,5))
Average_order_amount_by_age_group.plot(kind='bar',color=['green','red'])
plt.title('Average order amount by age group')
plt.xlabel('Age Group')
plt.ylabel('Average_order_amount')
plt.show()




# # Insight
# 
# 

# The average order amount increases with age.
# 
# The age group with the highest average order amount is 51-55.
# 
# 
# The age group with the lowest average order amount is 18-25.
# 
# There is a significant difference in the average order amount between the youngest and oldest age groups.
# 
# The average order amount for the age groups 36-45 and 46-50 is very similar.
# 
# Overall, the chart suggests that older customers tend to spend more on average than younger customers.

# In[75]:


# 3. Sales distribution by marital status


# In[76]:


sale_by_marital_status = df.groupby('Marital_Status')['Amount'].mean()
print(sale_by_marital_status)


# In[79]:


plt.figure(figsize=(8,5))
sale_by_marital_status.plot(kind='bar',color=['blue','yellow'])
plt.title('Marital_Status')
plt.xlabel('Marital_Status')
plt.ylabel('Amount')
plt.show()


# # Insight
# 
# 
# The average order amount is higher for married individuals than for single individuals.
# 
# The difference in average order amount between the two groups is significant.
# 
# The sample size for both groups appears to be relatively small, which could limit the generalizability of the findings.

# # 4. Sales by occupation
# 

# In[21]:


sale_by_occuption = df.groupby('Occupation')['Amount'].mean()

# Create a bar plot
plt.figure(figsize=(10, 6))
sale_by_occuption.plot(kind='bar', color='skyblue')

# Add labels and title
plt.title('Average Sales by Occupation')
plt.xlabel('Occupation')
plt.ylabel('Average Sale Amount')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()


# # Insight
# 
# 
# 
# The average sales amount varies significantly across different occupations.
# 
# The occupation with the highest average sales amount is Agriculture.
# 
# The occupation with the lowest average sales amount is Construction.
# 
# There is a clear gap between the top-earning occupations and the bottom-earning occupations.
# 
# The average sales amount for most occupations falls within a relatively narrow range.
# 

# # 5 Average order amount by occupation
# 

# In[23]:


avg_order_by_occupation = df.groupby('Occupation')['Amount'].mean()
print(avg_order_by_occupation)


# In[25]:


plt.figure(figsize=(8,5))
avg_order_by_occupation.plot(kind='bar',color =['yellow','cyan'])
plt.title('Average order amount by occupation')
plt.xlabel('Occupation')
plt.ylabel(' Average order amount by occupation')
plt.show()


# # Insight
# 
# 
# The average order amount varies significantly across different occupations.
# 
# The occupation with the highest average order amount is Agriculture.
# 
# The occupation with the lowest average order amount is Construction.
# 
# There is a clear gap between the top-earning occupations and the bottom-earning occupations.
# 
# The average order amount for most occupations falls within a relatively narrow range.

# # 6 Total orders by age Group

# In[27]:


orders_by_age_group = df.groupby('Age Group')['Orders'].sum()
print(orders_by_age_group)


# In[29]:


plt.figure(figsize=(8,5))
orders_by_age_group.plot(kind='bar',color =['yellow','cyan'])
plt.title('Total orders by age Group')
plt.xlabel('Age Group')
plt.ylabel('Total orders ')
plt.show()


# # # Insight
# 
# 
# 
# The total number of orders varies significantly across different age groups.
# 
# The age group with the highest total number of orders is 26-35.
# 
# The age group with the lowest total number of orders is 51-55.
# 
# There is a clear gap between the age group with the highest total number of orders and the age groups with the lowest total number of orders.
# 
# The total number of orders for most age groups falls within a relatively narrow range.

# # 7  Average amount spent by gender

# In[32]:


avg_amount_by_gender = df.groupby('Gender')['Amount'].mean()
print(avg_amount_by_gender)


# In[33]:


plt.figure(figsize=(8,5))
avg_amount_by_gender.plot(kind='bar',color=['green','red'])
plt.title('Average amount spent by gender')
plt.xlabel('Gender')
plt.ylabel('Average amount gender')
plt.show()


# # Insight
# 
# 
# The average amount spent is higher for males than for females.
# 
# The difference in average spending between the two groups is significant.
# 
# The sample size for both groups appears to be relatively small, which could limit the generalizability of the findings.

# # 8 Zone Wise total sales

# In[34]:


sales_by_zone = df.groupby('Zone')['Amount'].sum()
print(sales_by_zone)


# In[35]:


plt.figure(figsize=(8,5))
sales_by_zone.plot(kind='bar',color=['blue','red'])
plt.title('sales_by_zone')
plt.xlabel('Zone')
plt.ylabel('Amount')
plt.show()


# # Insight
# 
# The bar chart shows the total sales for each zone. The central zone has the highest sales, followed by the southern and northern zones. The eastern and western zones have the lowest sales.
# 
# Here are some additional insights:
# 
# The central zone has approximately 4 million in sales.
# 
# The southern zone has approximately 2.8 million in sales.
# 
# The northern zone has approximately 2.5 million in sales.
# 
# The eastern and western zones each have approximately 1 million in sales.
# 
# Overall, the central zone is the most successful in terms of sales.

# # 9 Correlation between age and amount spent
# 

# In[37]:


# Calculate the correlation
correlation_age_amount = df[['Age', 'Amount']].corr()
print(correlation_age_amount)

# Create a scatter plot with a regression line
plt.figure(figsize=(10, 6))
sns.regplot(x='Age', y='Amount', data=df, scatter_kws={'alpha':0.5}, line_kws={"color": "red"})

# Add labels and title
plt.title('Scatter Plot of Age vs. Amount')
plt.xlabel('Age')
plt.ylabel('Amount')

# Show the plot
plt.tight_layout()
plt.show()


# # Insight
# 
# 
# There is a weak positive correlation between age and amount spent. This means that as age increases, there is a slight tendency for people to spend more.
# 
# The correlation is not very strong. This indicates that there are other factors besides age that influence spending.
# 
# There is a significant amount of variability in the data. This means that there is a wide range of spending amounts for people of all ages.
# 
# The regression line shows the trend in the data. It indicates that the average amount spent increases slightly with age

# # 10 Average Order Amount By state

# In[39]:


avg_order_by_state =df.groupby ('State')['Amount'].mean()
print(avg_order_by_state)


# In[42]:


plt.figure(figsize=(8,5))
avg_order_by_state.plot(kind='bar', color=['green', 'red'])
plt.title('Average Order Amount By state')
plt.xlabel('State')
plt.ylabel('Amount')
plt.show()


# # Insight
# 
# 
# 
# The average order amount varies significantly across different states.
# 
# The state with the highest average order amount is Andhra Pradesh.
# 
# The state with the lowest average order amount is Haryana.
# 
# There is a clear gap between the state with the highest average order amount and the state with the lowest average order amount.
# 
# The average order amount for most states falls within a relatively narrow range.
# 

# #  11 Total Sales by product category

# In[26]:


sales_by_category = df.groupby('Product_Category')['Amount'].sum()
print(sales_by_category)


# In[27]:


plt.figure(figsize=(8,5))
sales_by_category.plot(kind='bar',color=['blue','red'])
plt.title('Total Sales by product category')
plt.xlabel('Product_Category')
plt.ylabel('Amount')
plt.show()


# # Insight
# 
# The average order amount varies significantly across different states.
# 
# The state with the highest average order amount is Andhra Pradesh.
# 
# The state with the lowest average order amount is Haryana.
# 
# There is a clear gap between the state with the highest average order amount and the state with the lowest average order amount.
# 
# The average order amount for most states falls within a relatively narrow range.

# # 12 Top 5 state by total sales amount

# In[32]:


top_states_by_sales =df.groupby('State')['Amount'].sum().sort_values(ascending=False).head(5)
print(top_states_by_sales)


# In[37]:


colors = ['skyblue', 'lightgreen', 'salmon', 'orange', 'purple']

# Create the horizontal bar plot
plt.figure(figsize=(10, 6))
top_states_by_sales.plot(kind='barh', color=colors)

# Add labels and title
plt.title('Top 5 States by Sales')
plt.xlabel('Total Sales Amount')
plt.ylabel('State')

# Show the plot
plt.tight_layout()
plt.show()


# # Insight
# 
# 
# Madhya Pradesh has the highest total sales amount.
# 
# Uttar Pradesh has the lowest total sales amount.
# 
# There is a clear gap between the state with the highest total sales amount and the state with the lowest total sales amount.
# 
# The total sales amount for most states falls within a relatively narrow range.
# 
# Overall, the chart suggests that certain states are associated with higher total sales amounts than others. However, more data is needed to understand the factors driving these differences.

# # 13 Sales Distribution by Marital status

# In[39]:


sales_by_marital_status =df.groupby('Marital_Status')['Amount'].sum()
print(sales_by_marital_status)


# In[42]:


plt.figure(figsize=(8,5))
sales_by_marital_status.plot(kind='bar',color=['red','green'])
plt.title(' Sales Distribution by Marital status')
plt.xlabel('Marital_Status')
plt.ylabel('Amount')
plt.show()


# # Insight
# 

# The total sales amount is higher for married individuals than for single individuals.
# 
# The difference in total sales amount between the two groups is significant.
# 
# The sample size for both groups appears to be relatively small, which could limit the generalizability of the findings.
# 
# Overall, the chart suggests that married customers tend to spend more than single customers. However, more data is needed to confirm this finding and to understand the reasons behind this difference.
# 

# In[45]:


top_occupations_orders = df.groupby('Occupation')['Orders'].sum().sort_values(ascending=False).head(5)
print(top_occupations_orders)

colors = ['green','salmon','orange','red','blue']
plt.figure(figsize=(10,6))
top_occupations_orders.plot(kind='barh',color =colors)
plt.title('top_occupations_orders')
plt.xlabel('Occupation')
plt.ylabel('Orders')
plt.tight_layout()
plt.show()



# # Insight
# 
# Govt has the highest total number of orders.
# 
# IT Sector has the lowest total number of orders.
# 
# There is a clear gap between the occupation with the highest total number of orders and the occupation with the lowest total number of orders.
# 
# The total number of orders for most occupations falls within a relatively narrow range.
# 
# Overall, the chart suggests that certain occupations are associated with a higher number of orders than others. However, more data is needed to understand the factors driving these differences

# # conclusion
# 
# # Overall Sales & Customer Behavior
# 
# Female shoppers dominate: Women significantly outspend men during Diwali, indicating they are a crucial target demographic for marketing and product offerings.
# 
# Spending increases with age: Older customers tend to have higher average order values. The 51-55 age group spends the most on average.
# 
# Married vs. Single: Married individuals have a slightly higher average purchase amount compared to single individuals.
# 
# Central Region Leads: The Central geographical zone records the highest total sales, suggesting a potentially larger customer base or higher spending power in that region.
# 
# # Product & Category Insights
# 
# Top Selling: The "Food" product category generates the most revenue, followed by "Clothing & Apparel" and "Electronics & Gadgets."
# 
# High-Value Categories: "Food," "Clothing & Apparel," and "Electronics & Gadgets" represent key areas for promotions and inventory management due to their high sales volume.
# 
# Consider exploring: Categories like "Office" and "Veterinary" have significantly lower sales, requiring investigation into the reasons (low demand, competition, etc.).
# 
# # Other Important Findings
# 
# Occupation Matters: Occupations like "Govt" and "IT Sector" have the highest order numbers, indicating potential marketing opportunities tailored to these professions. However, "Agriculture" has the highest average order amount, suggesting higher spending capacity in this segment.
# 
# State-wise Variations: Andhra Pradesh has the highest average order value among all states, while Uttar Pradesh leads in total sales amount. These state-specific trends can inform targeted marketing campaigns.
# 
# 
# Weak Age-Spending Correlation: While there's a slight positive correlation between a customer's age and how much they spend, it's not a strong predictor. Other factors likely play a more significant role.
# 
# # Recommendations & Next Steps
# 
# Targeted Marketing: Develop specific campaigns for high-value customer segments (women, older demographics, Central region residents, and professions like "Govt" and "IT").
# 
# Product Focus: Ensure sufficient inventory and attractive promotions for top-selling product categories. Explore ways to improve sales in underperforming categories.
# 
# Regional Strategies: Capitalize on the Central region's strong sales. Consider regional-specific promotions or product offerings for states with high average order values like Andhra Pradesh.
# 
# Deeper Analysis: Investigate the drivers behind high order numbers from "Govt" and "IT Sector" professions. Explore factors influencing spending habits beyond just age.
# 
# By leveraging these insights and recommendations, businesses can optimize their Diwali sales strategies to maximize revenue and customer engagement.
# 
#                                                                                                              
# 
# 
# 

# In[ ]:




