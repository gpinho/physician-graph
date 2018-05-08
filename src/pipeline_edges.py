import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from pipeline_store_datasets import save_files_to_s3

def combine_referral_datasets(left_filepath, left_year, list_right_filepath_year, usecols=['Initial Physician NPI', 'Secondary Physician NPI', 'Number Unique Beneficiaries'], dtype={'Initial Physician NPI':str, 'Secondary Physician NPI':str, 'Number Unique Beneficiaries':np.int32}, index_col=['Initial Physician NPI', 'Secondary Physician NPI']):
    print('function starting')
    left_df = pd.read_csv(left_filepath, usecols=usecols, dtype=dtype, index_col=index_col)
    left_df.columns += '_' + left_year
    print(f'year {left_year} loaded')
    for right_file in list_right_filepath_year:
        right_filepath, right_year = right_file
        right_df = pd.read_csv(right_filepath, usecols=usecols, dtype=dtype, index_col=index_col)
        print(f'year {right_year} loaded')
        right_df.columns += '_' + right_year
        left_df = left_df.merge(right_df, how='outer', left_index= True, right_index=True, copy=False)
        print(f'year {right_year} merged')
        left_df.to_csv('physician-shared-patient-patterns-' + left_year + '-' + right_year + '.csv')
        print('dataframe saved to csv')
    return left_df

def get_average(df):
    cols = df.columns
    df['Sum Number Unique Beneficiaries'] = 0
    for col in cols:
        df['Sum Number Unique Beneficiaries'] += df[col]
    df['Average Number Unique Beneficiaries'] = df['Sum Number Unique Beneficiaries'] / len(cols)
    return df

def drop_cols(df, cols):
    return df.drop(columns=cols)

def split_train_test(df):
    y_regression_train, y_regression_test = train_test_split(df, test_size=0.1)
    return y_regression_train, y_regression_test

if __name__ == '__main__':

    # feature engineer referral dataset
    initial_referral_dataset = 'https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2009-days180_withHeader.csv'
    initial_referral_year = '2009'
    other_referral_datasets_years = [('https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2010-days180_withHeader.csv', '2010'), ('https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2011-days180_withHeader.csv', '2011'), ('https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2012-days180_withHeader.csv', '2012'), ('https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2013-days180_withHeader.csv', '2013'), ('https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2014-days180_withHeader.csv', '2014'), ('https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2015-days180_withHeader.csv', '2015')]
    referral_df = combine_referral_datasets(initial_referral_dataset, initial_referral_year, other_referral_datasets_years)
    referral_df.to_csv('physician-shared-patient-patterns-2009-2015-days180_withHeader.csv')
    save_files_to_s3(['physician-shared-patient-patterns-2009-2015-days180_withHeader.csv'], 'physician-referral-graph')
    average_df = get_average(referral_df)
    average_df.to_csv('physician-shared-patient-patterns-average-unique-beneficiaries.csv')
    save_files_to_s3(['physician-shared-patient-patterns-average-unique-beneficiaries.csv'], 'physician-referral-graph')
    drop = ['Number Unique Beneficiaries_2009','Number Unique Beneficiaries_2010','Number Unique Beneficiaries_2011','Number Unique Beneficiaries_2012','Number Unique Beneficiaries_2013','Number Unique Beneficiaries_2014','Number Unique Beneficiaries_2015']
    y_regression_df = drop_cols(average_df, drop)
    y_regression_df.to_csv('y_regression_full.csv')
    y_regression_train, y_regression_test = split_train_test(y_regression_df)
    y_regression_train.to_csv('y_regression_train.csv')
    y_regression_test.to_csv('y_regression_test.csv')
    save_files_to_s3(['y_regression_train.csv', 'y_regression_test.csv'], 'physician-referral-graph')
