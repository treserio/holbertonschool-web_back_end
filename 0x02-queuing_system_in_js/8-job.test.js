import createPushNotificationsJobs from './8-job.js';

const kue = require('kue');
const queue = kue.createQueue();
const expect = require('chai').expect;

describe ('createPushNotificationsJobs test suite', () => {
  // Setup test mode
  before(() => queue.testMode.enter(true));
  afterEach(() => queue.testMode.clear());
  after(() => queue.testMode.exit());

  it('Test that displays error message if not array', () => {
    expect(() => createPushNotificationsJobs('8', queue)).to.throw(Error, 'Jobs is not an array');
    expect(() => createPushNotificationsJobs({'k': 'v'}, queue)).to.throw(Error, 'Jobs is not an array');
    expect(() => createPushNotificationsJobs(8, queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('Test that can create 2 new jobs for the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 1234 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data.phoneNumber).to.equal('4153518780');
    expect(queue.testMode.jobs[1].data).to.deep.equal({
      phoneNumber: '4153518781',
      message: 'This is the code 1234 to verify your account'
    })
  });
});
