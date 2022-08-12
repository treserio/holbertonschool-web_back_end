function createPushNotificationsJobs(jobs, que) {
  if (!Array.isArray(jobs)) throw Error('Jobs is not an array');
  for (const job of jobs) {
    const j = que.create('push_notification_code_3', job).save();
    try {
      j
        .on('enqueue', () => {
          console.log(`Notification job created: ${j.id}`);
        })
        .on('complete', () => {
          console.log(`Notification job ${j.id} completed`);
        })
        .on('failed', (err) => {
          console.log(`Notification job ${j.id} failed: ${err}`);
        })
        .on('progress', (progress) => {
          console.log(`Notification job ${j.id} ${progress}% complete`);
        });
    } catch (err) {}
  };
};

module.exports = createPushNotificationsJobs;
