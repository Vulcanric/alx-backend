// Tracking progress and errors with Kue: The Job creator
import { createQueue } from 'kue';


const queue = createQueue();

// Monitor upcoming events
queue.on("job enqueue", (jobId, jobObj) => { // Job has been added successfully
  console.log("Notification job created:", jobId);
});

queue.on("job complete", (jobId, result) => {
  console.log(`Notification job #${jobId} completed`);
});

queue.on("job failed", (jobId, error) => {
  console.log(`Notification job #${jobId} failed: ${error}`);
});

queue.on("job progress", (jobId, percentage) => {
  console.log(`Notification job #${jobId} ${percentage}% complete`);
});


const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

// Save into queu all the above jobs
jobs.forEach((job) => {
  queue.create('push_notification_code_2', job).save();
});
