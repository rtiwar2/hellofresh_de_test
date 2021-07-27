from etl.transform import Transform
from etl.extract.extract import Extract
from pyspark.sql import SparkSession


def test_transformer():
    input_file_path = "C:/Users/Lenovo/PycharmProjects/HelloFreshProject/pytest_sample/"
    spark = SparkSession.builder.appName("HelloFreshSparkETLUnitTest").getOrCreate()
    df = Extract().extracter(spark, input_file_path)
    ts_df = Transform().transformer(spark, df)
    assert (ts_df.count() == 3)


if __name__ == '__main__':
    test_transformer()
