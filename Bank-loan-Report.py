#!/usr/bin/env python
# coding: utf-8

# # IMPORTING THE LIBRARIES

# In[2]:


# Import the Libraries


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("E:\\DataAnalysis\\SQL PROJECTS\\Bank Loan Report\\financial_loan.csv")
data.head(10)  





# # INFORMATION ABOUT THE DATASET

# In[3]:


data.info()


# # GETTING THE ROWS AND COLUMNS

# In[4]:


data.shape


# # DESCRIBING THE DATASET WITH THE SUM AGG VALUES

# In[5]:


data.describe()


# # DIST. OF LOAN AMOUNT VS FREQUENCY 

# In[19]:


import matplotlib.pyplot as plt

# Plotting Loan Amount Distribution
plt.figure(figsize=(14, 6))
plt.hist(data['loan_amount'], bins=30, color='skyblue', edgecolor='black')
plt.bar_label(plt.gca().containers[0])
plt.title('Distribution of Loan Amounts')
plt.xlabel('Loan Amount')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# # LOAN PURPOSE COUNT VS PURPOSE

# In[7]:


# Plotting Loan Purpose Count
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
bars = data['purpose'].value_counts().plot(kind='bar', color='coral', edgecolor='black')
plt.title('Loan Purpose Count')
plt.xlabel('Purpose')
plt.ylabel('Number of Loans')
plt.xticks(rotation=45)

# Adding labels to each bar
for container in bars.containers:
    bars.bar_label(container, label_type='edge', padding=3, fmt='%d', color='black', fontsize=10)

plt.show()



# # LOAN STATUS DIST.

# In[8]:


# Plotting Loan Status Distribution
plt.figure(figsize=(8, 8))
data['loan_status'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99'])
plt.title('Loan Status Distribution')
plt.ylabel('')
plt.show()


# # LOAN STATUS DIST. VS GRADE

# In[9]:


import matplotlib.pyplot as plt

# Calculate the mean interest rate by grade
mean_interest_rate_by_grade = data.groupby('grade')['int_rate'].mean()

# Plot the bar chart
plt.figure(figsize=(12, 6))
bar = mean_interest_rate_by_grade.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average Interest Rate by Loan Grade')
plt.xlabel('Loan Grade')
plt.ylabel('Average Interest Rate (%)')

# Adding labels to each bar
for container in bar.containers:
    bar.bar_label(container, label_type='edge', padding=3, fmt='%.2f', color='red', fontsize=10)

plt.show()




# # ANNUAL INCOME VS HOME OWNERSHIP

# In[10]:


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.violinplot(x='home_ownership', y='annual_income', data=data, color='purple')
plt.title('Annual Income Distribution by Home Ownership')
plt.xlabel('Home Ownership')
plt.ylabel('Annual Income')
plt.yscale('log')  # Using log scale to handle outliers
plt.show()



# # DTI VS FREQUENCY

# In[18]:


import matplotlib.pyplot as plt

# Plotting DTI Distribution with custom bins (if needed)
plt.figure(figsize=(14, 6))
plt.hist(data['dti'], bins=30, color='teal', edgecolor='black')
plt.title('Distribution of Debt-to-Income Ratio (DTI)')
plt.xlabel('Debt-to-Income Ratio')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adding labels to each bin
for container in plt.gca().containers:
    plt.bar_label(container, fmt='%d', label_type='edge', fontsize=10)

plt.show()


# # LOAN AMT. VS TERM

# In[12]:


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.stripplot(x='term', y='loan_amount', data=data, color='orange', jitter=True, alpha=0.6)
plt.title('Loan Amount by Loan Term')
plt.xlabel('Loan Term')
plt.ylabel('Loan Amount')
plt.show()



# # AVG.LOAN AMOUNT VS PURPOSE

# In[14]:


import matplotlib.pyplot as plt

# Calculating the average loan amount by purpose
avg_loan_by_purpose = data.groupby('purpose')['loan_amount'].mean().sort_values()

# Plotting Average Loan Amount by Purpose
plt.figure(figsize=(12, 6))
bars = plt.bar(avg_loan_by_purpose.index, avg_loan_by_purpose, color='skyblue', edgecolor='black')
plt.title('Average Loan Amount by Purpose')
plt.xlabel('Purpose')
plt.ylabel('Average Loan Amount')
plt.xticks(rotation=45)

# Adding data labels
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 1000, 
             f'{bar.get_height():,.0f}', ha='center', color='black', fontweight='bold')

plt.show()


# # COUNT OF LOANS VS TERM

# In[16]:


# Counting loans by term
loan_count_by_term = data['term'].value_counts()

# Plotting Count of Loans by Term
plt.figure(figsize=(8, 6))
bars = plt.bar(loan_count_by_term.index, loan_count_by_term, color='coral', edgecolor='black')
plt.title('Count of Loans by Term')
plt.xlabel('Loan Term (Months)')
plt.ylabel('Number of Loans')

# Adding data labels
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 500, 
             f'{bar.get_height()}', ha='center', color='black', fontweight='bold')

plt.show()


# # MEDIAN INT.RATE VS EMP.LENGTH

# In[17]:


# Calculating median interest rate by employment length
median_int_rate_by_emp_length = data.groupby('emp_length')['int_rate'].median()

# Plotting Median Interest Rate by Employment Length
plt.figure(figsize=(10, 6))
plt.plot(median_int_rate_by_emp_length.index, median_int_rate_by_emp_length, marker='o', color='purple', linestyle='-')
plt.title('Median Interest Rate by Employment Length')
plt.xlabel('Employment Length (Years)')
plt.ylabel('Median Interest Rate (%)')

# Adding data labels
for i, value in enumerate(median_int_rate_by_emp_length):
    plt.text(median_int_rate_by_emp_length.index[i], value, f'{value:.1f}', 
             ha='center', va='bottom', fontweight='bold', color='purple')

plt.show()


# # CONCLUSION

# In[ ]:


1: Annual Income Distribution by Home Ownership:

The violin plot of annual income by home ownership category reveals that income distributions vary widely. 
Specifically, "Mortgage" and "Own" categories generally show higher income levels compared to "Rent," though 
there are outliers in each category. 
The use of a log scale provides better visualization of income variation across ownership types, 
reducing the impact of extreme values​


2: Average Interest Rate by Loan Grade:

Different loan grades correlate with varying average interest rates. 
Typically, higher loan grades (like A or B) tend to have lower interest rates,
indicating that loans associated with lower risk (or better credit) incur less interest.
This pattern emphasizes the lender's approach to assign lower rates to more creditworthy borrowers


3: Distribution of Loan Amounts:

The histogram of loan amounts suggests that a large number of loans are issued within a specific range, 
while higher loan amounts are less frequent. This distribution may reflect lending policies or borrower needs 
within a certain financial bracket​


4: Debt-to-Income (DTI) Ratio:

Analysis of the DTI ratio indicates most borrowers fall within a moderate DTI range, 
suggesting that borrowers are generally careful about managing their debt relative to income.
This also implies that lenders may target clients with manageable DTI levels, 
helping maintain loan performance​


5: Loan Purpose and Amount:

Average loan amounts vary significantly by purpose. For instance, 
loans taken out for "Home Improvement" or "Debt Consolidation" tend to be higher than those for smaller purposes, 
such as "Medical" expenses. This insight provides context into borrower intent and suggests
which needs drive larger loans​

