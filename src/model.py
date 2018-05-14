import graphlab as gl

if __name__ == '__main__':

    edges_train_url = 'https://s3-us-west-1.amazonaws.com/physician-referral-graph/edges_train.csv'
    edges_train_sf = gl.SFrame.read_csv(url, column_type_hints=[int, int, float])
    baseline_model = gl.recommender.factorization_recommender.create(edges_train_sf, user_id='Initial Physician NPI', item_id='Secondary Physician NPI', target='Average Number Unique Beneficiaries')
    baseline_model.save('model/baseline_model')
