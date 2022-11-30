from pyspark.sql import SparkSession
import pytest


@pytest.fixture
def spark() -> SparkSession:
    """
    Create a spark session. Unit tests don't have access to the spark global
    """
    return SparkSession.builder.getOrCreate()


def test_spark(spark):
    """
    Example test that needs to run on the cluster to work
    """
    data = spark.sql("select 1").collect()
    assert data[0][0] == 1
