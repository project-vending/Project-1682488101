python
# AWS Kinesis configuration settings
STREAM_NAME = 'your-kinesis-stream-name'
REGION_NAME = 'us-west-2'

# AWS S3 configuration settings
BUCKET_NAME = 'your-s3-bucket-name'

# other configuration settings
MAX_RECORDS = 1000  # maximum number of records to read from Kinesis stream at a time
INTERVAL_SECONDS = 5  # polling interval for reading data from Kinesis stream

# Streamlit app configuration settings
PAGE_TITLE = 'Real-time GOES Data Processing'
APP_PORT = 8501  # port number for running the Streamlit app
