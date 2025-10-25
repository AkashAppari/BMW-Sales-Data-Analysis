# BMW Worldwide Sales Data Analysis (2010-2024)

**Data Analysis Portfolio Project**

A comprehensive analysis of BMW's global sales performance spanning 15 years, demonstrating data cleaning, exploratory analysis, feature engineering, and business intelligence skills.

---

## 📊 Project Highlights

- **253+ million units** analyzed across 50,000 records
- **6 regions** and **11 BMW models** tracked over 15 years
- **50%+ green vehicle adoption** showing BMW's EV transition
- **Premium segment leads** with 27% market share
- **Asia** dominates regional sales, followed by Europe and North America

---

## 🎯 Project Objectives

- Clean and prepare raw sales data for analysis
- Uncover sales trends across regions, market segments, and vehicle types
- Engineer features for market segmentation and customer insights
- Create actionable visualizations and business recommendations


## 📁 Dataset

- **Source**: BMW worldwide sales records (2010-2024)
- **Size**: 50,000 records with 30+ features
- **Scope**: Multiple regions, models, fuel types, and market segments
- **Raw data**: `data/raw/BMW_Worldwide_Sales_Records_2010_2024.csv`
- **Processed data**: `data/processed/` (cleaned and feature-engineered versions)

---

## 🔍 Key Insights

### Market Performance
- **Top Region**: Asia leads with the highest total sales volume
- **Top Model**: 7 Series is the best-performing model overall
- **Average Price**: $75,035 across all vehicles

### Green Vehicle Transition
- **50.4%** of sales are now electric or hybrid vehicles
- Clear acceleration in EV adoption from 2018 onwards
- Europe and North America lead in green vehicle preference

### Market Segmentation
- **Entry Segment**: 45.8% (mass market appeal)
- **Premium**: 27.0% (core BMW positioning)
- **Performance**: 17.8% (M-series and sport models)
- **Ultra-Luxury**: 9.4% (7 Series and high-end variants)

### Vehicle Type Trends
- **SUVs** show strongest growth trajectory
- **Sedans** remain steady as core product line
- **Electric vehicles** gaining market share rapidly

---

## 📊 Visualizations

### Sales Trends Over Time
![Sales Trends](dashboards/sales_trends.png)
*BMW's global sales have remained relatively stable with a peak in 2022, showing resilience across economic cycles.*

### Regional Performance
![Regional Sales](dashboards/regional_sales.png)
*Asia, Europe, and North America are the three powerhouse markets for BMW worldwide.*

### Market Segment Distribution
![Market Segments](dashboards/market_segments.png)
*Entry segment dominates volume, but Premium and Performance segments drive brand value.*

### Green Vehicle Adoption
![Green Vehicle Adoption](dashboards/green_vehicle_adoption.png)
*Dramatic shift toward electric and hybrid vehicles, especially post-2016.*

### Vehicle Type Performance
![Vehicle Type Trends](dashboards/vehicle_type_trends.png)
*SUVs lead in absolute volume, with steady performance across all vehicle types.*

---

## 🛠️ Methods & Workflow

1. **Data Cleaning** (`notebooks/01_data_cleaning.ipynb`)
   - Load raw CSV files
   - Handle missing values (median for numeric, mode for categorical)
   - Remove duplicates
   - Normalize column names and data types
   - **Output**: `data/processed/BMW_Worldwide_Sales_Cleaned.csv`

2. **Exploratory Data Analysis** (`notebooks/02_eda.ipynb`)
   - Univariate and multivariate analysis
   - Correlation analysis
   - Seasonal and regional trend identification
   - Price-volume relationships
   - Initial visualization of key patterns

3. **Feature Engineering** (`notebooks/03_feature_engineering.ipynb`)
   - Create price categories (Budget → Luxury)
   - Define market segments (Entry, Premium, Performance, Ultra-Luxury)
   - Calculate vehicle age and engine power categories
   - Generate green vehicle indicators
   - Compute market share and performance metrics
   - **Output**: `data/processed/BMW_Worldwide_Sales_Features.csv`

