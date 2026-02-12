"""
README
======

# Jenkins + Docker Demo Application

This project demonstrates a simple **Flask web application** deployed using **Docker** and automated with **Jenkins pipelines**.

## Features
- Root endpoint (`/`) with a welcome page, links, and a calculator form
- Health check endpoint (`/health`) for monitoring and CI/CD verification
- Dynamic greeting (`/hello/<name>`)
- Calculator API (`/add?a=5&b=7`) with homepage form
- Mock item list API (`/items`) supporting GET and POST

## Project Structure
- src/app.py (this file)
- Dockerfile --- dockerfile for the application
- requirements.txt
- Jenkinsfile -- automate the process of building the docker image and run docker container

