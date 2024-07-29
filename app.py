from fluvio import (Fluvio, FluvioConfig, TopicSpec, FluvioAdmin)

config = FluvioConfig.new("sc:9003")
config.set_use_spu_local_address(True)

fluvio = Fluvio.connect_with_config(config)

topicSpec = TopicSpec.new_computed(partitions=1, replication=1, ignore=False)

admin = FluvioAdmin.connect_with_config(config)

try:
    admin.create_topic("my-topic", False, topicSpec)
except Exception:
    pass

producer = fluvio.topic_producer('my-topic')

for y in range(1000000000):
    print(f'RECORD {y}')
    producer.send_string(f'RECORD {y}')
