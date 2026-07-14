from pyspark.sql import SparkSession

def create_spark_session(
    app_name: str,
    cores: int = 2,
    memory: str = "2g",
):
    return (
        SparkSession.builder
        .appName(app_name)
        .master(f"local[{cores}]")
        .config("spark.driver.memory", memory)
        .config("spark.driver.cores", str(cores))
        .config("spark.sql.shuffle.partitions", str(cores * 2))
        .config("spark.default.parallelism", str(cores * 2))
        .getOrCreate()
    )