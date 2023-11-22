### https://kafka.apache.org/quickstart


#### In ubuntu
--Java 8
sudo apt-get update
sudo apt-get install openjdk-8-jdk

### Download the Kafka

https://www.apache.org/dyn/closer.cgi?path=/kafka/3.6.0/kafka_2.13-3.6.0.tgz

$ tar -xzf kafka_2.13-3.6.0.tgz
$ cd kafka_2.13-3.6.0


# Start the ZooKeeper service
$ bin/zookeeper-server-start.sh config/zookeeper.properties

Open another terminal session and run:

# Start the Kafka broker service

$ bin/kafka-server-start.sh config/server.properties

Generate a Cluster UUID
$ KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"

Format Log Directories

$ bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties


Start the Kafka Server
$ bin/kafka-server-start.sh config/kraft/server.properties

