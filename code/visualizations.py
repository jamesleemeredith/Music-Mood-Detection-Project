"""
This module is for your final visualization code.
After you have done your EDA and wish to create some visualizations for you final jupyter notebook
A framework for each type of visualization is provided.
"""
# visualization packages
import matplotlib.pyplot as plt
from matplotlib.axes._axes import _log as matplotlib_axes_logger
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as mtick
import seaborn as sns
import code_package.data_preparation as dp

# Standard data manipulation packages
import pandas as pd
import numpy as np

matplotlib_axes_logger.setLevel('ERROR')

# Set specific parameters for the visualizations
large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
sns.set_style("dark")
sns.set_context("poster")
sns.color_palette("colorblind")


def commercial_fatality_rates(df):
    fig, ax = plt.subplots()
    data = df[df['top_make'] & (df['use_category'] == 'Commercial')]
    sns.barplot(data=data, 
                x='make', 
                y='fatality_rate',
                ax=ax,
               )
    ax.set_title('Fatality Rates by Make (Commercial)')
    ax.set_ylabel('Fatality Rate')
    ax.set_xlabel('Make')
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0, decimals=None))
    fig.savefig("images/commercial_fatality_rates_by_make.png");
    
    pass

def private_fatality_rates(df):
    fig, ax = plt.subplots()
    data = df[df['top_make']  & (df['use_category'] == 'Private Enterprise')]
    sns.barplot(data=data, 
                x='make', 
                y='fatality_rate',
                ax=ax,
               )
    ax.set_title('Fatality Rates by Make (Private Enterprise)')
    ax.set_ylabel('Fatality Rate')
    ax.set_xlabel('Make')
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0, decimals=None))
    fig.savefig("images/private_fatality_rates_by_make.png");

    pass

def private_models_fatality_rates(df):
    fig, ax = plt.subplots(figsize=(10, 10))
    df_filter = df['top_model'] & (df['use_category'] == 'Private Enterprise')
    sns.barplot(data=df[df_filter], 
                x='fatality_rate',
                y='model',
                ax=ax,
               )
    sns.set_style("dark")
    ax.set_title('Fatality Rates by Model (Private Enterprise)')
    ax.set_ylabel('Fatality Rate')
    ax.set_xlabel('Make')
    ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0, decimals=None))
    fig.savefig("images/private_fatality_rates_by_model.png");

    pass


def visualization_one(target_var = None, input_vars= None, output_image_name=None):
    """
    The visualization functions are what is used to create each individual image.
    The function should be repeatable if not generalizable
    The function will call either the boxplot or density plot functions you wrote above

    :param target_var:
    :param input_vars:
    :param output_image_name: the desired name for the image saved
    :return: outputs a saved png file and returns a fig object for testing
    """
    ###
    # Main chunk of code here
    ###

    # Starter code for labeling the image
    plt.xlabel(None, figure = fig)
    plt.ylabel(None, figure = fig)
    plt.title(None, figure= fig)
    plt.legend()

    # exporting the image to the img folder
    plt.savefig(f'images/{output_image_name}.png', transparent = True, figure = fig)
    return fig