4. **Portfolio Summary** (`notebooks/portfolio_summary.ipynb`)
   - Executive-level KPIs and metrics
   - Key visualizations for presentation
   - Business insights and recommendations
   - Export charts to `dashboards/` folder

---

## 💼 Business Recommendations

**Strategic Priorities:**
1. **Accelerate EV Portfolio**: Expand electric offerings in SUV segment to capture growing demand
2. **Regional Customization**: Tailor product mix (SUVs for North America, premium sedans for Europe)
3. **Premium Focus**: Continue investing in premium/ultra-luxury segments for margin optimization
4. **Emerging Markets**: Increase entry-level model presence in high-growth regions

**Data-Driven Operations:**
- Use predictive analytics for demand forecasting and inventory optimization
- Develop targeted marketing based on regional vehicle type preferences
- Monitor market share trends by segment to identify competitive threats

---

## 🚀 How to Run

### Prerequisites
```bash
# Python 3.8+ required
python --version
```

### Setup

1. **Clone or download this repository**

2. **Create a virtual environment** (recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate  # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Running the Analysis

**Option 1: Portfolio Summary (Quick Start)**
```bash
jupyter notebook notebooks/portfolio_summary.ipynb
```
Run all cells to see the complete analysis with KPIs, visualizations, and insights.

**Option 2: Full Pipeline (Step-by-Step)**
```bash
jupyter notebook
# Then run notebooks in order:
# 1. 01_data_cleaning.ipynb
# 2. 02_eda.ipynb
# 3. 03_feature_engineering.ipynb
# 4. portfolio_summary.ipynb
```

### Generated Outputs
- **Cleaned data**: `data/processed/BMW_Worldwide_Sales_Cleaned.csv`
- **Feature-engineered data**: `data/processed/BMW_Worldwide_Sales_Features.csv`
- **Visualizations**: `dashboards/*.png` (5 key charts)

---

## 📦 Dependencies

See `requirements.txt` for exact versions. Core packages:
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **matplotlib** - Data visualization
- **seaborn** - Statistical visualization
- **scikit-learn** - Feature engineering and machine learning utilities
- **jupyter** - Interactive notebooks

---

## 📂 Project Structure

```
BMW-Sales-Data-Analysis/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── data/
│   ├── raw/                          # Original datasets
│   │   └── BMW_Worldwide_Sales_Records_2010_2024.csv
│   └── processed/                    # Cleaned and feature-engineered data
│       ├── BMW_Worldwide_Sales_Cleaned.csv
│       └── BMW_Worldwide_Sales_Features.csv
├── notebooks/
│   ├── 01_data_cleaning.ipynb        # Data cleaning pipeline
│   ├── 02_eda.ipynb                  # Exploratory analysis
│   ├── 03_feature_engineering.ipynb  # Feature creation
│   └── portfolio_summary.ipynb       # Executive summary notebook
├── dashboards/
│   ├── sales_trends.png              # Global sales over time
│   ├── regional_sales.png            # Regional performance
│   ├── market_segments.png           # Segment distribution
│   ├── green_vehicle_adoption.png    # EV/Hybrid trends
│   └── vehicle_type_trends.png       # Vehicle type performance
├── scripts/
│   ├── data_cleaning.py              # Reusable cleaning functions
│   ├── data_analysis.py              # Analysis utilities
│   └── visualization.py              # Plotting helpers
└── reports/
    └── project_summary.md            # Detailed project documentation
```

---

## 🎓 Skills Demonstrated

This project showcases:
- **Data Cleaning**: Handling missing values, duplicates, data type conversions
- **Exploratory Data Analysis**: Statistical analysis, correlation studies, trend identification
- **Feature Engineering**: Creating derived variables, segmentation, metric calculation
- **Data Visualization**: Clear, professional charts using matplotlib and seaborn
- **Business Intelligence**: Translating data insights into actionable recommendations
- **Python Programming**: Efficient use of pandas, numpy, and scikit-learn
- **Documentation**: Well-structured notebooks with markdown explanations

---

## 🔗 Related Files

- **Detailed Report**: See `reports/project_summary.md` for comprehensive analysis documentation
- **Notebooks**: All analysis notebooks in `notebooks/` folder
- **Visualizations**: High-resolution charts in `dashboards/` folder
````