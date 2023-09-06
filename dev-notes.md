# UdaConnect Projet Notes

## UdaConnect
### Background
Conferences and conventions are hotspots for making connections. Professionals in attendance often share the same interests and can make valuable business and personal connections with one another. At the same time, these events draw a large crowd and it's often hard to make these connections in the midst of all of these events' excitement and energy. To help attendees make connections, we are building the infrastructure for a service that can inform attendees if they have attended the same booths and presentations at an event.

### The Task
You work for a company that is building an app that uses location data from mobile devices. Your company has built a Proof of concept (POC) application to ingest location data named UdaConnect. This POC was built with the core functionality of ingesting location and identifying individuals who have shared close geographic proximity.

Management loved the POC, so now that there is buy-in, we want to enhance this application. You have been tasked to enhance the POC application into a Minimum Viable Product (MVP) to handle the large volume of location data that will be ingested.

To do so, you will refactor this application into a microservice architecture using message passing techniques that you have learned in this course.

## TODO

Management loved the POC, so now that there is buy-in, we want to enhance this application. You have been tasked to enhance the POC application into a Minimum Viable Product (MVP) to handle the large volume of location data that will be ingested.

1. Review Starter Code and evaluate which message passing strategy is suitable
2. Create architecture diagram to document.
   1. It's expected to use Kafka/gRPC and a new REST API
3. Refactor code into microservice (Python)
4. Provide OpenAPI Documentation for APIs
5. Create a Postman Library

## Submission Requirements
The completed project must include:

1. Instructions and commands on how to run the project in the project README.
2. Architecture diagram named docs/architecture_design.png
3. Document on justifying your architecture’s design decisions named docs/architecture_decisions.txt
4. OpenAPI documentation of your new REST API endpoint as docs/openapi.yaml
5. gRPC documentation of your endpoint and how to make a sample request in docs/grpc.txt
6. Screenshot of kubectl get pods as docs/pods_screenshot.png
7. Screenshot of kubectl get services as docs/services_screenshot.png
8. All project code
9. Postman collection of REST API endpoints that you created or modified as docs/postman.json



## Rubric

### Architecture

1. Location
2. Person
3. 