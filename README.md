# devopstask3
Task Description:
Create container image that’s has Jenkins installed using docker file.
When we launch this image, it should automatically starts Jenkins service in the container.
Deploy a container of this image on top of Kubernetes where we use Kubernetes resources like Pods, ReplicaSet, Deployment, PVC and Service.
Create a job chain of job 1, job2, job 3 and job 4 using build pipeline plugin in Jenkins 
Job 1: Pull the Github repo automatically when some developers push repo to Github.
Job 2: By looking at the code or program file, Jenkins should automatically start the respective language interpreter installed image container to deploy code on top of Kubernetes ( eg. If code is of PHP, then Jenkins should start the container that has PHP already installed )
Expose your pod so that testing team could perform the testing on the pod.
Make the data to remain persistent ( If server collects some data like logs, other user information )
Job 3: Test your app if it is working or not.
Job 4: if app is not working , then send email to developer with error messages and redeploy the application after code is being edited by the developer.
