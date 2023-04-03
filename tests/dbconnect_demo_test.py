import sys
sys.dont_write_bytecode = True
import pytest
from dbconnect_demo import getTripsCostingMoreThan


@pytest.fixture
def spark():
    from pyspark.sql import SparkSession
    return SparkSession.builder.getOrCreate()

def test_main(spark):
    df = getTripsCostingMoreThan(spark, 4)
    df = df.groupBy().min("trip_distance").collect()
    assert df[0][0] >= 4

if __name__ == '__main__':
    print(pytest.main(["-p", "no:cacheprovider", "main_test.py"]))
