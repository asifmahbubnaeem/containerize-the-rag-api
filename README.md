# Containerize a RAG API with Docker

**Project Link:** [View Project](http://learn.nextwork.org/projects/ai-devops-docker)

**Author:** asif naeem  
**Email:** asifnaim0123@gmail.com

---

![Image](http://learn.nextwork.org/delighted_chartreuse_swift_buddha's_hand_citron/uploads/ai-devops-docker_x7y8z9a0)

---

## Introducing Today's Project!

In this project, we will demonstrate how to containerize a RAG API, push it and public in dockerHub. We are doing this project to learn containerization and have a hands on experience.

### Key services and concepts

Services we used were docker, dockerHub, ollama, uvicorn, fastAPI, chromaDB. Key concepts we have learnt include how containerization works, how to build a docker image, how to write dockerFile, how to publish our docker image and pull it from public registry.

### Challenges and wins

This project took me approximately 110 minutes. The most challenging part was preparing the app.py file so that RAG api still functions properly when containerized. It was most rewarding to publish our rag-api in the public registry and pull it from there locally and run again.

### Why I did this project

We have done this project because we wanted to have a handson experience about dockerizarion and level up our expertise.

---

## Setting Up the RAG API

In this step, we are  setting up a RAG api using ollama, fastAPI and chromaDB. The RAG API is an API that will use our knowledge base documents to answer questions/requests. How it works: it receives  a request from a user, retrives relevant informations from knowledge base/documents from a chroma database(a vector db) and passes the results to ollama to generate a response with  an LLM. Finally, the api is also responsible for passing the generated response back to the user.

### API setup and workspace

In this step, we are installing docker Desktop. Docker is a containerization platform, which means engineers use it to package their application and all of it's dependencies into a package so that this can run any where same way.

### Dependencies installed

The packages we have installed are:
chromadb                                 1.4.1
fastapi                                  0.128.0
ollama                                   0.6.1
uvicorn                                  0.40.0
FastAPI is used for  building APIs with python. Chroma is used for  store vector embeddings of our knowledge base. Uvicorn is used for running our fastAPI application. It is lioke a server that starts our API and listens for incoming requests. Ollama is used as a gateway to AI language models (LLMs) running locally on our machine. When our RAG api receives a question, it uses ollama to send that question, along with relevant context from our database, to the AI model to generate a human like response

![Image](http://learn.nextwork.org/delighted_chartreuse_swift_buddha's_hand_citron/uploads/ai-devops-docker_c9d0e1f2)

### Local API working

I tested that my API works by runnig a uvicorn server locally and then sending a POST request with a query "what is cucumber?" as follows:
curl -X POST "http://127.0.0.1:8000/query" -G  --data-urlencode "q=what is cucumber?"
 The local API responded with :
Cucumber (pronounced kuh-KUM-ber) is a tool for running automated acceptance tests written in plain language, which improves communication, collaboration, and trust among team members. It's written for anyone on the development team, whether they have experience with coding or not.
 This confirms that our API is working and deliverying the response based on the embeddings we have provided as part of the cucumber.txt document.

![Image](http://learn.nextwork.org/delighted_chartreuse_swift_buddha's_hand_citron/uploads/ai-devops-docker_v5w6x7y8)

---

## Installing Docker Desktop

### Docker Desktop setup

Docker Desktop is a user friendly application that bundles the docker engine(i.e the core of the docker application that creates the container), CLI and other tools into a single package.  We have installed it because using GUI makes it more easy to handle and more visual. Containerization will help my project by packaging our application into a single executable package , so it runs every where without breaking for dependency issues.

### Docker verification

We have verified Docker is working by running following command from terminal:
docker run hello-world
The hello-world container proves that our docker:
1. can download images from internet
2. can create and run containers
3. installation is working correctly

![Image](http://learn.nextwork.org/delighted_chartreuse_swift_buddha's_hand_citron/uploads/ai-devops-docker_i9j0k1l2)

---

## Creating the Dockerfile

In this step, we are containerizing our API! That means building a docker image that packages up our docker API and all of it's dependencies. In order to build that docker image, we have to write a Dockerfile first - that contains the instructions for building the image.

### How the Dockerfile works

A Dockerfile is a set of instruction for building a Docker image. The key instructions in my Dockerfile are as follows: 

FROM tells Docker to specify the base mage, 
COPY is used for copying all the application files from local machine to container
RUN executes the commands during build time
CMD defines which command runs when the container starts.

### Containerized API test results

Testing the API after containerization proved that dockerization is working properly. The difference between running locally and in Docker is that docerization is using the specific dependencies version wheras the local run uses the dependencies version of the system we are running. Containerization helps because it isolates all the packages and application code make it easy to run from local machine to teammembers machine or from cloud.

![Image](http://learn.nextwork.org/delighted_chartreuse_swift_buddha's_hand_citron/uploads/ai-devops-docker_o1p2q3r4)

---

## Building and Running the Container

### Docker image build complete

Building a Docker image involves Docker reading our DockerFile from top to bottom, executing each instruction and then creating a portable, read-only package of our application code, dependencies and settings. This process snapshots the results into a reusable image. We have just verified my Docker image was built successfully by running the command :

docker images | grep rag-api
 which shows :
rag-api   latest  4ef957891c05   2 minutes ago   1.34GB
This confirms that my API is now containerized 
because 

![Image](http://learn.nextwork.org/delighted_chartreuse_swift_buddha's_hand_citron/uploads/ai-devops-docker_p9q0r1s2)

![Image](http://learn.nextwork.org/delighted_chartreuse_swift_buddha's_hand_citron/uploads/ai-devops-docker_x7y8z9a0)

---

## Pushing to Docker Hub

In this project extension, We are pushing to Docker Hub. Docker Hub is a cloud based registry where we can store and share Docker images. We are doing this because we want to store and share our work of containerizing our RAG API, so that this can be used by any one in the world and run/update/modify as per their need.

### Docker Hub push complete

We have pushed to Docker Hub by running the docker push command to push my rag-api image where I have referenced it's new tag that contains my docker hub username. Docker Hub is useful because it is public and free to use, also we can use it to share publicly our created image. The advantage of pushing to a registry is that any one in the world can easily pull the application from central registry and use it.

![Image](http://learn.nextwork.org/delighted_chartreuse_swift_buddha's_hand_citron/uploads/ai-devops-docker_m5n6o7p8)

### Pulling from Docker Hub

Pulling an image from Docker Hub means downloading the image that can be shared/uploaded via dockerHub When I ran docker pull, Docker was installing local copy of the exact image I have just uploaded. The difference between building locally and pulling from Docker Hub is that we can easily run our containerized application from any where in the world right after pulling it. This helps our work to be more flexible and reduces specific machine dependency for various package versioning.

![Image](http://learn.nextwork.org/delighted_chartreuse_swift_buddha's_hand_citron/uploads/ai-devops-docker_f5g6h7i8)

---

---
