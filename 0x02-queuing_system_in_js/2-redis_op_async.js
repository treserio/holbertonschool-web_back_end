const redis = require('redis');
const util = require('util');

const redcli = redis.createClient();

redcli
  .on('connect', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

function setNewSchool(schoolName, value) {
  redcli.set(schoolName, value, redis.print);
}

const displaySchoolValue = util.promisify(function displaySchoolValue(schoolName) {
  redcli.get(schoolName, (e, d) => {
    console.log(d);
  });
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
