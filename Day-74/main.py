import pandas as pd
import matplotlib.pyplot as plt


# Data Exploration
colors = pd.read_csv('data/colors.csv')
colors.head()

colors['name'].nunique()

# Find the number of transparent colours where is_trans == 't' versus the number of opaque colours where is_trans == 'f'. See if you can accomplish this in two different ways.
colors.groupby('is_trans').count()
colors.is_trans.value_counts()

# Read the sets.csv data and take a look at the first and last couple of rows.
sets = pd.read_csv('data/sets.csv')
sets.head()

sets.tail()


# In which year were the first LEGO sets released and what were these sets called?
sets.sort_values('year').head()


# How many different sets did LEGO sell in their first year? How many types of LEGO products were on offer in the year the company started?
sets[sets['year'] == 1949]


# Find the top 5 LEGO sets with the most number of parts.
sets.sort_values('num_parts', ascending=False).head()


# Use .groupby() and .count() to show the number of LEGO sets released year-on-year. How do the number of sets released in 1955 compare to the number of sets released in 2019?
sets_by_year = sets.groupby('year').count()
sets_by_year['set_num'].head()

sets_by_year['set_num'].tail()

# Show the number of LEGO releases on a line chart using Matplotlib.
plt.plot(sets_by_year.index, sets_by_year.set_num)

plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])


# Aggregate Data with the Python .agg() Function
themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})

themes_by_year.rename(columns = {'theme_id':'nr_themes'}, inplace = True)
themes_by_year.head()

themes_by_year.tail()


# Plot the number of themes released by year on a line chart. Only include the full calendar years (i.e., exclude 2020 and 2021).
plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])


# Line Charts with Two Seperate Axes
# This looks terrible
plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])

ax1 = plt.gca() # get the axis
ax2 = ax1.twinx() # create another axis that shares the same x-axis

ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])


ax1 = plt.gca() # get the axis
ax2 = ax1.twinx() # create another axis that shares the same x-axis

ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])


ax1 = plt.gca()
ax2 = ax1.twinx()

# Add styling
ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='g')
ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], 'b')

ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Sets', color='green')
ax2.set_ylabel('Number of Themes', color='blue')


# Use the .groupby() and .agg() function together to figure out the average number of parts per set. How many parts did the average LEGO set released in 1954 compared to say, 2017?
parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})
parts_per_set.head()

parts_per_set.tail()


# Scatter Plots in Matplotlib
plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])


# Number of Sets per LEGO Theme
set_theme_count = sets["theme_id"].value_counts()
set_theme_count[:5]


# Database Schemas, Foreign Keys and Merging DataFrames
themes = pd.read_csv('data/themes.csv') # has the theme names!
themes.head()

themes[themes.name == 'Star Wars']

sets[sets.theme_id == 18]

sets[sets.theme_id == 209]


# Merging (i.e., Combining) DataFrames based on a Key
set_theme_count = pd.DataFrame({'id':set_theme_count.index,
                                'set_count':set_theme_count.values})
set_theme_count.head()


merged_df = pd.merge(set_theme_count, themes, on='id')
merged_df[:3]

# Basic, but unreadable
plt.bar(merged_df.name[:10], merged_df.set_count[:10])


plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)

plt.bar(merged_df.name[:10], merged_df.set_count[:10])
