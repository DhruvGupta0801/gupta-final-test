# Gupta Final Test

This is the final project for INFT 1210, deploying a Flask API server to AWS ECS with a CI/CD pipeline.

## Overview
- **App**: A Flask API with routes `/`, `/host`, and `/ip`.
- **Deployment**: Uses AWS ECS with Fargate, an Application Load Balancer, and Terraform for infrastructure.
- **CI/CD**: GitHub Actions workflow to build and deploy the Docker image to ECR and update the ECS service.