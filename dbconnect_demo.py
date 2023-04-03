def getTripsCostingMoreThan(spark, value):
    df = spark.read.table("samples.nyctaxi.trips")
    df = df.where(f"trip_distance > {value}")
    return df


if __name__ == "__main__":
    from pyspark.sql import SparkSession
    spark = SparkSession.builder.getOrCreate()
    df = getTripsCostingMoreThan(spark, 5)
    df.show()
