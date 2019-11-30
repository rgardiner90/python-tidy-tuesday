#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:39:52 2019

@author: richard_gardiner
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

student_loans = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2019/2019-11-26/loans.csv")



# Does the size of loans increase over years?



## Grouping the dataset
grouped_loans = student_loans["total"].groupby(student_loans["year"])

## Getting the grouped mean
new_df = grouped_loans.mean()

## Plotting
plt.plot(new_df)

## Ploting the whole thing in one step
plt.plot(student_loans["total"].groupby(student_loans["year"]).mean())
plt.title("Have Student Loans Increased Over \nthe Past Few Years?")
plt.xlabel("Year")
plt.ylabel("Average Loan Size")



# Which company has the largest number of loans?

# grouping and counting
companies = pd.DataFrame(student_loans["total"].groupby(student_loans["agency_name"]).count())

# creating a variable from the index
companies["company"] = companies.index

# sorting the data
companies = companies.sort_values("total", ascending = True)

# plotting
plt.barh(companies["company"], companies["total"])
plt.title("Which Company has the most loans?")
plt.xlabel("Number of Loans Serviced")
plt.ylabel("Company")



# Does Size of Loan correlate with garneshment
min(student_loans["wage_garnishments"])
max(student_loans["wage_garnishments"])

## getting correlation coefficients (pretty strong)
np.corrcoef(student_loans["total"], student_loans["wage_garnishments"])

## tighter correlation at the lower end (heteroskedasticity)
plt.scatter("total", "wage_garnishments", data = student_loans) 



# How to get a best fit line?

## Turns out that seaborn seems to be pretty well set up for this:

## library & dataset
import seaborn as sns
 
## use the function regplot to make a scatterplot
sns.regplot("total", "wage_garnishments", data = student_loans)

 