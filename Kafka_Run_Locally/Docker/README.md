https://hub.docker.com/r/bitnami/kafka
https://www.conduktor.io/kafka/how-to-start-kafka-using-docker/



kafka-topics --create --topic <topic-name> --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092
<br>
kafka-console-producer --topic <topic-name> --bootstrap-server localhost:9092
<br>
kafka-console-consumer --topic <topic-name> --from-beginning --bootstrap-server localhost:9092

<br>
docker exec -it kafka1 /bin/bash
<br>
kafka-topics --create --topic quickstart-events --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092

<br>
kafka-console-producer --topic quickstart-events --bootstrap-server localhost:9092

<br>
kafka-console-consumer --topic quickstart-events --from-beginning --bootstrap-server localhost:9092

<br>
kafka-topics.sh --create --topic quickstart-events --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092

<br>


<br>
kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
<br>
kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
