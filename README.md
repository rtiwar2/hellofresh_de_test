**NOTE**:
As I didn't want to use my organisation's laptop (where softwares are already installed with resolved dependency) to avoid code push etc from local to github which may violate organisation policy and invoke vulenarbilities which may cause security issues. **Therefore, I had to work on personal laptop which hasonly Windows 10 installed and get all other required softwares, packages installed to create runnable project. However, there is still some known/existing issue for data write with Windows-10 which could not be resolved despite trying several methods. I am hereby pasting the output which anyway I have printed after transforming the data before load in ETL code.**

+----------+----------------------+
|difficulty|avg_total_cooking_time|
+----------+----------------------+
|medium    |45.0                  |
|hard      |194.3913043478261     |
|easy      |19.625                |
+----------+----------------------+


**spark_submit_run.sh**:
1) This shell script contains spark-submit command for the project to run on yarn cluster. It invoke main python script **etl/main.py** along with other spark config parametrs.
2) If job has to be run locally on client mode then master and deployment-mode property have to be changed accordingly (local and client)
3) Spark resources parameters(driver, executor etc) and other config parameters are kind of indicative place holders which may not be of high importance for small amount of input data but these are really helpful to optimize spark job when it comes to implementation in real world to process TBs of data.

**requirements.txt**: This file has package with required version info required for this project.

**etl/main.py**:   This is main python script which invokes below scripts to execute ETL process
1) **etl/extract/extract.py**: Script contains extract logic for extracting input data with appropriate filter and required columns along with logging and exception handling.
2) **etl/extract/transform.py**: Script contains extract logic for transforming the input data required for target load along with logging and exception handling.
3) **etl/extract/load.py**: Script contains code for data writing to csv from final transformed dataframe along with logging and exception handling. 
    
**resources**: This directory contains further below directories and files.
1) **input**: This directory conatins input json files.
2) **output**: This directory is supposed to have output csv file.
3) **config/logging.conf**: This file contains configuration properties for logging.
4) **properties.ini**: This file can be used for storing all configurations/parameters required for the ETL job at one place (avoiding hardcoding and touching actual code).
    
 **pytest_sample**:
1) This directory has python scripts for unit testing using pytest.
2) It has one of the json inputs file as sample input data file for unit testing.
3) test_extract.py and test_transform.py are the python scripts used for unit testing of extract and transform module.
    
   
    
