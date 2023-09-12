import pandas as pd
import matplotlib.pyplot as plt

# Read the .csv file and store it in a Pandas dataframe
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

# Examine the first 5 rows and the last 5 rows of the of the dataframe
df.head()
df.tail()

# Check how many rows and how many columns there are. What are the dimensions of the dataframe?
df.shape

# Count the number of entries in each column of the dataframe
df.count()

# Calculate the total number of post per language. Which Programming language has had the highest total number of posts of all time?
df.groupby('TAG').sum()

# How many months of data exist per language? Which language had the fewest months with an entry?
df.groupby('TAG').count()

# Data Cleaning
df['DATE'][1]

df.DATE[1]
type(df['DATE'][1])
print(pd.to_datetime(df.DATE[1]))
type(pd.to_datetime(df.DATE[1]))

# Convert Entire Column
df.DATE = pd.to_datetime(df.DATE)
df.head()


# Data Manipulation
test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu'],
                        'Power': [100, 80, 25, 50, 99, 75, 5]})
test_df

pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
pivoted_df

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')

reshaped_df.shape

reshaped_df.columns

reshaped_df.head()

# Count the number of entries per programming language. Why might the number of entries be different?
reshaped_df.count()

reshaped_df.fillna(0, inplace=True)

reshaped_df.head()

reshaped_df.isna().values.any()


# Data Visualisaton with with Matplotlib
plt.plot(reshaped_df.index, reshaped_df.java)
# alternative way of selecting the column
# plt.plot(reshaped_df.index, reshaped_df['java'])

plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
plt.plot(reshaped_df.index, reshaped_df.java)

# Show two line (e.g. for Java and Python) on the same chart.
plt.figure(figsize=(16,10)) # make chart larger
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python)


plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# plot all languages using for loop
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column])


plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column],
             linewidth=3, label=reshaped_df[column].name)

plt.legend(fontsize=16)


# Smoothing out Time Series Data
# The window is number of observations that are averaged
roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)