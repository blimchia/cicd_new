# Simple API Deployment to Google Cloud Run

This repository contains the necessary files to deploy and run a simple Flask PubSub containerized application on Google Cloud Run using GitHub Actions. 

The script is indeed quite basic, focusing primarily on essential functionality. It sets up a Flask application to receive messages, decodes and processes them, and includes basic error handling. This serves as a foundation upon which you can build more complex message processing logic tailored to your specific use case.

You can utilize Google Cloud Pub/Sub for real-time message processing. 

# Build and Deploy to Cloud Run

This GitHub Actions workflow automates the process of building and deploying a simple publish-subscribe Python Flask application to Google Cloud Run. The application utilizes Google Cloud Run, Google Cloud Artifact Registry, and Docker for containerization.

## Workflow Overview

- **Trigger:** The workflow is triggered on pushes to the `main` branch.
- **Environment Variables:** The workflow utilizes the following environment variables:
  - `PROJECT_ID`: Google Cloud project ID where the application will be deployed.
  - `GAR_LOCATION`: Google Cloud Artifact Registry location where the container image will be stored.
  - `SERVICE`: Name of the Cloud Run service.
  - `REGION`: Region where the Cloud Run service will be deployed.

## Workflow Steps

1. **Checkout:** Checks out the repository's code.
2. **Google Auth:** Authenticates with Google Cloud using a service account key stored in GitHub Secrets.
3. **Set up Cloud SDK:** Sets up the Google Cloud SDK for authentication and other operations.
4. **Use gcloud CLI:** Verifies the gcloud CLI installation.
5. **Docker Auth and Build:**
   - Authenticates Docker to Google Cloud Artifact Registry.
   - Builds the Docker image for the Flask application.
   - Pushes the Docker image to Google Cloud Artifact Registry.
6. **Deploy to Cloud Run:**
   - Deploys the Docker image to Google Cloud Run.
   - Specifies the Cloud Run service name, image location, region, and allows unauthenticated access.
7. **Show Output:** Displays the URL of the deployed Cloud Run service.

## Additional Steps

1. Ensure that the necessary environment variables (`PROJECT_ID`, `GAR_LOCATION`, `SERVICE`, `REGION`) are correctly set in the GitHub workflow.
2. Push changes to the `main` branch to trigger the workflow.
3. Monitor the workflow execution and check the Cloud Run service URL output for access to the deployed application.

## Integrating with Google Cloud Pub/Sub

To integrate your Flask application with Google Cloud Pub/Sub for real-time message processing, follow these steps:

1. **Set up a Pub/Sub Topic and Subscription:**
   - Create a Pub/Sub topic where you want to publish messages.
   - Create a subscription for the topic. This subscription will be used to receive messages published to the topic.

2. **Deploy Flask Application:**
   - Deploy your Flask application on Google Cloud Run, or any other server of your choice.

3. **Expose Flask Endpoint:**
   - Expose the `/pubsub` endpoint of your Flask application to the internet so that Google Cloud Pub/Sub can send messages to it. Ensure that your server's firewall allows incoming connections on the specified port.

4. **Create a Pub/Sub Publisher:**
   - Create a script or application that publishes messages to the Pub/Sub topic you created in step 1. This script/application could be running on a Google Cloud Function, Compute Engine instance, or any other environment that can publish messages to Pub/Sub.

5. **Publish Messages:**
   - Use the Pub/Sub Publisher created in step 4 to publish messages to the Pub/Sub topic. The messages should be in the format expected by your Flask application, typically a JSON payload containing the message data.

6. **Receive Messages in Flask Application:**
   - When a message is published to the Pub/Sub topic, Pub/Sub will deliver it to the subscription you created. Your Flask application's `/pubsub` endpoint will receive these messages. (Optional: You can integrate with other logic or component to process them, and perform any required actions based on the message content.)
