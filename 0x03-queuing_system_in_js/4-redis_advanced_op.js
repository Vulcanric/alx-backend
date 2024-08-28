// Implement Hashes
import { createClient, print } from 'redis';

const client = createClient();


client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});


client.on('ready', () => {
  console.log('Redis client connected to the server');

  const keys = ["Portland", "Seattle", "New York", "Bogota", "Cali", "Paris"];
  const values = [50, 80, 20, 20, 40, 2];

  for (let i = 0; i < keys.length; i++) {
    client.hset('HolbertonSchools', keys[i], values[i], (err, reply) => {
      if (err) console.log(err);
      print(`Reply: ${reply}`);
    });
  }

  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) console.log(err);
    console.log(reply);
  });

});
