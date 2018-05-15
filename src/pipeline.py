import graphlab as gl

class Pipeline(object):

    def __init__(self):
        self.referrals_sf = None
        self.edges_sf = None
        self.edges_train_sf = None
        self.edges_test_sf = None
        self.physicians_sf = None
        self.specialties_sf = None
        self.nodes_sf = None
        self.initial_node_sf = None
        self.secondary_node_sf = None


    def load_dataset_referrals(self, years, filepaths, usecols, dtype):

        datasets = zip(years, filepaths)

        left_year, left_file = datasets[0]
        self.referrals_sf = gl.SFrame.read_csv(left_file, usecols=usecols, column_type_hints=dtype)
        self.referrals_sf.rename({'Number Unique Beneficiaries': left_year})

        for idx in range(1, len(datasets)):
            right_year, right_file = datasets[idx]
            right_sf = gl.SFrame.read_csv(right_file, usecols=usecols, column_type_hints=dtype)
            right_sf.rename({'Number Unique Beneficiaries': right_year})
            self.referrals_sf = self.referrals_sf.join(right_sf, on=['Initial Physician NPI', 'Secondary Physician NPI'], how='outer')


    def get_referral_edges(self):

        cols = self.referrals_sf.column_names()
        for idx in range(2, len(cols)):
            self.referrals_sf = self.referrals_sf.fillna(cols[idx], 0.0)

        sum_col = cols[2]
        for idx in range(3, len(cols)):
            col = cols[idx]
            sum_col += self.referrals_sf[col]
        average_col = sum_col / (len(cols) - 2)

        self.edges_sf = self.referrals_sf[cols[0:2]]
        self.edges_sf.add_column(average_col, name='Referrals')

    def split_train_test_edges(self, train_fraction):

        self.edges_train_sf, self.edges_test_sf = self.edges_sf.random_split(train_fraction)


    def load_dataset_physicians(self, filepath, usecols, dtype):

        self.physicians_sf = gl.SFrame.read_csv(filepath, usecols=usecols, column_type_hints=dtype)


    def load_dataset_specialties(self, filepath, usecols, dtype):

        self.specialties_sf = gl.SFrame.read_csv(filepath, usecols=usecols, column_type_hints=dtype)


    def get_physician_nodes(self):

        self.specialties_sf.rename({'Code': 'Healthcare Provider Taxonomy Code_1'})
        self.nodes_sf = self.physicians_sf.join(self.specialties_sf, on='Healthcare Provider Taxonomy Code_1', how='left')
        self.nodes_sf.remove_column('Healthcare Provider Taxonomy Code_1')


    def split_initial_secondary_nodes(self):

        self.initial_node_sf = self.nodes_sf
        self.initial_node_sf.rename({'NPI': 'Initial Physician NPI'})
        self.secondary_node_sf = self.nodes_sf
        self.initial_node_sf.rename({'NPI': 'Secondary Physician NPI'})

if __name__ == '__main__':

    pass
