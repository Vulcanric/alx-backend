// Defines a Job creation function
import { createQueue } from 'kue';


export default function createPushNotificationsJobs(jobs, queue) {
    if (!(jobs instanceof Array)) throw Error('Jobs is not an array');

    queue.on("job enqueue", (job_id, job) => {
        console.log(`Notification job created: ${job_id}`);
    });
    queue.on("job complete", (job_id, result) => {
        console.log(`Notification job ${job_id} completed -> ${result}`);
    });
    queue.on("job failed", (job_id, error) => {
        console.log(`Notification job ${job_id} failed: ${error}`);
    });
    queue.on("job progress", (job_id, percent) => {
        console.log(`Notification job ${job_id} ${percent}% complete`);
    });

    jobs.forEach((job) => {
        queue.create("push_notification_code_3", job).save();
    });
}
