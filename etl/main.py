from pyspark.sql import SparkSession
from etl.extract.extract import Extract
from etl.transform.transform import Transform
from etl.load.load import Load
import sys
import logging.config
import configparser


if __name__ == '__main__':
    try:
        logging.config.fileConfig("../resources/config/logging.conf")

        logging.info("creating spark session")
        spark = SparkSession.builder.appName("HelloFreshSparkETL").getOrCreate()

        logging.info("reading configs from resources/properties.ini")
        param_config = configparser.ConfigParser()
        param_config.read('../resources/properties.ini')
        input_data_path = param_config.get('FILE_CONFIGS', 'input_data_path')
        output_data_path = param_config.get('FILE_CONFIGS', 'output_data_path')
        logging.info("input_data_path: " + input_data_path)
        logging.info("output_data_path: " + output_data_path)
        # input_data_path = "C:/Users/Lenovo/PycharmProjects/HelloFreshProject/resources/input/"
        # output_data_path = "E:/python_output/output_data"
        # logging.info("input_data_pathn: "+input_data_path)
        # logging.info("output_data_path: " + output_data_path)

        logging.info("Invoking extractor")
        input_df = Extract().extracter(spark, input_data_path)

        logging.info("Invoking transformer")
        transform_df = Transform().transformer(spark, input_df)

        logging.info("Invoking loader")
        Load().loader(spark, transform_df, output_data_path)

        logging.info("end of main function i.e. application")
    except Exception as e:
        logging.error("Error occured in loader function :: " + str(e))
        sys.exit(1)
