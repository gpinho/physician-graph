from geopy.geocoders import Nominatim
import pandas as pd

def convert_categorical_to_dummy(data_frame, categorical_cols):
    '''
    Takes a pandas dataframe
    Takes a list of target categorical columns
    Returns a new pandas dataframe with dummy variables
    '''
    return pd.get_dummies(data_frame, prefix_sep='_' , columns=categorical_cols)


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


def get_coordinates(npi_file, usecols):

    df = pd.read_csv(npi_file, usecols=usecols, index_col=['NPI'])

    d = pd.to_dict()

    geolocator = Nominatim()

    for index, row in df.iterrows():
        first_line = row['Provider First Line Business Mailing Address']
        second_line = row['Provider Second Line Business Mailing Address']
        city = row['Provider Business Mailing Address City Name']
        state = row['Provider Business Mailing Address State Name']
        postal_code = row['Provider Business Mailing Address Postal Code']
        country = row['Provider Business Mailing Address Country Code (If outside US)']
        try:
            address = f"{first_line} {city} {state} {country}"
            location = geolocator.geocode(address)
            latitude, longitude = location.latitude, location.longitude
            d['Latitude'][index] = latitude
            d['Longitude'][index] = longitude
        except:
            address = f"{city} {state} {country}"
            location = geolocator.geocode(address)
            d['Latitude'][index] = latitude
            d['Longitude'][index] = longitude

    df = pd.DataFrame.from_dict(d)
    df.to_csv('npidata_pfile_20050523-20180408_practiceLocation.csv')

if __name__ == '__main__':


    # feature engineer specialty dataset
    specialty_cols = ['Code', 'Grouping', 'Classification', 'Specialization', 'Definition']
    specialty_df = pd.read_csv('https://s3-us-west-1.amazonaws.com/physician-referral-graph/nucc_taxonomy_180.csv', index_col=['Code'], dtype=str, usecols=specialty_cols)
    specialty_df.replace('Definition to come...', np.nan, inplace=True)
    specialty_categorical_cols = ['Grouping', 'Classification', 'Specialization']
    specialty_df_dummies = convert_categorical_to_dummy(taxonomy_df, taxonomy_categorical_cols)
    specialty_df_dummies.to_csv('nucc_taxonomy_180_dummies.csv')


    save_files_to_s3(['nucc_taxonomy_180_dummies.csv'], 'physician-referral-graph')



    npi_file = 'https://s3-us-west-1.amazonaws.com/physician-referral-graph/npidata_pfile_20050523-20180408_withHeader.csv'
    usecols = ['NPI', 'Provider First Line Business Mailing Address',
    'Provider Business Mailing Address City Name', 'Provider Business Mailing Address State Name', 'Provider Business Mailing Address Postal Code', 'Provider Business Mailing Address Country Code (If outside US)']
    get_coordinates(npi_file, usecols)
    # feature engineer npi dataset
    # npi_usecols = ['NPI', 'Provider Gender Code','Healthcare Provider Taxonomy Code_1']
    # npi_df = pd.read_csv("https://s3-us-west-1.amazonaws.com/physician-referral-graph/npidata_pfile_20050523-20180408_withHeader.csv", index_col=['NPI'], usecols=npi_usecols)
    # npi_categorical_cols = ['Provider Gender Code']
    # npi_df_dummies = convert_categorical_to_dummy(npi_df, npi_categorical_cols)
    # npi_df_dummies.to_csv('npidata_pfile_20050523-20180408_withHeader_dummies.csv')
    # save_files_to_s3(['npidata_pfile_20050523-20180408_withHeader_dummies.csv'], 'physician-referral-graph')
