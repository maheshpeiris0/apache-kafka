import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.kafka.clients.producer.Callback;
import org.apache.kafka.clients.producer.RecordMetadata;

import java.util.Properties;

public class KafkaProducerExample {
    public static void main(String[] args) {
        // Kafka configuration
        Properties props = new Properties();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, System.getenv("BOOTSTRAP_SERVERS")); // Replace with your server
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        props.put("sasl.mechanisms", "PLAIN");
        props.put("security.protocol", "SASL_SSL");
        props.put("sasl.username", System.getenv("SASL_USERNAME")); // Replace with your API key
        props.put("sasl.password", System.getenv("SASL_PASSWORD")); // Replace with your API secret

        // Create Producer instance
        Producer<String, String> producer = new KafkaProducer<>(props);

        // Produce a message
        String topic = "topic_0";
        String messageKey = "5";
        String messageValue = "message hello Java";
        ProducerRecord<String, String> record = new ProducerRecord<>(topic, messageKey, messageValue);

        producer.send(record, new Callback() {
            @Override
            public void onCompletion(RecordMetadata metadata, Exception exception) {
                if (exception == null) {
                    System.out.println("Message sent successfully to partition " + metadata.partition() +
                            " at offset " + metadata.offset());
                } else {
                    System.err.println("Error sending message: " + exception.getMessage());
                }
            }
        });

        // Flush and close the producer
        producer.flush();
        producer.close();
    }
}
