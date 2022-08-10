const kue = require('kue');
const que = kue.createQueue();

const job = que
  .create('push_notification_code', {
    phoneNumber: 'string',
    message: 'string',
  })
  .save();

job
  .on('enqueue', () => {
    console.log(`Notification job created: ${job.id}`);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed', () => {
    console.log('Notification job failed');
  });
