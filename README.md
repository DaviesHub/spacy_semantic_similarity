# Semantic Similarity using SpaCy

## Contents
1. Description
2. Features
3. Package Requirements
4. Installation & Usage
5. Running the Application with Docker
6. Contributions
7. References

## Description
This project demonstrates how to compare words semantically using the SpaCy library in Python.

## Features
The features of this project are as follows:

- Semantic similarity comparison: The project uses the SpaCy library to compare the semantic similarity of words and sentences.

- Docker containerization: The project can be built and run in a Docker container, making it easy to deploy and use across different systems.

- User-friendly: The project includes a README file with clear instructions on how to clone the repo, build the Docker image, and run the container.

## Package Requirements
Package requirements for this app can be seen on the requirements.txt file. Install the required packages by running the
following command on the command line:
'pip install -r requirements.txt'

## Installation & Usage 
To run the script outside of Docker, follow these steps:

1. Install the requirements in the requirements.txt file 
2. Download the 'en_core_web_md' model for SpaCy: python -m spacy download en_core_web_md
3. Clone this repository and navigate to the root directory
4. Run the script: semantic.py

## Running the Application with Docker
To run the script inside Docker, follow these steps:

1. Install Docker on the machine if it is not already installed.
2. Clone this repository and navigate to the root directory.
3. Build the Docker image: docker build -t <'image name'>.
4. Run the Docker container: docker run <'image name'>.
5. The output of the script will be printed to the console.

## Contributions
Contributions to the project are welcome. Please submit a pull request with your changes.

## References
SpaCy documentation: https://spacy.io/
Docker documentation: https://docs.docker.com/