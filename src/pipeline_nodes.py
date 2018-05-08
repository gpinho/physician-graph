
import numpy as np
import pandas as pd
import re
import string
from pipeline_datasets import save_files_to_s3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from nltk import word_tokenize, corpus
from nltk.stem import WordNetLemmatizer
from geopy.geocoders import Nominatim

def convert_categorical_to_dummy(data_frame, categorical_cols):
    '''
    Takes a pandas dataframe
    Takes a list of target categorical columns
    Returns a new pandas dataframe with dummy variables
    '''
    return pd.get_dummies(data_frame, prefix_sep='_' , columns=categorical_cols)

def tokenize(doc):
    '''
    INPUT: string
    OUTPUT: list of strings

    Tokenize and stem/lemmatize the document.
    '''
    return [wordnet.lemmatize(word) for word in word_tokenize(re.sub('[^a-z\s]', '', doc.lower()))]

# def combine_physician_specialty(physician_df, left_year, list_right_filepath_year, usecols=['Initial Physician NPI', 'Secondary Physician NPI', 'Number Unique Beneficiaries'], dtype={'Initial Physician NPI':str, 'Secondary Physician NPI':str, 'Number Unique Beneficiaries':np.int32}, index_col=['Initial Physician NPI', 'Secondary Physician NPI']):
#     print('function starting')
#     left_df = pd.read_csv(left_filepath, usecols=usecols, dtype=dtype, index_col=index_col)
#     left_df.columns += '_' + left_year
#     print(f'year {left_year} loaded')
#     for right_file in list_right_filepath_year:
#         right_filepath, right_year = right_file
#         right_df = pd.read_csv(right_filepath, usecols=usecols, dtype=dtype, index_col=index_col)
#         print(f'year {right_year} loaded')
#         right_df.columns += '_' + right_year
#         left_df = left_df.merge(right_df, how='outer', left_index= True, right_index=True, copy=False)
#         print(f'year {right_year} merged')
#         left_df.to_csv('physician-shared-patient-patterns-' + left_year + '-' + right_year + '.csv')
#         print('dataframe saved to csv')
#     return left_df

# def get_top_values(lst, n, labels):
#     '''
#     INPUT: LIST, INTEGER, LIST
#     OUTPUT: LIST
#
#     Given a list of values, find the indices with the highest n values.
#     Return the labels for each of these indices.
#
#     e.g.
#     lst = [7, 3, 2, 4, 1]
#     n = 2
#     labels = ["cat", "dog", "mouse", "pig", "rabbit"]
#     output: ["cat", "pig"]
#     '''
#     return [labels[i] for i in np.argsort(lst)[-1:-n-1:-1]]


# def get_coordinates(npi_file, usecols):
#
#     df = pd.read_csv(npi_file, usecols=usecols, index_col=['NPI'])
#
#     d = pd.to_dict()
#
#     geolocator = Nominatim()
#
#     for index, row in df.iterrows():
#         first_line = row['Provider First Line Business Mailing Address']
#         second_line = row['Provider Second Line Business Mailing Address']
#         city = row['Provider Business Mailing Address City Name']
#         state = row['Provider Business Mailing Address State Name']
#         postal_code = row['Provider Business Mailing Address Postal Code']
#         country = row['Provider Business Mailing Address Country Code (If outside US)']
#         try:
#             address = f"{first_line} {city} {state} {country}"
#             location = geolocator.geocode(address)
#             latitude, longitude = location.latitude, location.longitude
#             d['Latitude'][index] = latitude
#             d['Longitude'][index] = longitude
#         except:
#             address = f"{city} {state} {country}"
#             location = geolocator.geocode(address)
#             d['Latitude'][index] = latitude
#             d['Longitude'][index] = longitude
#
#     df = pd.DataFrame.from_dict(d)
#     df.to_csv('npidata_pfile_20050523-20180408_practiceLocation.csv')

