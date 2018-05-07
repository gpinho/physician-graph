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

if __name__ == '__main__':

    # feature engineer taxonomy dataset
    taxonomy_df = pd.read_csv('https://s3-us-west-1.amazonaws.com/physician-referral-graph/nucc_taxonomy_180.csv', index_col=['Code'])
    taxonomy_categorical_cols = ['Grouping', 'Classification', 'Specialization']
    taxonomy_df_dummies = convert_categorical_to_dummy(taxonomy_df, taxonomy_categorical_cols)
    taxonomy_df_dummies.to_csv('nucc_taxonomy_180_dummies.csv')
    save_files_to_s3(['nucc_taxonomy_180_dummies.csv'], 'physician-referral-graph')
