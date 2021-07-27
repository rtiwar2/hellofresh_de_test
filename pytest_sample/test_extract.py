from etl.extract.extract import Extract
from pyspark.sql import SparkSession
import pytest


def test_extractor():
    input_file_path = "C:/Users/Lenovo/PycharmProjects/HelloFreshProject/pytest_sample/"
    spark = SparkSession.builder.appName("HelloFreshSparkETLUnitTest").getOrCreate()
    df = Extract().extracter(spark, input_file_path)
    assert (df.count() == 22)


if __name__ == '__main__':
    test_extractor()
