import pandas as pd
import numpy as np
import os

def download_files(url_list):
    '''
    Takes a list of urls and downloads files to local directory
    '''
    download_command = 'curl'
    for url in url_list:
        download_command += ' -L -O ' + url
    os.system(download_command)


def unzip_files():
    '''
    Unzips all zip files in local directory
    '''
    unzip_command = 'unzip \*.zip'
    os.system(unzip_command)


def format_header(header_file, remove_char='.'):
    '''
    Takes a string with the header file
    Removes '.' to prevent errors with GraphLab
    Returns a string with column names separated by ','
    '''
    df = pd.read_csv(header_file)
    header = list(df.columns.values)
    for idx, col in enumerate(header):
        if remove_char in col:
            header[idx] = col.replace(remove_char, "")
    return ','.join(header)


def save_header_to_file(header, data_file, has_header=True):
    '''
    Takes a string with the desired header for the data file
    Takes a string with the target data file
    If data file already has a header, replace it with header provided
    If data file doesn't have a header, insert header provided
    Saves changes to a new file with header
    '''
    data_file_withHeader = data_file[:-4] + '_withHeader.csv'
    # creates a new file only with header
    os.system("echo '" + header + "' > " + data_file_withHeader)
    # copies data into to the created file
    os.system('cat ' + data_file + ' >> ' + data_file_withHeader)
    # deletes row with old header
    if has_header == True:
        os.system("sed -i  '2d' " + data_file_withHeader)


def save_header_to_file_list(header, data_files, has_header=True):
    '''
    Takes a list of strings with multiple target data files
    For each data file call save_header_to_file function
    '''
    for data_file in data_files:
        save_header_to_file(header, data_file, has_header)


def save_files_to_s3(data_files, s3_bucket):
    '''
    Takes a list of strings with multiple target data files
    Save each data file to specified s3 bucket
    '''
    aws_command = 'aws s3 cp '
    bucket_address =  ' s3://' + s3_bucket + '/'
    for data_file in data_files:
        os.system(aws_command + data_file + bucket_address)


def convert_categorical_to_dummy(data_frame, categorical_cols):
    '''
    Takes a pandas dataframe
    Takes a list of target categorical columns
    Returns a new pandas dataframe with dummy variables
    '''
    return pd.get_dummies(data_frame, prefix_sep=': ' , columns=categorical_cols)


def extract_nlp_features(data_frame, nlp_cols):
    '''
    Takes a pandas dataframe
    Takes a list of target nlp columns
    Returns a new pandas dataframe with IF-IDF word vectors
    '''
    pass

def tokenizer():
    '''
    Opportunity to use Stemming or Lemmatization
    '''
    pass

def combine_referral_datasets(left_filepath, left_suffix, list_right_filepath_suffix, index_col=['Initial Physician NPI', 'Secondary Physician NPI']):
    left_df = pd.read_csv(left_filepath, index_col=index_col)
    for right_file in list_right_filepath_suffix:
        right_filepath, right_suffix = right_file
        right_df = pd.read_csv(right_filepath, index_col=index_col)
        left_df = left_df.merge(right_df, how='outer', left_index= True, right_index=True, sort=True, copy=False, suffixes=(left_suffix, right_suffix))
    return left_df




if __name__ == '__main__':

    # list of dataset urls
#     referral_dataset_urls = ['http://downloads.cms.gov/foia/physician-shared-patient-patterns-2009-days180.zip', 'http://downloads.cms.gov/foia/physician-shared-patient-patterns-2010-days180.zip', 'http://downloads.cms.gov/foia/physician-shared-patient-patterns-2011-days180.zip', 'http://downloads.cms.gov/foia/physician-shared-patient-patterns-2012-days180.zip', 'http://downloads.cms.gov/foia/physician-shared-patient-patterns-2013-days180.zip', 'http://downloads.cms.gov/foia/physician-shared-patient-patterns-2014-days180.zip', 'http://downloads.cms.gov/foia/physician-shared-patient-patterns-2015-days180.zip']
#     npi_dataset_urls = ['http://download.cms.gov/nppes/NPPES_Data_Dissemination_April_2018.zip']
#     taxonomy_dataset_urls = ['http://www.nucc.org/images/stories/CSV/nucc_taxonomy_180.csv']

    # download datasets to local directory
#     download_files(taxonomy_dataset_urls + referral_dataset_urls + npi_dataset_urls)

    # unzip all zip files to local directory
