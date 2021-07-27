import logging.config
import sys


class Extract:
    logging.config.fileConfig("../resources/config/logging.conf")

    def extracter(self, spark, input_data_path):
        try:
            logging.info("Inside Extract.extracter() function")

            input_df = spark.read.json(input_data_path + "/*.json")
            input_df.createOrReplaceTempView("input_data")
            rtn_df = spark.sql("select cookTime, prepTime from input_data where lower(ingredients) like '%beef%'")

            logging.info("End of Extract.extracter() function")
            return rtn_df
        except Exception as e:
            logging.error("Error occured in extractor function :: " + str(e))
            sys.exit(1)
