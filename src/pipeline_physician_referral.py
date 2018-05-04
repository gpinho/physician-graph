
def combine_referral_datasets(left_suffix, left_filepath, list_right_filepath_suffix, index_col=['Initial Physician NPI', 'Secondary Physician NPI']):
    left_df = pd.read_csv(left_filepath, index_col=index_col)
    for right_file in list_right_filepath_suffix:
        right_suffix, right_filepath = right_file
        right_df = pd.read_csv(right_filepath, index_col=index_col)
        left_df = left_df.merge(right_df, how='outer', left_index= True, right_index=True, sort=True, copy=False, suffixes=(left_suffix, right_suffix))
    return left_df

if __name__ == '__main__':
    # feature engineer referral dataset
    initial_referral_dataset = 'https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2009-days180_withHeader.csv'
    initial_referral_year = '2009: '
    other_referral_datasets_years = [('2010: ','https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2010-days180_withHeader.csv'), ('2011: ', 'https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2011-days180_withHeader.csv'), ('2012: ', 'https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2012-days180_withHeader.csv'), ('2013: ', 'https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2013-days180_withHeader.csv'), ('2014: ', 'https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2014-days180_withHeader.csv'), ('2015: ', 'https://s3-us-west-1.amazonaws.com/physician-referral-graph/physician-shared-patient-patterns-2015-days180_withHeader.csv')]
    referral_df = combine_referral_datasets(initial_referral_year, initial_referral_dataset, other_referral_datasets_years)
    referral_df.to_csv('physician-shared-patient-patterns-2009-2015-days180_withHeader.csv')
    save_files_to_s3(['physician-shared-patient-patterns-2009-2015-days180_withHeader.csv'], 'physician-referral-graph')
