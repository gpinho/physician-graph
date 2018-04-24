import json
import pandas as pd
from pymongo import MongoClient

def get_header(header_path, remove_char='.'):
    df = pd.read_csv(header_path)
    header = list(df.columns.values)
    for idx, col in enumerate(header):
        if remove_char in col:
            header[idx] = col.replace(remove_char, "")
    return header

def mongo_import(csv_path, db_name, coll_name, header, chunksize=500000):
    """ Imports a csv file at path csv_name to a mongo colection
    returns: count of the documents in the new collection
    """
    client = MongoClient()
    db = client[db_name]
    coll = db[coll_name]
    tfreader = pd.read_csv(csv_path, names=header, chunksize=chunksize)
    for chunk in tfreader:
        data = pd.DataFrame(chunk)
        payload = json.loads(data.to_json(orient='records'))
        coll.insert(payload)
    return coll.count()

if __name__ == '__main__':
    # npi dataset
    # header_npi = get_header('data/NPI/npidata_pfile_20050523-20180408_FileHeader.csv')
    # mongo_import('data/NPI/npidata_pfile_20050523-20180408.csv', 'healthcare', 'npi', header_npi)

    # referral dataset
    # header_referral = ['Initial Physician NPI', 'Secondary Physician NPI', 'Shared Count', 'Number Unique Beneficiaries', 'Number Same Day Visits']
    # mongo_import('data/referral/physician-shared-patient-patterns-2014-days180.txt', 'healthcare', 'referral-2014-180', header_referral)

    # provider taxonomy dataset
    # mongo_import('data/provider taxonomy/nucc_taxonomy_180.csv', 'healthcare', 'provider-taxonomy', None)