if __name__ == '__main__':


    # feature engineer specialty dataset
    # specialty_cols = ['Code', 'Grouping', 'Classification', 'Specialization', 'Definition']
    # specialty_df = pd.read_csv('https://s3-us-west-1.amazonaws.com/physician-referral-graph/nucc_taxonomy_180.csv', dtype=str, usecols=specialty_cols)
    # specialty_df.replace('Definition to come...', np.nan, inplace=True)
    # specialty_categorical_cols = ['Grouping', 'Classification', 'Specialization']
    # specialty_df_dummies = convert_categorical_to_dummy(specialty_df, specialty_categorical_cols)
    # specialty_df_dummies.to_csv('nucc_taxonomy_180_dummies.csv')
    # save_files_to_s3(['nucc_taxonomy_180_dummies.csv'], 'physician-referral-graph')
    #
    # wordnet = WordNetLemmatizer()
    # vectorizer = TfidfVectorizer(stop_words='english', tokenizer=tokenize)
    # vectors = vectorizer.fit_transform(specialty_df_dummies['Definition'].fillna('')).toarray()
    # words = vectorizer.get_feature_names()
    # description_vect_df = pd.DataFrame(vectors, columns=words)
    # specialty_df_combined = pd.concat([specialty_df_dummies, description_vect_df], axis=1).drop(['Definition'], axis=1)
    # specialty_df_combined.to_csv('nucc_taxonomy_180_nlp.csv')
    # save_files_to_s3(['nucc_taxonomy_180_nlp.csv'], 'physician-referral-graph')

    # feature engineer physician dataset
    physician_cols = ['NPI', 'Entity Type Code', 'Provider Business Practice Location Address City Name', 'Provider Business Practice Location Address State Name', 'Provider Business Practice Location Address Country Code (If outside US)', 'Provider Gender Code', 'Healthcare Provider Taxonomy Code_1']
    physician_dtype = {'NPI':int, 'Entity Type Code':float, 'Provider Business Practice Location Address City Name':str, 'Provider Business Practice Location Address State Name':str, 'Provider Business Practice Location Address Country Code (If outside US)':str, 'Provider Gender Code':str, 'Healthcare Provider Taxonomy Code_1':str}
    physician_file = 'https://s3-us-west-1.amazonaws.com/physician-referral-graph/npidata_pfile_20050523-20180408_withHeader.csv'
    # physician_file = 'data/samples/npidata_pfile_20050523-20180408_withHeader-subsample.csv'
    physician_df = pd.read_csv(physician_file, dtype=physician_dtype, usecols=physician_cols)
    physician_df['Entity Type Code'].replace(2, 0, inplace=True)
    physician_categorical_cols = ['Provider Business Practice Location Address City Name', 'Provider Business Practice Location Address State Name', 'Provider Business Practice Location Address Country Code (If outside US)', 'Provider Gender Code']
    physician_df_dummies = convert_categorical_to_dummy(physician_df, physician_categorical_cols)
    physician_df_dummies.to_csv('npidata_pfile_20050523-20180408_withHeader_dummies.csv')
    save_files_to_s3(['npidata_pfile_20050523-20180408_withHeader_dummies.csv'], 'physician-referral-graph')

    # get_coordinates(npi_file, usecols)
    # # feature engineer npi dataset
    # npi_usecols = ['NPI', 'Provider Gender Code','Healthcare Provider Taxonomy Code_1']
    # npi_df = pd.read_csv("https://s3-us-west-1.amazonaws.com/physician-referral-graph/npidata_pfile_20050523-20180408_withHeader.csv", index_col=['NPI'], usecols=npi_usecols)
    # npi_categorical_cols = ['Provider Gender Code']
    # npi_df_dummies = convert_categorical_to_dummy(npi_df, npi_categorical_cols)
    # npi_df_dummies.to_csv('npidata_pfile_20050523-20180408_withHeader_dummies.csv')
    # save_files_to_s3(['npidata_pfile_20050523-20180408_withHeader_dummies.csv'], 'physician-referral-graph')
