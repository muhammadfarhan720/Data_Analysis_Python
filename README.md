# 📊 Data Analysis Projects with Python

A collection of my most critical projects from **Computation for Data Sciences** course for mastering **data cleaning**, **pre-processing**, and **EDA** using Python tools.  
Click the **blue text hyperlinks** below to view problems and solution code in **Google Colab**.

---

## 1️⃣ [Vectorized Data Cleaning Engine](https://colab.research.google.com/drive/1XEe-KLOpyizrUyAQhd0xwOCU1A2-op0-#scrollTo=vZuVntpbrI2w)

**Core Skills:** `Pandas`, `Vectorized Operations`, `Regex`, `Data Validation`

- **Vectorized Cleaning:**  
  `df.loc[]` + `median()` outlier replacement | `str.extract()` for text parsing  
- **Unit Conversion:**  
  Custom `apply()` functions for time, temperature, storage  
- **Categorical Standardization:**  
  `str.replace()` with regex | Dictionary mapping  
- **Data Type Enforcement:**  
  `astype(int64/float64)` | Column-specific casting  
- **Data Validation:**  
  Statistical verification (`mean()`, `std()`, `median()`, conditional counts)  
- **Regex Processing:**  
  `r'(\d+\.\d+|\d+)'` numeric extraction | Case-insensitive matching  

---

## 2️⃣ [Real Estate Market EDA Analysis](https://colab.research.google.com/drive/1mTa3N2GlIrzPwT2Jyo6yukMLcc6nNjVo?usp=sharing)

**Core Skills:** `EDA`, `Data Cleaning`, `Feature Engineering`, `Seaborn`, `Matplotlib`

- **Data Handling:**  
  `pd.read_csv()` | `df.drop()` | `pd.concat()` | `groupby().transform()`  
- **Cleaning:**  
  `fillna()` strategies | Sparse feature removal | Data type conversion (`astype()`)  
- **Feature Engineering:**  
  `TotalSF = TotalBsmtSF + 1stFlrSF + 2ndFlrSF`  
- **Correlation Analysis:**  
  `df.corr()` | Custom threshold filtering | `sns.heatmap()`  
- **Visualization:**  
  - Distribution: `sns.distplot()` + `scipy.stats.probplot()`  
  - Bivariate: `sns.lmplot()`, `sns.jointplot()`, `sns.stripplot()`  
  - Multivariate: Bubble plots (`plt.scatter()`), Faceted plots (`sns.lmplot(col=)`)  
- **Statistical Transformation:**  
  Log normalization (`np.log1p()`)  
- **Insight Generation:**  
  - Identified 11 key pricing drivers  
  - Detected temporal vs. structural impact patterns  

---

## 3️⃣ [API Data Processing Stack](https://colab.research.google.com/drive/1WbvAvbjDIbOJUCdquefBw8aTsMGWEf2q?usp=sharing)

**Core Skills:** `API Integration`, `JSON Parsing`, `Data Transformation`, `Visualization`

- **API Integration:**  
  `requests.get()` | `response.json()` | Nested JSON traversal  
- **Data Transformation:**  
  `datetime.fromisoformat()` | List comprehensions | `lambda` functions  
- **Analysis:**  
  Top-N filtering (`sorted()[0:N]`) | Set operations (`set()`) |  
  Time-series binning (day/night) | Relative scaling  
- **Visualization:**  
  `matplotlib` (`bar`, `plot`, `text`) | Annotated charts |  
  Multi-line plots | Large-format figures (`figsize`)  
- **Specialized Parsing:**  
  Wind speed extraction (`split()` + `isdigit()`) | API pagination patterns  

---

# 💻 Python Data Structure & Object-Oriented Programming Projects

A curated collection of my Python projects from **Computation for Data Sciences** course demonstrating experience in **data structures**, **algorithms**, and **OOP**.  
Each project includes self-contained source code and test cases.

---

## Projects

1. [**Leap Year & Roman Numeral Validator**](https://github.com/muhammadfarhan720/Data_Analysis_Python/tree/main/Numerical_Algorithms)  
   **Skills:** `Conditionals`, `Loops`, `String Processing`  
   Algorithms for leap year detection and Roman numeral validation.

2. [**Command-Line Phonebook Database**](https://github.com/muhammadfarhan720/Data_Analysis_Python/tree/main/CLI_Dictionary)  
   **Skills:** `Dictionaries`, `CRUD Operations`, `Input Validation`  
   Interactive dictionary-based contact manager.

3. [**DNA Sequence Experiment Data Analysis**](https://github.com/muhammadfarhan720/Data_Analysis_Python/tree/main/DA_DNA)  
   **Skills:** `File I/O`, `Lists`, `Dictionaries`, `Functions`  
   CSV data loader and statistical analysis toolkit.

4. [**Rational Number Class**](https://github.com/muhammadfarhan720/Data_Analysis_Python/tree/main/OOP_Test_method)  
   **Skills:** `OOP`, `Classes`, `Method Design`  
   Object-oriented implementation of rational number arithmetic.

---
