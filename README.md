# Physician Relationship Search
This project is being developed as a capstone project for Data Science Immersive at Galvanize.
https://www.galvanize.com/san-francisco/data-science

# Results So Far
https://docs.google.com/presentation/d/1bu3FExwoFKlToCH6hGJyhg-ORDFAgX9EinYX5eBYIYs/edit#slide=id.g397c130158_0_168

# Background
In 2017 I went to my same old primary care physician for just another checkup. However, this time we discovered different problems that required me to look for new specialty physicians. Searching the web for doctors based on specialty and location wasn't good enough, I eventually returned to my primary care physician to get recommendations. This story is not unique, how can we make search results better by leveraging physician relationships?

# Goal
Predict Physician Referrals

# Models
- Matrix Factorization
- Factorization Machine

# Datasets

### Physician Shared Patient Patterns
* **Readme**: https://downloads.cms.gov/foia/physician_shared_patient_patterns_technical_requirements.pdf
* **Download**: https://www.cms.gov/Regulations-and-Guidance/Legislation/FOIA/Referral-Data-FAQs.html

### NPI | National Plan and Provider Enumeration System (NPPES)
* **Readme**: https://www.cms.gov/Regulations-and-Guidance/Administrative-Simplification/NationalProvIdentStand/Downloads/Data_Dissemination_File-Readme.pdf
* **Code Values**: https://www.cms.gov/Regulations-and-Guidance/Administrative-Simplification/NationalProvIdentStand/Downloads/Data_Dissemination_File-Code_Values.pdf
* **Download**: http://download.cms.gov/nppes/NPI_Files.html
* **API**: https://npiregistry.cms.hhs.gov/registry/help-api

### Health Care Provider Taxonomy Code
* **National Uniform Claim Committee**:
http://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40/csv-mainmenu-57

# Next Steps

* **Additional Datasets**
  * **Physician Education**
  * **Physician Most Common Procedures**

* **Hyperparameter Optimization**
  * **Topic Modeling**
  * **Feature Importance**

* **Classification Model**
  * **Predict Strong Relationships Between Physicians With Over N Referrals**

* **Web App**
  * **Build Physician Relationship Search Engine**
