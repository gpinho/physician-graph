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

# PCA/SVD - Unsupervised Learning - Dimensionality Reduction
Use Cases:
- Reduce dimensionality for (1) Clustering, (2) Visualization, (3) Compress/Storage

How it Works:
- X: physicians by features
- E: eigenvectors of the covariance matrix by features
- X': physicians by eigenvectors (principal components)

- X * E(t) = X'
- X(t) * X = Covariance Matrix

- Given X, PCA will return the best X' to minimize distance from the original data to the projections while maximizing the variance of the projections, first k principal components will create the best k dimensional reconstruction. SVD will return the same result in a more computationally efficient manner.

Questions:
- If the latent features are difficult to interpret why would I want to use PCA instead of NMF?
- Principal Component Regression? NMF Regression?
- Same questions as NMF

Next Steps:
- Similar Steps to NMF

# Recommenders
Use Cases:
- Popularity
- Content-Based / Content Filtering
- Collaborative Filtering: User-User (Physician-Physician), Item-Item (RelationshipWith-RelationshipWith), Similarity Matrix, RelationshipWith Prediction for Physician (Known RelationshipWith Similarity * Number of Shared Patients)
- Matrix Factorization Methods

Questions:
- Can we add the Physician Features (non-relationship)?
  - If Item/Column: Similarity between RelationshipWith and Specialty/Location
  - If User/Row: Similarity between User and GroupByFeatureMean?
- Model evaluation, k-fold cross-validation holdout set?
- Cold start / New Physician (Search), input Physician Features (non-relationship) and Recommend Based on User-User Similarity?
- Problem a good fit with Collaborative Filtering?
- Problem a good fit for UVD/NMF + SGD? k = set of indices of known rating?
- Work towards similar ends by different means (similarity x factorization)?

# Graph Theory
- Communities
- Link Prediction Based on Common Connections


# Graphlab
https://turi.com/learn/userguide/recommender/choosing-a-model.html
- Explicit data: observations include an actual rating given by the user
  - Predict the rating a user would give a particular item > factorization_recommender (can easily incorporate user or item side features.)
  - Recommend items that it believes the user would rate highly > item_similarity_recommender or ranking_factorization_recommender (later uses side data as well)
- Implicit data: collection of items a user has interacted with.
- Item content data: collection of items with no user interaction data
- Side data: in many cases, additional information about the users or items can improve the quality of the recommendations. For example, including information about the genre and year of a movie can be useful information in recommending movies. We call this type of information user side data or item side data depending on whether it goes with the user or the item.

# Review Repos
- Recommendation Systems
- Recommender Case Study

# Next Steps
- Pipeline
  - Put all raw files on data folder



- Edges Class
  - Takes Referral Files (Year, RelationshipType, Average)
  - Return NPIs with Relationships

  - Takes All Possible NPIs  
  - Returns NPIs Without Relationships

  - Return All Possible Relationships with and without Edges

- Headers Class (?)
  - Returns CSV File with Headers



- Repos for Spark Cluster
- https://github.com/gSchool/dsi-spark-aws/blob/master/pair_part2.md
- https://github.com/gSchool/dsi-solns-g65/tree/master/spark-aws




- Nodes Class
  - Takes NPI File
  - Get more data from Taxonomy Class
  - Gets Coordinates from Geopy
  - Returns All Possible NPIs

- Edges Class
  - Takes All Possible NPIs
  - Takes Referral Files
  - Returns NPIs with and without Relationships
  - Return All Possible Relationships with and without Edges

- Taxonomies Class
  - Takes Taxonomy File
  - Return Description Words Vectorized

Distance Class




-
- Extract Taxonomy Code from
- Vectorize Taxonomy Table CSV (Only for Taxonomy Codes)
- Complete Node Table CSV



- Goal00: next mvp run model on a full year with side data physician categorical variables
- Goal0: map necessary files and work backwards
- Goal1: Edge Table: Get all possible edges and values for each year (which database?)
- Goal2: Node Table: Get all possible nodes to a database
- Goal3: Node Table: Get all possible nodes to a database
- Goal4: Pipeline: Feature engineering NLP Description
- Goal5: Pipeline: Feature engineering Distance



- EDA using Spark? On EMR?
- EDA on NPI dataset
- Vectorize descriptions and EDA on them
- Figure out best way to combine dataset (look at what graphlab takes as input)
- How to deal with nested dictionaries (?)
- Figure out best way to store dataset (csv? database?)
- Use Spark to create combined dataset (?) RDD vs DataFrame(SparkSQL)


- (continue graphlab tutorial / test)
- https://github.com/turi-code/tutorials/blob/master/notebooks/basic_recommender_functionalities.ipynb
- https://github.com/turi-code/tutorials/blob/master/notebooks/recsys_rank_10K_song.ipynb
- Run GraphLab on subsample of data (install graphlab on instance, install spark, view bigdata repos, the ones where we actually do stuff on EC2)
- Run GraphLab on the 2014 referral data
- Combine dataset sample
- EDA on combined dataset
- Recommender System PDF (Netflix)
- Step by step add side data and engineer additional features
- Checkout geopy to get geographic coordinates
- Most common neighbors to compare ranking results


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
        * Provider Organization Name (Legal Business Name) > Dummy Variables
        * Provider Business Practice Location Address City Name > Dummy Variables
        * Provider Business Practice Location Address State Name > Dummy Variables
        * Provider Business Practice Location Address Country Code (If outside US) > Dummy Variables
        * Provider Gender Code > Dummy Variables
        * Healthcare Provider Taxonomy Code_1 > Key for Taxonomy Dataset > Use Most Recent Taxonomy Code?
        * Is Sole Proprietor > Dummy Variables
      * Follow-up MVP Variables
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

## Predictions and Recommendations
* **Given a Physician Predict Current Relationships**
* **Given a Physician Recommend New Relationships**
* **Given a Condition Recommend a Physician**
* **Given a Condition Recommend a a Community of Physicians**

## Web App
* **Search by Physician, Procedure, Condition**
* **Physician Profile**
* **Physician Current Relationships**
* **Physician New Relationships Recommendations**
* **Physician Communities**
* **Procedure Profile**
* **Procedure Physician Recommendations**
* **Procedure Communities Recommendations**
* **Condition Profile**
* **Condition Physician Recommendations**
* **Condition Communities Recommendations**
