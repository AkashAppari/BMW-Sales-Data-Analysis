# BMW Sales Data Analysis — Portfolio Project

## 📊 Project Overview

This project demonstrates fundamental data analysis skills through a comprehensive analysis of BMW's worldwide sales data from 2010-2024. Using Python, pandas, and data visualization tools, I explore sales trends, market segments, and the company's transition to electric vehicles.

**Key Question:** How did BMW successfully transition to electric vehicles while maintaining its luxury brand positioning?

---

## 🎯 Skills Demonstrated

This portfolio project showcases the following data analysis skills:

### Technical Skills
- **Data Cleaning**: Handling missing values, removing duplicates, data type conversions
- **Data Manipulation**: Using pandas for filtering, grouping, aggregating, and transforming data
- **Exploratory Data Analysis (EDA)**: Statistical summaries, trend analysis, pattern identification
- **Data Visualization**: Creating clear, professional charts using matplotlib and seaborn
- **Feature Engineering**: Creating new variables from existing data (market segments, categories)
- **Statistical Analysis**: Calculating correlations, percentages, growth rates
- **Business Intelligence**: Translating data insights into actionable business recommendations

### Soft Skills
- **Problem-Solving**: Breaking down complex business questions into analyzable components
- **Communication**: Presenting findings through visualizations and clear explanations
- **Attention to Detail**: Ensuring data quality and accuracy throughout the analysis
- **Business Acumen**: Understanding what metrics matter and why

---

## 📖 The Story

Through 15 years of sales data, this analysis reveals:

1. **Successful Electric Transition**: BMW achieved 50%+ green vehicle adoption (up from <5% in 2010)
2. **Strong Brand Loyalty**: Near-zero price-sales correlation shows customers buy for brand value, not price
3. **Balanced Global Presence**: Unusual regional distribution (16-17% each) suggests strong global strategy
4. **Growth Opportunity**: Entry segment drives 45.8% of volume—the next frontier for expansion

---

## 🔍 Key Findings

### 1. Electric Vehicle Success
- **50.4% of sales** are now electric or hybrid vehicles
- Reached 50% tipping point around 2018-2019
- **10x transformation** from 2010 levels

### 2. Brand Strength
- **Price-sales correlation: 0.0** (near zero)
- Customers buy for brand value, not price
- Ideal scenario for a luxury brand

### 3. Regional Balance
- All regions maintain **16-17% market share** each
- Most global brands have 1-2 dominant markets (40-60%)
- Shows exceptional global strategy execution

### 4. Market Segments
- **Entry segment**: 45.8% of volume (growth engine)
- **Premium segment**: 27.1% (core positioning)
- **Performance segment**: 17.8% (brand halo)
- **Ultra-Luxury segment**: 9.3% (highest margins)

---

## 📊 Visualizations

The project includes 5 key visualizations:

1. **Sales Trends Over Time** - Shows BMW's sales trajectory from 2010-2024
2. **Regional Performance** - Demonstrates balanced global distribution
3. **Market Segment Distribution** - Reveals which segments drive volume
4. **Green Vehicle Adoption** - Tracks the electric transition over time
5. **Vehicle Type Performance** - Shows preferences across SUV, Sedan, etc.

All visualizations are saved in the `dashboards/` folder.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Jupyter Notebook (comes with Anaconda)

### Installation Steps

1. **Download the project**
   ```bash
   git clone github.com/AkashAppari/BMW-Sales-Data-Analysis
   cd BMW-Sales-Data-Analysis
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the dataset**
   - Visit: [Kaggle Dataset](https://www.kaggle.com/datasets/ahmadrazakashif/bmw-worldwide-sales-records-20102024)
   - Download `BMW_Worldwide_Sales_Records_2010_2024.csv`
   - Place it in the `data/raw/` folder

5. **Run the analysis**
   ```bash
   jupyter notebook notebooks/portfolio_summary.ipynb
   ```
   Then run all cells (Cell → Run All)

---

## 📁 Project Structure

```
BMW-Sales-Data-Analysis/
├── README.md                          # Project overview (this file)
├── requirements.txt                   # Python package dependencies
├── data/
│   ├── raw/                          # Original dataset (download from Kaggle)
│   └── processed/                    # Cleaned and processed data
├── notebooks/
│   ├── 01_data_cleaning.ipynb        # Step 1: Clean the raw data
│   ├── 02_eda.ipynb                  # Step 2: Exploratory data analysis
│   ├── 03_feature_engineering.ipynb  # Step 3: Create new features
│   ├── 04_forecasting.ipynb          # Step 4: Sales forecasting (optional)
│   └── portfolio_summary.ipynb       # ⭐ Main analysis notebook
└── dashboards/
    └── *.png                         # Generated visualizations
```

**Recommended Reading Order:**
1. Start with `portfolio_summary.ipynb` for the complete story
2. Review `01_data_cleaning.ipynb` to see data preparation
3. Check `02_eda.ipynb` for exploratory analysis techniques
4. Explore `03_feature_engineering.ipynb` for feature creation methods

---

## 💡 Business Recommendations

Based on the analysis:

1. **Focus on Entry Segment** - Drives 45.8% of volume, biggest growth opportunity
2. **Leverage Brand Loyalty** - Price doesn't drive sales, focus on brand value
3. **Accelerate EV Expansion** - Build on 50%+ green vehicle momentum
4. **Maintain Global Balance** - Current regional strategy is working well

---

## 🛠️ Tools & Technologies

- **Python 3.8+** - Programming language
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computations
- **matplotlib** - Data visualization
- **seaborn** - Statistical visualizations
- **Jupyter Notebook** - Interactive analysis environment

---

## 📈 Dataset Information

- **Source**: [Kaggle - BMW Worldwide Sales Records](https://www.kaggle.com/datasets/ahmadrazakashif/bmw-worldwide-sales-records-20102024)
- **Size**: 50,000 records
- **Time Period**: 2010-2024 (15 years)
- **Features**: Model, Year, Region, Fuel Type, Price, Sales Volume, etc.

---

## 📝 What I Learned

This project helped me practice:
- Working with real-world business data
- Cleaning and preparing data for analysis
- Creating meaningful visualizations
- Identifying trends and patterns
- Communicating insights clearly
- Thinking about business implications

---

## 🔗 Contact & Portfolio

This is a portfolio project demonstrating data analysis capabilities. For questions or feedback, please reach out through my portfolio.

---

*Project completed: 15 years of data, 50,000 records analyzed, 5 key visualizations created*