#     unzip_files()

    # adjust headers
#     npi_dataset_header = format_header('npidata_pfile_20050523-20180408_FileHeader.csv')
#     save_header_to_file(npi_dataset_header, 'npidata_pfile_20050523-20180408.csv', has_header=True)
#     referral_dataset_txts = ['physician-shared-patient-patterns-2009-days180.txt', 'physician-shared-patient-patterns-2010-days180.txt', 'physician-shared-patient-patterns-2011-days180.txt', 'physician-shared-patient-patterns-2012-days180.txt', 'physician-shared-patient-patterns-2013-days180.txt', 'physician-shared-patient-patterns-2014-days180.txt', 'physician-shared-patient-patterns-2015-days180.txt']
#     referral_dataset_header = ','.join(['Initial Physician NPI', 'Secondary Physician NPI', 'Shared Count', 'Number Unique Beneficiaries', 'Number Same Day Visits'])
#     save_header_to_file_list(referral_dataset_header, referral_dataset_txts, has_header=False)

    # save files with adjusted headers to s3
#     taxonomy_dataset_csvs = ['nucc_taxonomy_180.csv']
#     npi_dataset_csvs = ['npidata_pfile_20050523-20180408_withHeader.csv']
#     referral_dataset_csvs = ['physician-shared-patient-patterns-2009-days180_withHeader.csv', 'physician-shared-patient-patterns-2010-days180_withHeader.csv', 'physician-shared-patient-patterns-2011-days180_withHeader.csv', 'physician-shared-patient-patterns-2012-days180_withHeader.csv', 'physician-shared-patient-patterns-2013-days180_withHeader.csv', 'physician-shared-patient-patterns-2014-days180_withHeader.csv', 'physician-shared-patient-patterns-2015-days180_withHeader.csv']
#     save_files_to_s3(taxonomy_dataset_csvs + npi_dataset_csvs + referral_dataset_csvs, 'physician-referral-graph')

    # feature engineer taxonomy dataset
    # taxonomy_df = pd.read_csv('https://s3-us-west-1.amazonaws.com/physician-referral-graph/nucc_taxonomy_180.csv', index_col=['Code'])
    # taxonomy_categorical_cols = ['Grouping', 'Classification', 'Specialization']
    # taxonomy_df_dummies = convert_categorical_to_dummy(taxonomy_df, taxonomy_categorical_cols)
    # taxonomy_df_dummies.to_csv('nucc_taxonomy_180_dummies.csv')
    # save_files_to_s3(['nucc_taxonomy_180_dummies.csv'], 'physician-referral-graph')

    # feature engineer npi dataset
    # npi_usecols = ['NPI', 'Provider Gender Code','Healthcare Provider Taxonomy Code_1']
    # npi_df = pd.read_csv("https://s3-us-west-1.amazonaws.com/physician-referral-graph/npidata_pfile_20050523-20180408_withHeader.csv", index_col=['NPI'], usecols=npi_usecols)
    # npi_categorical_cols = ['Provider Gender Code']
    # npi_df_dummies = convert_categorical_to_dummy(npi_df, npi_categorical_cols)
    # npi_df_dummies.to_csv('npidata_pfile_20050523-20180408_withHeader_dummies.csv')
    # save_files_to_s3(['npidata_pfile_20050523-20180408_withHeader_dummies.csv'], 'physician-referral-graph')

    # feature engineer referral dataset
    initial_referral_dataset = 'https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2009-days180_withHeader.csv'
    initial_referral_year = '2009: '
    other_referral_datasets_years = [('2010: ','https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2010-days180_withHeader.csv'), ('2011: ', 'https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2011-days180_withHeader.csv'), ('2012: ', 'https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2012-days180_withHeader.csv'), ('2013: ', 'https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2013-days180_withHeader.csv'), ('2014: ', 'https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2014-days180_withHeader.csv'), ('2015: ', 'https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2015-days180_withHeader.csv')]
    referral_df = combine_referral_datasets(initial_referral_dataset, initial_referral_yearm other_referral_datasets_years)
    referral_df.to_csv('physician-shared-patient-patterns-2009-2015-days180_withHeader.csv')
    save_files_to_s3(['physician-shared-patient-patterns-2009-2015-days180_withHeader.csv'], 'physician-referral-graph')



    combine different years into one file




    # get adjusted average (2015)

    # split test train referral datasets
