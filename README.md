# Data

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
    * **Selected Columns**: https://npiregistry.cms.hhs.gov/registry/Json-Conversion-Field-Map
        * NPI
        * Entity Type Code
        * NPI Deactivation Reason Code
        * Provider Organization
        * Provider Name
        * Provider Credential
        * Provider Location
        * Provider Gender
        * Provider Taxonomy Code (1-15) (Primary Taxonomy?) (http://www.wpc-edi.com/reference/codelists/healthcare/health-care-provider-taxonomy-code-set/) (Health Care Provider Taxonomy Codes Codes define a health care service provider type, classification, and area of specialization.) (with description)
        * Provider License Number (1-15)
        * Provider License Number State Code (1-15)
        * Provider Taxonomy Code Switch (1-15)                        
        * Other Provider (?)
        * ...
        * Other Provider Identifier (4x50) (Insurance Provider? Only Medicare?)
        * Is Sole Proprietor
        * Is Organization Subpart
        * Parent Organization
        * Healthcare Provide Taxonomy Group (?) (1-15) (Multi or Single Specialty Group)

NPI records in the downloadable file will also include deactivated health care provider
data. But for these deactivated providers, only the NPI and its deactivation date will be visible in the
downloadable file

### Health Care Provider Taxonomy Code
* **National Uniform Claim Committee**:
http://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40/csv-mainmenu-57
* **Washington Publishing Company**: http://www.wpc-edi.com/reference/codelists/healthcare/health-care-provider-taxonomy-code-set/


# Hypothesis and Questions

## Features
* **Relationships Between Physicians**
    * **Physician Specialty**
        * Can I get relationships between taxonomy codes (specialties)?
        * Can I translate the code to specialty name?
        * Can I get a description of each specialty?
        * Can NLP on that description be used to to create relationships between specialties?
    * **Physician Location**:
        * Can I get the location of physicians?
    * **Insurance Coverage**:
        * Can I get insurance coverage for physicians? Data based on Medicare only claims?

* **Relationships Between Conditions, Procedures and Specialties**:
    * **Conditions**: XXX
    * **Procedures**: XXX
    * **Specialties**: XXX

## Predictions and Recommendations
* **Given a Physician Predict Current Relationships**
* **Given a Physician Recommend New Relationships**
* **Given a Condition Recommend a Physician**
* **Given a Condition Recommend a a Community of Physicians**

## Web App
* **Search by Physician, Procedure, Condition **
* **Physician Profile **
* **Physician Current Relationships **
* **Physician New Relationships Recommendations **
* **Physician Communities **
* **Procedure Profile **
* **Procedure Physician Recommendations **
* **Procedure Communities Recommendations **
* **Condition Profile **
* **Condition Physician Recommendations **
* **Condition Communities Recommendations **

# Week 0
### Objective: Predict Current Relationships and Recommend New Relationships
### Big Data: Start Local
### CSV vs API: API
### MVP: Predict Current Relationships
### Database: MongoDB
### Training: Potentially Use Different Years to Progressively Train the Model
