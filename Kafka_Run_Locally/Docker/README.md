https://hub.docker.com/r/bitnami/kafka
https://www.conduktor.io/kafka/how-to-start-kafka-using-docker/



kafka-topics --create --topic <topic-name> --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092
<br>
kafka-console-producer --topic <topic-name> --bootstrap-server localhost:9092
<br>
kafka-console-consumer --topic <topic-name> --from-beginning --bootstrap-server localhost:9092

<br>
docker exec -it kafka1 /bin/bash

