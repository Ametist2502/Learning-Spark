from pyspark.sql import SparkSession

session = (
    SparkSession.builder
        .appName("Insert to Postgre")
        .master("local[2]")
        .config("spark.driver.memory", "2g")
        .config("spark.driver.cores", "2")
        .config("spark.sql.shuffle.partitions", "4")
        .config("spark.default.parallelism", "4")
        .config(
            "spark.jars",
            "libs/postgresql-42.7.12.jar"
        )
        .getOrCreate()
)

df = (
    session.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("data/songs.csv")
)

jdbc_url = "jdbc:postgresql://172.23.4.205:5432/poc_oltp"

properties = {
    "user": "postgres",
    "password": "postgres",
    "driver": "org.postgresql.Driver"
}

(
    df.write
    .mode("overwrite")      # append | overwrite
    .jdbc(
        url=jdbc_url,
        table="songs",
        properties=properties
    )
)

# Giữ chương trình chạy một lúc
input("Press Enter to exit...")