const redis = require('redis');

const redcli = redis.createClient();

redcli
  .on('connect', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  })
  .on('message', (chan, msg) => {
    if (chan == 'holberton school channel') console.log(msg);
    if (msg == 'KILL_SERVER') redcli.quit();
  })
  .subscribe('holberton school channel');
