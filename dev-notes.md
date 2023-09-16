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

1. Review and Plan

Review the starter project

Determine which message passing strategies would integrate well when refactoring to a microservice architecture.

2. Design and Document
Using the design decisions from the previous step, create an architecture diagram of your microservice architecture showing the services and message passing techniques between them.
Continue to use Kubernetes and maintain the core functionality of the starter project.
Include at least three message passing strategies into your microservice architecture implementing Kafka, gRPC, and either enhancing or creating a RESTful API endpoint.
3. Justify Your Decisions
Write a 2-3 sentence rationale for each message passing strategy to justify your decision.
4. Refactor into Microservices
Refactor the starter code into a microservice architecture.
While microservices can be technology-agnostic, we want to make sure that we use tools that your company is comfortable with. Therefore, this project should be done in Python.
5. Create OpenAPI Documentation
Provide OpenAPI documentation for API endpoints.
6. Create a Postman Library
Provide Postman library for REST endpoints that you created or modified.

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

## Dev Steps

*09-09-2023:*
   * Added Actions file for API Container. Done.

*10-09-2023:*
* Create pod for kafka broker topic "requests"
* Mofidy API People to receive data and forward it to kafka topic "requests"
* Create pod to subscribe and post using gRPC to pod location_api

### Architecture

User requests are received by frontend react api and forwarded to backend using python flask for the following address:

Command below invokes the persons api:
```
http://localhost:30001/api/persons/9/connection?start_date=2020-01-01&end_date=2020-12-30&distance=5
```

```python
class ConnectionDataResource(Resource):
    @responds(schema=ConnectionSchema, many=True)
    def get(self, person_id) -> ConnectionSchema:
        start_date: datetime = datetime.strptime(
            request.args["start_date"], DATE_FORMAT
        )
        end_date: datetime = datetime.strptime(request.args["end_date"], DATE_FORMAT)
        distance: Optional[int] = request.args.get("distance", 5)

        results = ConnectionService.find_contacts(
            person_id=person_id,
            start_date=start_date,
            end_date=end_date,
            meters=distance,
        )
        return results
```

To consume Kafka messages using gRPC in Python, you'll need to follow these steps:

Set up a Kafka consumer: Start by setting up a Kafka consumer in Python using a library like confluent-kafka-python or kafka-python. This will allow you to connect to your Kafka cluster and consume messages from a specific topic.

Define a gRPC service: Next, define a gRPC service in a .proto file. This file will specify the message types and service methods for your gRPC service. You can define a method that will be responsible for receiving Kafka messages.

Generate gRPC code: Use the protoc compiler to generate the gRPC code in Python. This will generate the necessary client and server code based on your .proto file.

Implement the gRPC server: Implement the gRPC server in Python using the generated code. This server will handle incoming gRPC requests and process them accordingly. In this case, it will consume Kafka messages.

Consume Kafka messages in gRPC server: Inside the gRPC server implementation, use the Kafka consumer you set up earlier to consume messages from the Kafka topic. You can then process these messages as needed.

Start the gRPC server: Finally, start the gRPC server and listen for incoming requests. Once the server is running, it will be able to consume Kafka messages using gRPC.

Remember to import the necessary libraries, handle error cases, and ensure that your Kafka and gRPC configurations are properly set up.

I hope this helps! Let me know if you have any further questions.