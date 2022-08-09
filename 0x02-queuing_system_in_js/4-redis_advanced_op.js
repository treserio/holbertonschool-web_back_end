const redis = require('redis');

const redcli = redis.createClient();

const redisVals = {
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2'
}

for (const [k, v] of Object.entries(redisVals)) {
  redcli.hset('HolbertonSchools', k, v, redis.print);
}

redcli.hgetall('HolbertonSchools', (e, r) => {
  console.log(r);
})
