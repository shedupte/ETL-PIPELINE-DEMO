from pyspark.sql import SparkSession
import config
import boto3
import json

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("S3 JSON Processing") \
    .getOrCreate()

# Set AWS credentials in the SparkSession configuration
spark.conf.set("spark.hadoop.fs.s3a.access.key", config.aws_access_key_id)
spark.conf.set("spark.hadoop.fs.s3a.secret.key", config.aws_secret_access_key)

# Initialize 'boto3' client for S3 
s3 = boto3.client('s3')

# Use the boto3 client to download S3 data and load data in parsed JSON format
s3_object = s3.get_object(Bucket=config.s3_bucket, Key=config.json_file_key)
json_data = s3_object['Body'].read().decode('utf-8')
parsed_json = json.loads(json_data)

# Create DataFrame from parsed JSON 
df = spark.createDataFrame(parsed_json['listings'])

# Show the DataFrame
df.show()

# Close SparkSession
spark.stop()
