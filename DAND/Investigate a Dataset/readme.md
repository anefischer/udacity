## Review

* Pandas is a very handy and powerful python library for handling data frames and various tedious tasks as hand. [Link1](https://towardsdatascience.com/10-python-pandas-tricks-that-make-your-work-more-efficient-2e8e483808ba) [Link2](https://realpython.com/python-pandas-tricks/)
* [Boolean-Indexing](http://pandas.pydata.org/pandas-docs/stable/indexing.html#boolean-indexing)
* [Series.map](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.map.html)
* [Working-with-text-data](https://pandas.pydata.org/pandas-docs/stable/text.html)
* [Value-Counts](https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6) [more](https://chrisalbon.com/python/data_wrangling/pandas_dataframe_count_values/)
* [Indexing and Selecting data](https://pandas.pydata.org/pandas-docs/version/0.15/indexing.html)
* [Apply, Map](https://medium.com/@evelynli_30748/map-apply-applymap-with-the-lambda-function-5e83028be759)
* [Group-by](https://realpython.com/pandas-groupby/) [more](http://pandas.pydata.org/pandas-docs/stable/groupby.html)
* [markdown cell](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [Python graph gallery for matplotlib and seaborn](https://python-graph-gallery.com/)
* [Working with matplotlib](https://matplotlib.org/3.1.1/tutorials/introductory/sample_plots.html)
* [Here is a Reference link to plotting with categorical data](https://seaborn.pydata.org/tutorial/categorical.html)
* The first thing to do is to always [Identify the missing values](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.isnull.html) within the dataset. The few steps after this explain how to deal with the missing data
* If there are columns with a few rows of missing data the [Dropna method](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.dropna.html) could be used to drop the missing rows.
* If there are rows with missing data the [Fillna-method](http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.fillna.html) can be used instead of dropping them completely (This method can vary with the data and the project)
* The final option is if there are way too many missing values within a column it is best to drop the column completely using the [Drop-column-method](http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.drop.html)
* [Binning or Cutting](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.cut.html) Groups continuous or numerical values into smaller groups or ‘bins’
* [Pandas-Dummies](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.get_dummies.html) Transforms categorical data into dummy/indicator variables
