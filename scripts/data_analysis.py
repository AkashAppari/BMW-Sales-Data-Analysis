"""
data_analysis.py

Core functions for analyzing BMW sales data, including:
- Market segment analysis
- Regional performance metrics
- Time series calculations
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple


class DataAnalysisError(Exception):
    """Custom exception for data analysis issues."""
    pass


def _ensure_columns(df: pd.DataFrame, required: List[str]) -> None:
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise DataAnalysisError(f"Missing required columns: {missing}")


def calculate_market_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate key market performance metrics."""
    if df is None or df.empty:
        raise DataAnalysisError("calculate_market_metrics requires a non-empty DataFrame")

    required = ['Market_Segment', 'Sales_Volume', 'Price_USD', 'Year']
    _ensure_columns(df, required)

    metrics = pd.DataFrame()

    # Sales by segment
    try:
        metrics['Market_Share'] = df.groupby('Market_Segment')['Sales_Volume'].sum()
        total = metrics['Market_Share'].sum()
        metrics['Market_Share_Pct'] = metrics['Market_Share'] / total * 100 if total else 0
    except Exception as exc:
        raise DataAnalysisError(f"Failed to compute market share: {exc}")

    # Average price by segment
    try:
        metrics['Avg_Price'] = df.groupby('Market_Segment')['Price_USD'].mean()
    except Exception as exc:
        print(f"Warning: failed to compute Avg_Price: {exc}")

    # Growth metrics (safe handling when insufficient years)
    try:
        yearly_sales = df.pivot_table(
            values='Sales_Volume',
            index='Market_Segment',
            columns='Year',
            aggfunc='sum'
        )
        if yearly_sales.shape[1] >= 2:
            last = yearly_sales.columns[-1]
            prev = yearly_sales.columns[-2]
            metrics['YoY_Growth'] = (
                (yearly_sales[last] - yearly_sales[prev]) / yearly_sales[prev] * 100
            )
        else:
            metrics['YoY_Growth'] = 0
    except Exception as exc:
        print(f"Warning: failed to compute YoY_Growth: {exc}")

    return metrics


def analyze_regional_performance(df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    """Analyze sales performance by region."""
    if df is None or df.empty:
        raise DataAnalysisError("analyze_regional_performance requires a non-empty DataFrame")

    required = ['Region', 'Year', 'Sales_Volume', 'Model', 'Market_Segment']
    _ensure_columns(df, required)

    results = {}

    # Regional sales volume
    try:
        results['sales'] = df.groupby(['Region', 'Year'])['Sales_Volume'].sum().unstack()
    except Exception as exc:
        raise DataAnalysisError(f"Failed to compute regional sales: {exc}")
    
    # Popular models by region
    try:
        results['top_models'] = (
            df.groupby(['Region', 'Model'])['Sales_Volume']
            .sum()
            .reset_index()
            .sort_values('Sales_Volume', ascending=False)
            .groupby('Region')
            .head(3)
        )
    except Exception as exc:
        print(f"Warning: failed to compute top_models: {exc}")
    
    # Market segment preferences
    try:
        results['segment_share'] = (
            df.groupby(['Region', 'Market_Segment'])['Sales_Volume']
            .sum()
            .unstack()
            .fillna(0)
        )
    except Exception as exc:
        print(f"Warning: failed to compute segment_share: {exc}")
    
    return results


def calculate_time_series_metrics(df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, float]]:
    """Calculate time series metrics and trends."""
    if df is None or df.empty:
        raise DataAnalysisError("calculate_time_series_metrics requires a non-empty DataFrame")

    _ensure_columns(df, ['Year', 'Sales_Volume', 'Price_USD', 'Green_Vehicle'])

    # Prepare time series data
    ts_data = df.groupby('Year').agg({
        'Sales_Volume': 'sum',
        'Price_USD': 'mean',
        'Green_Vehicle': 'sum'
    })
    
    # Calculate year-over-year changes
    ts_data['Sales_YoY'] = ts_data['Sales_Volume'].pct_change() * 100
    ts_data['Price_YoY'] = ts_data['Price_USD'].pct_change() * 100
    
    # Calculate key metrics
    try:
        avg_yearly_growth = ts_data['Sales_YoY'].mean()
    except Exception:
        avg_yearly_growth = 0

    try:
        price_trend = ts_data['Price_YoY'].mean()
    except Exception:
        price_trend = 0

    try:
        green_vehicle_growth = (
            ts_data['Green_Vehicle'].iloc[-1] / ts_data['Green_Vehicle'].iloc[0] - 1
        ) * 100 if ts_data['Green_Vehicle'].iloc[0] > 0 else 0
    except Exception:
        green_vehicle_growth = 0

    metrics = {
        'avg_yearly_growth': avg_yearly_growth,
        'price_trend': price_trend,
        'green_vehicle_growth': green_vehicle_growth
    }
    
    return ts_data, metrics


def segment_customer_base(df: pd.DataFrame) -> pd.DataFrame:
    """Segment customers based on purchase patterns."""
    if df is None or df.empty:
        raise DataAnalysisError("segment_customer_base requires a non-empty DataFrame")

    required = ['Price_USD', 'Customer_ID', 'Vehicle_Type']
    _ensure_columns(df, required)

    segments = df.copy()

    # Price sensitivity (safe qcut)
    try:
        segments['Price_Category'] = pd.qcut(
            df['Price_USD'].rank(method='first'),
            q=5,
            labels=['Budget', 'Value', 'Mid-Range', 'Premium', 'Luxury']
        )
    except Exception:
        # fallback to cut if qcut fails due to duplicate edges
        segments['Price_Category'] = pd.cut(df['Price_USD'], bins=5, labels=['Budget', 'Value', 'Mid-Range', 'Premium', 'Luxury'])

    # Vehicle type preference
    try:
        segments['Primary_Type'] = df.groupby('Customer_ID')['Vehicle_Type'].agg(lambda x: x.mode().iat[0] if not x.mode().empty else np.nan)
    except Exception:
        segments['Primary_Type'] = np.nan

    # Purchase frequency
    try:
        purchase_freq = df.groupby('Customer_ID').size()
        freq_map = purchase_freq.to_dict()
        segments['Purchase_Frequency'] = segments['Customer_ID'].map(freq_map)
        segments['Purchase_Frequency'] = pd.qcut(segments['Purchase_Frequency'].rank(method='first'), q=3, labels=['Low', 'Medium', 'High'])
    except Exception:
        segments['Purchase_Frequency'] = 'Unknown'

    return segments