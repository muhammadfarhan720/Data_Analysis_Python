# Data_Analysis_Python
This repo contains some of the most critical projects I completed for mastering data cleaning, pre-processing and EDA analysis using python tools. Click the following hyperlinks to get the problems and the solution code provided in the Colab notebooks pages : 


[**Vectorized Data Cleaning Engine**](https://colab.research.google.com/drive/1XEe-KLOpyizrUyAQhd0xwOCU1A2-op0-#scrollTo=vZuVntpbrI2w)  

_Optimized for large datasets using Pandas:_  

   • `df.loc[]` + `median()` for outlier replacement  
   • Regex patterns (`r'(\d+\.\d+|\d+)'`) for numeric extraction  
   • `astype()` for dtype enforcement (int64/float64)  
   • Custom unit converters (F°→C°, hours→minutes)  
   • Categorical mapping via `replace()`  
   • Storage standardization (1TB = 1000GB)  
   • Statistical validation with `mean()`/`std()`/`median()`




[**Real Estate Market EDA Analysis**](https://colab.research.google.com/drive/1mTa3N2GlIrzPwT2Jyo6yukMLcc6nNjVo?usp=sharing)

_Production-grade data analysis workflow:_

   • **Data Handling**:  
     `pd.read_csv()` | `df.drop()` | `pd.concat()` | `groupby().transform()`  
   • **Cleaning**:  
     `fillna()` strategies | Sparse feature removal | Data type conversion (`astype()`)  
   • **Feature Engineering**:  
     `TotalSF = TotalBsmtSF + 1stFlrSF + 2ndFlrSF`  
   • **Correlation Analysis**:  
     `df.corr()` | Custom threshold filtering | `sns.heatmap()`  
   • **Visualization**:  
     - Distribution: `sns.distplot()` + `scipy.stats.probplot()`  
     - Bivariate: `sns.lmplot()`, `sns.jointplot()`, `sns.stripplot()`  
     - Multivariate: Bubble plots (`plt.scatter()`), Faceted plots (`sns.lmplot(col=)`)  
   • **Statistical Transformation**:  
     Log normalization (`np.log1p()`)  
   • **Insight Generation**:  
     - Identified 11 key pricing drivers  
     - Detected temporal vs. structural impact patterns  
      



[**API Data Processing Stack**](https://colab.research.google.com/drive/1WbvAvbjDIbOJUCdquefBw8aTsMGWEf2q?usp=sharing)


_Hands-on experience with:_

• **API Integration**:  
  `requests.get()` | `response.json()` | Nested JSON traversal  
• **Data Transformation**:  
  `datetime.fromisoformat()` | List comprehensions | `lambda` functions  
• **Analysis**:  
  Top-N filtering (`sorted()[0:N]`) | Set operations (`set()`) |  
  Time-series binning (day/night) | Relative scaling  
• **Visualization**:  
  `matplotlib` (`bar`, `plot`, `text`) | Annotated charts |  
  Multi-line plots | Large-format figures (`figsize`)  
• **Specialized Parsing**:  
  Wind speed extraction (`split()` + `isdigit()`) |  
  API pagination patterns  


# Python Data Structure & Object-Oriented Programming Projects

A curated collection of Python projects demonstrating expertise in **data structures**, **algorithms**, and **object-oriented programming**.  
Each project is a self-contained folder including source code and test cases.

---

## Projects

1. [**Leap Year & Roman Numeral Validator**](https://github.com/muhammadfarhan720/Data_Analysis_Python/tree/main/Numerical_Algorithms)  
   Algorithms for calendar leap year detection and Roman numeral validation.  
   **Skills:** `Conditionals`, `Loops`, `String Processing`

2. [**Command-Line Phonebook Database**](https://github.com/muhammadfarhan720/Data_Analysis_Python/tree/main/CLI_Dictionary)  
   Interactive dictionary-based contact manager.  
   **Skills:** `Dictionaries`, `CRUD Operations`, `Input Validation`

3. [**DNA Sequence Experiment Data Analysis**](https://github.com/muhammadfarhan720/Data_Analysis_Python/tree/main/DA_DNA)  
   CSV data loader and statistical analysis toolkit.  
   **Skills:** `File I/O`, `Lists`, `Dictionaries`, `Functions`

4. [**Rational Number Class**](https://github.com/muhammadfarhan720/Data_Analysis_Python/tree/main/OOP_Test_method)  
   Object-oriented implementation of rational number arithmetic.  
   **Skills:** `OOP`, `Classes`, `Method Design`
