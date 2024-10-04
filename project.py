import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset= pd.read_csv(r"C:\Users\Tony\Downloads\cleaned.csv")

# To take a look at the first five rows we use the pandas function “ .head()”. 
print(dataset.head())

# Similarly “.tail()” returns the last five observations of the data set.
print(dataset.tail())

# To know the total number of rows and columns in the data set we use “.shape”
print(dataset.shape)

# to know the columns and their corresponding data types, along
# with finding whether they contain null values or not.
print(dataset.info())

# To get a better understanding of the dataset, we can also see the statistical summary of
# the dataset using the function “.describe()”.
# This includes count, mean, median (or 50th percentile) standard variation, min-max, and
# percentile values of columns as shown below.
print(dataset['rating'].describe())

# to see the number of unique users and items in the dataset
print(dataset.nunique())

# checking for missing value
print(dataset.isnull().sum())


# Finding Answers with the Data Using Visualizations

# what was the best year of sales
yearly_sales= dataset.groupby('year')['amount'].sum()

plt.figure(figsize=(10, 6))
plt.bar(yearly_sales.index, yearly_sales.values)
plt.title('year wise sales')
plt.xlabel('year')
plt.ylabel('total sales')
plt.tight_layout()
plt.show()

# We can see that the year 2015 to 2018 had the best sales.
# what was the best month of sales
dataset_2015_2018 = dataset[(dataset['year'] >= 2015) & (dataset['year']<= 2018)]
best_sales=dataset_2015_2018.groupby('month')['rating'].count()
plt.figure(figsize=(10, 6))
plt.bar(best_sales.index, best_sales.values)
plt.title('month wise sales')
plt.xlabel('month')
plt.xticks(best_sales.index)
plt.tight_layout()
plt.show()


# what brand sold the most in 2015 to 2018
dataset_2015_2018 = dataset[(dataset['year'] >= 2015) & (dataset['year']<= 2018)]
highest_selling_brand= dataset_2015_2018.groupby('brand')['amount'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.bar(highest_selling_brand.index, highest_selling_brand.values)
plt.title('top 10 selling brands in 2015-2018')
plt.xlabel('brand')
plt.ylabel('amount')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# What products sold the most in the three years 2016, 2017 & 2018
# Create subplots with 2 rows and 2 columns
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
# Plot for 2016
top_selling_2016 = dataset[dataset['year'] ==
2016].groupby('brand')['rating'].count().sort_values(ascending=False).head(10)
axs[0, 0].bar(top_selling_2016.index, top_selling_2016)
axs[0, 0].set_title('Top Selling Products in 2016')
axs[0, 0].tick_params(axis='x', rotation=45) # Rotate x-axis labels

# Plot for 2017
top_selling_2017 = dataset[dataset['year'] ==
2017].groupby('brand')['rating'].count().sort_values(ascending=False).head(10)
axs[0, 1].bar(top_selling_2017.index, top_selling_2017)
axs[0, 1].set_title('Top Selling Products in 2017')
axs[0, 1].tick_params(axis='x', rotation=45) # Rotate x-axis labels

# Plot for 2018
top_selling_2018 = dataset[dataset['year'] ==
2018].groupby('brand')['rating'].count().sort_values(ascending=False).head(10)
axs[1, 0].bar(top_selling_2018.index, top_selling_2018)
axs[1, 0].set_title('Top Selling Products in 2018')
axs[1, 0].tick_params(axis='x', rotation=45) # Rotate x-axis labels
# Hide the empty subplot
axs[1, 1].axis('off')

plt.tight_layout()
plt.show()


# What product by category sold the most between 2015 to 2018?
dataset2015_2018 = dataset[(dataset['year'] >= 2015) & (dataset['year']<= 2018)]
category_sales=dataset2015_2018.groupby('category')['amount'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 10))
plt.bar(category_sales.index, category_sales.values)
plt.title('top 10 selling categories in 2015-2018')
plt.xlabel('catefory')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# What product by brand name sold the least between 2015 to 2018?
dataset2015_2018 = dataset[(dataset['year'] >= 2015) & (dataset['year']<= 2018)]
product_by_brand=dataset2015_2018.groupby('brand')['amount'].sum().sort_values(ascending=True).head(10)
plt.figure(figsize=(10,6))
plt.bar(product_by_brand.index, product_by_brand.values)
plt.title('top 10 least selling brands in 2015-2018')
plt.xlabel('brand')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# What is the most rated brand name between 2015 to 2018?
dataset2015_2018 = dataset[(dataset['year'] >= 2015) & (dataset['year']<= 2018)]
brand_rating= dataset2015_2018.groupby('brand')['rating'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
plt.bar(brand_rating.index, brand_rating.values)
plt.title('10 most rating brand 2015 to 2018')
plt.xlabel('brand')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# category percentage sales
sales_percentage=dataset.groupby('category')['amount'].sum().sort_values(ascending=False).head(5)
plt.pie(sales_percentage, labels=sales_percentage.index, autopct='%1.1f%%', startangle=90)
plt.title('top 5 category sales percentage')
plt.show()


# brand wise sales percentage
brand_sales_percentage= dataset.groupby('brand')['rating'].count().sort_values(ascending=False).head(5)
plt.pie(brand_sales_percentage,labels=brand_sales_percentage.index, autopct='%1.1f%%', startangle=90)
plt.title('top 5 brand wise sales percentage')
plt.show()

# Gender wise customer distribution
gender_distribution = dataset['gender'].value_counts()
plt.pie(gender_distribution, labels=gender_distribution.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral'])
plt.title('Gender wise customer Distribution')
plt.show()



# Rating distribution
ratings = dataset['rating'].value_counts().sort_index()

plt.figure(figsize=(8, 6))
plt.bar(ratings.index, ratings.values, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])

plt.title('Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(np.arange(1, 6))  # Set x-ticks to show only the ratings 1-5

plt.tight_layout()
plt.show()
