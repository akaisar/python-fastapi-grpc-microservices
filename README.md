# python-fastapi-grpc-microservices
FastAPI + gRPC + Microservice Application
This repository provides an example of a microservice application built using FastAPI. The application consists of two microservices, one for authentication and another for retrieving Ethereum balance of a given mainnet wallet address. Additionally, there is a database microservice for data storage.

# Features
FastAPI: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python. It is used to develop the microservices' public-facing endpoints and provides excellent performance and scalability.

gRPC: gRPC is a high-performance, open-source framework for building remote procedure call (RPC) APIs. It enables efficient and reliable communication between microservices using protocol buffers (protobuf) for message serialization and deserialization.

Microservice Architecture: The application follows a microservice architecture, where different services are developed and deployed independently. Each microservice has a specific functionality and can be scaled individually, providing flexibility and maintainability.

Authentication Microservice: This microservice handles user registration, login using JWT (JSON Web Tokens), and token validation using gRPC. It provides REST endpoints for registration and login and gRPC endpoints for token validation.

Blockchain Microservice: This microservice retrieves the Ethereum balance of a given mainnet wallet address. It requires a JWT token obtained from the authentication microservice, which should be sent via the x-authic-auth header. It exposes REST endpoints for retrieving the balance.

Database Microservice: The database microservice handles data storage and retrieval. It is used by the authentication microservice to store user information.

# Getting Started
To run the project, follow these steps:

1. Clone the repository:
```
git clone https://github.com/akaisar/python-fastapi-grpd-microservices.git
```

2. Replace the Infura secrets in the code with your own. These secrets are used to interact with the Ethereum blockchain.

3. Navigate to the project directory:
```
cd python-fastapi-grpd-microservices
```
4. Build and start the application using Docker Compose:
```
docker-compose up -d --build
```
5. The microservices will be available at the following endpoints:

    Authentication Microservice: http://localhost:8080/auth/docs

    Blockchain Microservice: http://localhost:8080/blockchain/docs

# Testing the APIs
Once the application is running, you can test the APIs using the provided Swagger UI interface.

Authentication Microservice: Open the Swagger UI for the authentication microservice at http://localhost:8080/auth/docs. Here, you can register a user, login to obtain a JWT token.

Blockchain Microservice: Open the Swagger UI for the blockchain microservice at http://localhost:8080/blockchain/docs. You can use the provided endpoints to retrieve the Ethereum balance of a mainnet wallet address. Remember to include the JWT token obtained from the authentication microservice in the x-authic-auth header.

Contributing
Contributions to this repository are welcome. If you encounter any issues or have ideas for improvements, please open an issue or submit a pull request.
