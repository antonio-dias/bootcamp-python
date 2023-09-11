import pandas as pd

# Read the .csv File
df = pd.read_csv('salaries_by_college_major.csv')

print(df.head())


# Data Exploration and Data Cleaning

df.shape

df.columns

df.isna()

df.tail()

clean_df = df.dropna()
clean_df.tail()


# Accessing Columns and Individual Cells
clean_df['Starting Median Salary'].max()

clean_df['Starting Median Salary'].idxmax()

clean_df['Starting Median Salary'][43]

clean_df['Undergraduate Major'].loc[43]

clean_df['Undergraduate Major'][43]

clean_df.loc[43]

# Solution: Highest and Lowest Earning Degrees
print(clean_df['Mid-Career Median Salary'].max())
print(f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
clean_df['Undergraduate Major'][8]

print(clean_df['Starting Median Salary'].min())
clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()]

clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()]


# Sorting Values & Adding Columns: Majors with the Most Potential vs Lowest Risk

# clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
# clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()

low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()

# Solution: Degrees with the Highest Potential
highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

highest_spread = clean_df.sort_values('Spread', ascending=False)
highest_spread[['Undergraduate Major', 'Spread']].head()

highest_spread = clean_df.sort_values('Mid-Career Median Salary', ascending=False)
highest_spread[['Undergraduate Major', 'Mid-Career Median Salary']].head()


# Grouping and Pivoting Data with Pandas

clean_df.groupby('Group').count()

pd.options.display.float_format = '{:,.2f}'.format
clean_df.groupby('Group').mean()