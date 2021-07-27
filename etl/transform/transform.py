import isodate as isodate
from pyspark.sql.types import IntegerType
import logging.config
import sys


class Transform:
    logging.config.fileConfig("../resources/config/logging.conf")

    def convert_time_in_sec(self, pt):
        return isodate.parse_duration(pt).seconds

    def transformer(self, spark, input_df):
        try:
            logging.info("Inside Transform.transformer() function")

            logging.info("registering function convert_time_in_sec")
            spark.udf.register("convert_time_in_sec", self.convert_time_in_sec, IntegerType())

            input_df.createOrReplaceTempView("input_data")
            rtn_df = spark.sql("""
                select * from
                (
                select 
                    case when total_cook_time < 30 then 'easy'
                        when total_cook_time >= 30 and total_cook_time <= 60 then 'medium'
                        when total_cook_time > 60 then 'hard'
                        else 'undefined'
                    end as difficulty,
                    avg(total_cook_time) as avg_total_cooking_time
                from
                (
                    select 
                        (convert_time_in_sec(cookTime) + convert_time_in_sec(prepTime)) / 60 as total_cook_time
                    from input_data
                )s
                group by 1
                )s1
            """)

            rtn_df.show(truncate=False)
            logging.info("End of Transform.transformer() function")
            return rtn_df
        except Exception as e:
            logging.error("Error occured in transformer function :: " + str(e))
            sys.exit(1)
