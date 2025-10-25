"""
visualization.py

Visualization functions for BMW sales data analysis.
Creates standardized plots and figures for analysis and reporting.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional


def set_plotting_style():
    """Set consistent style for all visualizations."""
    plt.style.use('seaborn')
    plt.rcParams['figure.figsize'] = (12, 6)
    sns.set_palette('deep')
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.labelsize'] = 12


def plot_sales_trends(df: pd.DataFrame, save_path: Optional[str] = None) -> None:
    """Plot sales trends over time with segmentation."""
    if df is None or df.empty:
        raise ValueError("plot_sales_trends requires a non-empty DataFrame")

    set_plotting_style()
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # Overall sales trend
    try:
        yearly_sales = df.groupby('Year')['Sales_Volume'].sum()
        yearly_sales.plot(ax=ax1, marker='o')
    except Exception as exc:
        raise ValueError(f"Failed to plot overall sales trend: {exc}")
    ax1.set_title('Total Sales Volume Over Time')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Sales Volume')
    
    # Sales by market segment
    try:
        segment_sales = df.pivot_table(
            values='Sales_Volume',
            index='Year',
            columns='Market_Segment',
            aggfunc='sum'
        )
        segment_sales.plot(ax=ax2, kind='bar', stacked=True)
    except Exception as exc:
        print(f"Warning: failed to plot segment sales: {exc}")
    ax2.set_title('Sales Volume by Market Segment')
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Sales Volume')
    plt.legend(title='Market Segment', bbox_to_anchor=(1.05, 1))
    
    plt.tight_layout()
    if save_path:
        try:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        except Exception as exc:
            print(f"Warning: failed to save plot to {save_path}: {exc}")


def create_regional_dashboard(df: pd.DataFrame, save_path: Optional[str] = None) -> None:
    """Create a dashboard of regional sales performance."""
    if df is None or df.empty:
        raise ValueError("create_regional_dashboard requires a non-empty DataFrame")

    set_plotting_style()
    fig = plt.figure(figsize=(15, 10))
    
    # Regional sales distribution
    plt.subplot(2, 2, 1)
    try:
        sns.barplot(
            data=df.groupby('Region')['Sales_Volume'].sum().reset_index(),
            x='Region',
            y='Sales_Volume'
        )
    except Exception as exc:
        print(f"Warning: failed to create regional sales barplot: {exc}")
    plt.xticks(rotation=45)
    plt.title('Total Sales by Region')
    
    # Model popularity by region
    plt.subplot(2, 2, 2)
    try:
        region_model = df.pivot_table(
            values='Sales_Volume',
            index='Region',
            columns='Model',
            aggfunc='sum'
        )
        sns.heatmap(region_model, cmap='YlOrRd', annot=True, fmt='.0f')
    except Exception as exc:
        print(f"Warning: failed to create region-model heatmap: {exc}")
    plt.title('Model Popularity by Region')
    
    # Price distribution by region
    plt.subplot(2, 2, 3)
    try:
        sns.boxplot(data=df, x='Region', y='Price_USD')
    except Exception as exc:
        print(f"Warning: failed to create price distribution boxplot: {exc}")
    plt.xticks(rotation=45)
    plt.title('Price Distribution by Region')
    
    # Green vehicle adoption
    plt.subplot(2, 2, 4)
    try:
        green_adoption = (
            df[df['Green_Vehicle']].groupby(['Year', 'Region'])
            ['Sales_Volume'].sum().unstack()
        )
        green_adoption.plot(marker='o')
    except Exception as exc:
        print(f"Warning: failed to plot green vehicle adoption: {exc}")
    plt.title('Green Vehicle Adoption by Region')
    
    plt.tight_layout()
    if save_path:
        try:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        except Exception as exc:
            print(f"Warning: failed to save dashboard to {save_path}: {exc}")


def plot_feature_importance(
    features: pd.Series,
    title: str = 'Feature Importance',
    save_path: Optional[str] = None
) -> None:
    """Plot feature importance scores."""
    if features is None or features.empty:
        raise ValueError("plot_feature_importance requires a non-empty pandas Series")

    set_plotting_style()
    plt.figure(figsize=(10, 6))

    try:
        features.sort_values().plot(kind='barh')
    except Exception as exc:
        raise ValueError(f"Failed to plot feature importance: {exc}")
    plt.title(title)
    plt.xlabel('Importance Score')
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)


def create_market_segments_view(df: pd.DataFrame, save_path: Optional[str] = None) -> None:
    """Create visualization of market segmentation analysis."""
    if df is None or df.empty:
        raise ValueError("create_market_segments_view requires a non-empty DataFrame")

    set_plotting_style()
    fig = plt.figure(figsize=(15, 10))
    
    # Segment size
    plt.subplot(2, 2, 1)
    try:
        df['Market_Segment'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    except Exception as exc:
        print(f"Warning: failed to plot market segment distribution: {exc}")
    plt.title('Market Segment Distribution')
    
    # Price ranges by segment
    plt.subplot(2, 2, 2)
    try:
        sns.boxplot(data=df, x='Market_Segment', y='Price_USD')
    except Exception as exc:
        print(f"Warning: failed to create price ranges boxplot: {exc}")
    plt.xticks(rotation=45)
    plt.title('Price Ranges by Segment')
    
    # Segment performance over time
    plt.subplot(2, 2, (3, 4))
    try:
        segment_trend = df.pivot_table(
            values='Sales_Volume',
            index='Year',
            columns='Market_Segment',
            aggfunc='sum'
        )
        segment_trend.plot(marker='o')
    except Exception as exc:
        print(f"Warning: failed to plot segment performance over time: {exc}")
    plt.title('Segment Performance Over Time')
    
    plt.tight_layout()
    if save_path:
        try:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        except Exception as exc:
            print(f"Warning: failed to save market segments view to {save_path}: {exc}")