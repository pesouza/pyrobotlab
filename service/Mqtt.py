topic = "inmoov/test"
qos = 2
broker = "tcp://broker.mqttdashboard.com:1883" 

clientID = "MRLMQTTpython1"
mqtt1 = Runtime.createAndStart("Mqtt", "Mqtt")
print mqtt1.getDescription()

mqtt1.setBroker(broker)
mqtt1.setQos(qos)
mqtt1.setPubTopic(topic)
mqtt1.setClientId(clientID)
mqtt1.connect(broker)
# authentification mqtt1.connect(broker,"guest","guest")

mqtt1.subscribe("inmoov/test", 0)
mqtt1.publish("hello inmoov world")

mqtt1.addListener("publishMqttMsgString", "python", "publishMqttMsgString")
	 
#  MQTT call-back

def publishMqttMsgString(msg):
	print "message : ",msg[0]
print "topic : ",msg[1]
