import paho.mqtt.client as mqtt

ID_DO_USER = 'chat/primeiro_test'
IP_BROKER = 'test.mosquitto.org'
client = mqtt.Client("user321123") # create new instance
print("connecting to broker")
client.connect(IP_BROKER) #connect to
client.publish(ID_DO_USER, 'Galera, aproveita que tem DRINK no bar #borabeber')
