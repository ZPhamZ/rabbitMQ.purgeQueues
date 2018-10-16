import pika
import json

def getRbmqParam():
    with open('settingsNonProd.json') as fi:
        settings = json.load(fi)        
        username, password, hostname, port, vhost, rbmqqueue = settings.get('username'), settings.get('password'), settings.get('hostname'), settings.get('port'), settings.get('vhost'), settings.get('rbmqqueue')
        purgeQueues(username, password, hostname, port, vhost, rbmqqueue)
        
def purgeQueues(username, password, hostname, port, vhost, rbmqqueue):
    credentials = pika.PlainCredentials(username, password)
    parameters = pika.ConnectionParameters(hostname,
                                           port,
                                           vhost,
                                           credentials)    
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    with open('file.json') as fi1:
        queueNames = json.load(fi1)        
        for queueName in queueNames:
            channel.queue_purge(queue = queueName)
            print(queueName + " has been purged")
    connection.close()

def main():
    getRbmqParam()

main()
