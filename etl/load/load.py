import logging.config
import sys


class Load:
    logging.config.fileConfig("../resources/config/logging.conf")

    def loader(self, spark, transform_df, output_data_path):
        try:
            logging.info("Inside Load.loader() function")
            # logging.info("transform_df.count: " + str(transform_df.count()))
            transform_df.write.mode("overwrite").csv(output_data_path)

            logging.info("End of Load.loader() function")
        except Exception as e:
            logging.error("Error occured in loader function :: " + str(e))
            sys.exit(1)
