const kue = require('kue');
const que = kue.createQueue();

const blacklist = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklist.includes(phoneNumber)) {
    return done(Error (`Phone number ${phoneNumber} is blacklisted`));
  }
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

que.process('push_notification_code_2', 5, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
// que.process('push_notification_code_2', 4, (job, done) => {
//   sendNotification(job.data.phoneNumber, job.data.message, job, done);
// });
// que.process('push_notification_code_2', 3, (job, done) => {
//   sendNotification(job.data.phoneNumber, job.data.message, job, done);
// });
