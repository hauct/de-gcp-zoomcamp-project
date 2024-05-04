from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Tạo SparkSession
spark = SparkSession.builder.appName("pyspark_parquet_example").getOrCreate()

# Định nghĩa schema của DataFrame
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

# Tạo dữ liệu mẫu
data = [("Alice", 30), ("Bob", 25), ("Charlie", 40)]

# Tạo DataFrame
df = spark.createDataFrame(data, schema)

# Xuất DataFrame ra file Parquet trên GCS
df.write.parquet("gs://de-gcp-zoomcamp-project_dataproc-source/output.parquet")

# Đọc file Parquet từ GCS
df_read = spark.read.parquet("gs://de-gcp-zoomcamp-project_dataproc-source/output.parquet")

# Hiển thị DataFrame đã đọc
df_read.show()

# Dừng SparkSession
spark.stop()