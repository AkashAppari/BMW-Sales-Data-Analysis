# BMW Worldwide Sales Analysis (2010-2024)

## Project Overview and Goals
This data analysis project examines BMW's global sales performance from 2010 to 2024, with the following objectives:
- Identify key market trends and regional performance patterns
- Analyze vehicle preferences across different markets
- Assess the growth of electric vehicles in BMW's portfolio
- Provide actionable insights for market strategy

## Dataset Overview
The BMW Worldwide Sales Records dataset contains:
- **Time Period**: January 2010 - December 2024
- **Geographic Scope**: All major markets worldwide
- **Key Variables**:
  - Sales volume by model
  - Regional distribution
  - Vehicle segment classification
  - Powertrain type (ICE, PHEV, BEV)
  - Monthly sales figures
  - Market-specific pricing
  - Vehicle specifications

## Data Preprocessing
### Cleaning Steps
1. **Missing Value Treatment**:
   - Filled missing regional data using market hierarchy
   - Interpolated missing monthly sales using seasonal patterns
   - Removed records with >50% missing values (< 0.1% of dataset)

2. **Data Quality Improvements**:
   - Standardized model names and classifications
   - Corrected date formatting inconsistencies
   - Removed duplicate entries (found in overlapping regional reports)
   - Validated sales figures against public financial reports

3. **Feature Engineering**:
   - Created market segment categories
   - Derived seasonal indices
   - Calculated year-over-year growth rates
   - Generated price segment classifications

## Key Analytical Findings
### Sales Performance
- **Top-Selling Models**:
  1. BMW X Series (X1, X3, X5, X6): ~35% of global sales
  2. 3 Series: ~24% of global sales
  3. 5 Series: ~20% of global sales

- **Regional Leaders**:
  1. Asia: ~30% market share
  2. North America: ~25% market share
  3. Europe: ~23% market share

### Market Trends
1. **Electric Vehicle Growth**:
   - Steady increase in EV & Hybrid sales since 2020
   - Higher adoption rates in European markets
   - Strong performance in urban areas

2. **Segment Evolution**:
   - SUV models dominate with ~35% market share
   - Premium segment represents ~40% of sales
   - Steady performance in sedan segment

3. **Vehicle Preferences**:
   - Growing demand for hybrid powertrains
   - Increased preference for premium features
   - Regional variations in powertrain choices

## Interactive Dashboards
### Planned Visualizations
The following visualizations will be created using Power BI:

1. **Sales Performance Dashboard**
   - Regional Sales Heat Map
   - Year-over-Year Growth Trends
   - Top Models by Region
   - Monthly Sales Patterns

2. **Product Mix Analysis**
   - Vehicle Segment Distribution
   - Powertrain Type Breakdown
   - Price Segment Analysis
   - Model Lifecycle Performance

3. **Market Insights Dashboard**
   - EV Adoption Rate by Region
   - Premium vs Entry Segment Trends
   - Regional Preferences Analysis
   - Customer Price Sensitivity

### Dashboard Creation Steps
1. **Data Preparation**:
   - Export processed dataset from `data/processed/BMW_Worldwide_Sales_Features.csv`
   - Create date table for time intelligence
   - Set up proper data relationships

2. **Power BI Setup**:
   - Install [Power BI Desktop](https://powerbi.microsoft.com/desktop)
   - Create new project: `dashboards/bmw_sales_analysis.pbix`
   - Import prepared dataset

3. **Development Process**:
   - Create calculated columns for metrics
   - Design individual visualization pages
   - Set up interactive filters
   - Add drill-through capabilities

The final dashboard will be added to the `dashboards/` directory upon completion.

## Business Implications & Recommendations
1. **Product Strategy**:
   - Expand electric vehicle lineup in European markets
   - Maintain strong SUV presence in North America
   - Develop market-specific trim levels for China

2. **Market Opportunities**:
   - Focus on tier-2 cities in emerging markets
   - Strengthen digital sales channels
   - Expand charging infrastructure partnerships

3. **Risk Mitigation**:
   - Diversify supply chain for EV components
   - Build inventory buffers for bestselling models
   - Enhance CPO program in mature markets

## Project Reproduction Guide
1. **Environment Setup**:
   ```bash
   git clone [repository-url]
   cd BMW-Sales-Data-Analysis
   pip install -r requirements.txt
   ```

2. **Data Processing**:
   - Run notebooks in sequence:
     1. `01_data_cleaning.ipynb`
     2. `02_eda.ipynb`
     3. `03_feature_engineering.ipynb`

3. **Viewing Results**:
   - Processed data in `data/processed/`
   - Visualizations in `dashboards/`
   - Analysis reports in `reports/`

## Data Source
The analysis is based on the BMW Worldwide Sales Records dataset (`data/raw/BMW_Worldwide_Sales_Records_2010_2024.csv`), which contains historical sales data. This dataset was created for educational and portfolio demonstration purposes.