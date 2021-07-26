import logging.config

class Extract:
    def extracter(self, spark, input_data_path):
        logging.config.fileConfig("C:/Users/Lenovo/PycharmProjects/HelloFreshProject/resources/config/logging.conf")
        logging.info("Inside Extract.extracter() function")
        input_df = spark.read.json(input_data_path + "/*.json")
        input_df.createOrReplaceTempView("input_data")
        rtn_df = spark.sql("select cookTime, prepTime from input_data where lower(ingredients) like '%beef%'")
        logging.info("End of Extract.extracter() function")
        return rtn_df
