// A Node-Redis client subscriber
import { createClient } from 'redis';


const subscriberClient = createClient();
const channel = "holberton school channel";

subscriberClient.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});

subscriberClient.on('ready', () => {

  console.log('Redis client connected to the server');

  subscriberClient.subscribe(channel); // Subscribe to channel
  // When message sent from the publisher-client to the channel is received
  subscriberClient.on('message', (channel, message) => {
    console.log(message);

    if (message === "KILL_SERVER") {
      subscriberClient.unsubscribe(channel);
      process.exit();
    }
  });

});
