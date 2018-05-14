![Alt text](/app/static/img/pg-logo.png?raw=true "Optional Title")

# Predicting Physician Relationships Based on Shared Patients
This project is being developed as a capstone project for Galvanize's Data Science Immersive course.
https://www.galvanize.com/san-francisco/data-science



# Background
Patients rely on a network of specialized physicians in order to get healthcare, but to address patients specific needs physicians refer one another but what drives these referrals? There are no features that highlight existing relationships and that recommend new relationships between physicians. We expect to build a web app able to predict physician relationships (shared patients).

# Objective
Predict Edges/Links Using Physician Features (non-relationship) by a Model that was trained using Relationship Features

# NMF/UVD - Unsupervised Learning - Dimensionality Reduction
Use Cases:
- Soft clustering where each physician can have partial relationship in each cluster
- Identify latent features (topics, features that explain the cluster)

How it Works:
- W: physician by latent features
- H: latent features by features
- V: physicians by features

- W * H = V'

- Given V, NMF will return the best W and H in order to minimize OLS/ALS/SGD for a given k (number of desired latent features)

Questions:
- If we only use relationship features why should we use NMF to form soft clusters instead of graph communities?
- If we use all the features and identify the latent ones for each cluster how can we use it to predict edges?
- What's the impact of the number of features for NMF? Do they have different weights?
- How will NMF consider a feature such as Physician Specialty? Physicians are unlikely to refer to the same specialty
- How to represent directions in the matrix? (one column for each direction? or relationship only represented in one node but not the other?)
- What should the matrix representation be? nodes? edges?

Next Steps:
- Model Evaluation
  - Input combined dataset matrix
  - Choose k
  - Check results
  - Remove 10% of the relationships and save as test set
  - Input combined dataset matrix
  - Use same k
  - Compare results to test set
- Model Prediction
  - Given a new physician how can I predict clusters?
  - Given a new physician how can I predict edges?



# Datasets

### Physician Shared Patient Patterns
* **Readme**: https://downloads.cms.gov/foia/physician_shared_patient_patterns_technical_requirements.pdf
* **Download**: https://www.cms.gov/Regulations-and-Guidance/Legislation/FOIA/Referral-Data-FAQs.html
* **Overview**
    * **Providers Who Share Relationships with Common Patients**: "An organization or provider participating in the delivery of health services to the same patient within a 30 days, 60 days, 90 days and finally a 180 day period after another organization or provider participated in providing health services to the same patient."
    * **Example**: "For instance, if a patient with a patient identifier of 111-22-3333 was listed on a claim with a "treatment association" by NPI 3333333333, and then also listed on a claim as being treated 12 days after that date with a "treatment association" by NPI 4444444444. Then 3333333333 would have "shared" the patient with 4444444444
    * **Treatment Association**: "A "treatment association" is any field in the claims database,-other- than referring NPI, or the NPI for suppliers of durable medical equipment. Essentially, those NPI records that could have participated in the delivery of healthcare services associated with a given claim."
    * **Privacy Measures**: "In order to protect the identity of patients, this report excludes any sharing that happened with less than 11 different patients over the course of the year."
    * **Data Source**: "produced from the Integrated Data Repository (IDR) database, which houses claims from the National Claims History (NCH) database." (Medicare)

* **Files**
    * **Number of Files**: 28
    * **Years**: 2009, 2010, 2011, 2012, 2013, 2014, 2015 (until 10/01/2015)
    * **Intervals**: 30, 60, 90, 180 days
    * **File Size**: 2-7 GB each
    * **File Type**: txt (csv)
* **Variables**
    * **Number of Rows**: 138,614,191 (one file example)
    * **Rows**: Providers Who Share Relationships with Common Patients (directed)
    * **Number of Columns**: 5
    * **Columns**
        * **Initial Physician NPI**
        * **Secondary Physician NPI**
        * **Shared Count**: "number of beneficiary referrals"
        * **Number Unique Beneficiaries**: "number of unique beneficiary referrals"
        * **Number Same Day Visits**: "number of beneficiary referrals on the same day"
            * "Presumed shared relationships based on same-day events will be assigned to the lesser of the two NPIs"

### NPI | National Plan and Provider Enumeration System (NPPES)
* **Readme**: https://www.cms.gov/Regulations-and-Guidance/Administrative-Simplification/NationalProvIdentStand/Downloads/Data_Dissemination_File-Readme.pdf
* **Code Values**: https://www.cms.gov/Regulations-and-Guidance/Administrative-Simplification/NationalProvIdentStand/Downloads/Data_Dissemination_File-Code_Values.pdf
* **Download**: http://download.cms.gov/nppes/NPI_Files.html
* **API**: https://npiregistry.cms.hhs.gov/registry/help-api
* **Overview**
    * **xxx**:

* **Files**
    * **Number of Files**: 1
    * **Years**: 2005-2018 YTD
    * **File Size**: 6 GB
    * **File Type**: csv
* **Variables**
    * **Number of Rows**: 5,546,686
    * **Rows**: NPI Record
    * **Number of Columns**: 329
    * **Columns**: https://npiregistry.cms.hhs.gov/registry/Json-Conversion-Field-Map more details at https://www.cms.gov/Regulations-and-Guidance/Administrative-Simplification/NationalProvIdentStand/Downloads/Data_Dissemination_File-Code_Values.pdf
      * Next MVP Variables
        * NPI > Key for Referral Dataset
        * Provider Gender Code > Dummy Variables
        * Healthcare Provider Taxonomy Code_1 > Key for Taxonomy Dataset > Use Most Recent Taxonomy Code?
      * Follow-up MVP Variables
        * Provider Organization Name (Legal Business Name) > Dummy Variables
        * Provider Business Practice Location Address First Line, City, State, Country > Coordinates (Geopy) > ?
        * Is Sole Proprietor > Dummy Variables
        * Entity Type Code > Labels > Dummy Variables
        * Provider Other Organization Name > Include in Provider Organization Name (Legal Business Name) > Dummy Variables
        * Provider Business Practice Location Address Postal Code > Get Geographic Coordinates (Geopy) > Calculate Distance Between Providers > How to Include in Model Training?
        * Other Provider Variables > Research
        * Is Organization Subpart > Labels > Include in Is Sole Proprietor > Dummy Variables
        * Healthcare Provider Taxonomy Group_1 > Labels > Dummy Variables

Obs: NPI records in the downloadable file will also include deactivated health care provider data. But for these deactivated providers, only the NPI and its deactivation date will be visible in the downloadable file

### Health Care Provider Taxonomy Code
* **National Uniform Claim Committee**:
http://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40/csv-mainmenu-57
* **Washington Publishing Company**: http://www.wpc-edi.com/reference/codelists/healthcare/health-care-provider-taxonomy-code-set/


# Next Steps

## Additional Datasets
* **Physician Education**
* **Physician Most Common Procedures**

## Hyperparameter Optimization
* **Topic Modeling**
* **Feature Importance**

## Classification Model
* **Predict Strong Relationships Between Physicians With Over N Referrals**

## Web App
* **Build Physician Relationship Search Engine**
