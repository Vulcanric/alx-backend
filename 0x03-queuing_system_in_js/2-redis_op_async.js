// Connects to the Redis server running on localhost
import { createClient, print } from 'redis';
import { promisify } from 'util';


const client = createClient();


client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});


client.on('ready', () => {
  console.log('Redis client connected to the server');
  
  // Create asynchronous versions of function .set and .get
  const asyncRedisSet = promisify(client.set).bind(client);
  const asyncRedisGet = promisify(client.get).bind(client);

  async function setNewSchool(schoolName, value) {
    try {
      const reply = await asyncRedisSet(schoolName, value);
      print(`Reply: ${reply}`);
    } catch (err) {
      console.log(err);
    }
  }

  async function displaySchoolValue(schoolName) {
    try {
      const reply = await asyncRedisGet(schoolName);
      console.log(reply);
    } catch (err) {
      console.log(err);
    }
  }

  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
});
