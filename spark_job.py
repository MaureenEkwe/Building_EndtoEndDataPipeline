docker exec -it datapipeline_spark-master_1 \
  spark-submit \
  --master spark://spark-master:7077 \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1,org.apache.kafka:kafka-clients:3.4.0,com.datastax.spark:spark-cassandra-connector_2.12:3.4.1 \
  /opt/bitnami/spark/spark_stream.py