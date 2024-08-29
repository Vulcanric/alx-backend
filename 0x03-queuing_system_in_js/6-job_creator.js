// A Job creator using Kue
import { createQueue } from 'kue';


const queue = createQueue();

const jobData = {
  phoneNumber: "",
  message: "",
}

// Handling upcoming events
/* When a job is created without error */
queue.on("job enqueue", (job_id, job_obj) => {
  console.log("Notification job created:", job_id);
});

queue.on("job complete", (job_id, result) => {
  console.log("Notification job completed");
});

queue.on("job failed", (job_id, error) => {
  console.log("Notification job failed");
});

// Add a job with the job data jobData to the queue
queue.create("push_notification_code", jobData).save();
