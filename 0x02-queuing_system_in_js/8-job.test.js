import createPushNotificationsJobs from './8-job.js';

const kue = require('kue');
const que = kue.createQueue();
const expect = require('chai').expect;

describe('createPushNotificationsJobs', () => {
  before(() => que.testMode.enter(true));
  afterEach(() => que.testMode.clear());
  after(() => que.testMode.exit());

  it('Errors', () => {
    expect(() => createPushNotificationsJobs('8', que)).to.throw(Error, 'Jobs is not an array');
    expect(() => createPushNotificationsJobs({'k': 'v'}, que)).to.throw(Error, 'Jobs is not an array');
    expect(() => createPushNotificationsJobs(8, que)).to.throw(Error, 'Jobs is not an array');
  });

  it('Test creation of 2 jobs', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 5678 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, que);
    expect(que.testMode.jobs.length).to.equal(2);
    expect(que.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(que.testMode.jobs[0].data.phoneNumber).to.equal('4153518780');
    expect(que.testMode.jobs[1].data.message).to.equal(
      'This is the code 5678 to verify your account'
    );
    que.process('push_notification_code_3', 2, (job, done) => {
      done();
    });
  });
});
