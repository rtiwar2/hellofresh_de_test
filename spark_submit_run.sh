## all below spark config properties are listed just to imply that these can be tweaked and used to handle -
## volume of data or for performance tuning

spark-submit \
--master yarn \
--deploy-mode cluster \
--driver-memory 4g \
--driver-cores 2 \
--executor-memory 16g \
--executor-cores 4 \
--conf "spark.sql.adaptive.enabled=true" \
--conf "spark.driver.maxResultSize=2g" \
--conf "spark.sql.shuffle.partitions=20" \
--conf "spark.executor.memoryOverhead=1024" \
--conf "spark.memory.fraction=0.8" \
--conf "spark.serializer=org.apache.spark.serializer.KryoSerializer" \
--conf "spark.sql.files.maxPartitionBytes=134217728" \
--conf "spark.dynamicAllocation.minExecutors=1" \
--conf "spark.dynamicAllocation.maxExecutors=200" \
--conf "spark.dynamicAllocation.enabled=true" \
--conf "spark.shuffle.service.enabled=true" \
--conf "spark.speculation=true" \
--conf "spark.speculation.multiplier=3" \
--conf "spark.speculation.quantile=0.9" \
--conf "spark.locality.wait=0s" \
--conf "spark.network.timeout=300s" \
--conf "spark.yarn.maxAppAttempts=1" etl/main.py
