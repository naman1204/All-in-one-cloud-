# Cloud Management Web Application

A full-stack cloud management platform designed to enable real-time interaction with AWS services through a web interface. This project focuses on improving cloud resource management, optimizing backend performance, and streamlining deployment workflows using modern DevOps tools.

---

## Features

- Real-time interaction with AWS services using AJAX and Python CGI  
- Optimized backend processing to improve API response times and reduce server load  
- Automated CI/CD pipelines using Jenkins to eliminate manual deployment steps  
- Integrated AWS auto-scaling to improve system reliability and reduce downtime  
- Docker-based containerization for consistent and faster deployments  

---

## Tech Stack

### Frontend
- HTML  
- CSS  
- JavaScript (AJAX)  

### Backend
- Python (CGI)  

### Cloud & DevOps
- AWS (EC2, Auto Scaling)  
- Docker  
- Jenkins  

---

## Architecture Overview

Client (Browser)

↓
HTML/CSS + JavaScript (AJAX)

↓
Python CGI Backend

↓
AWS Services (EC2, Auto Scaling)

↓

Docker Containers + Jenkins CI/CD


---

## Setup & Installation

### Prerequisites
- Python 3.x  
- Docker  
- AWS account  
- Jenkins (optional for CI/CD)  

### Steps

1. Clone the repository
```bash
git clone https://github.com/your-username/cloud-management-app.git
cd cloud-management-app
```
Configure environment variables (AWS credentials, etc.)
Run the application
```bash
python server.py
```
(Optional) Run with Docker
```bash
docker build -t cloud-app .
docker run -p 8080:8080 cloud-app
```
Deployment
Containerized using Docker for portability across environments
Automated deployments through Jenkins pipelines
Hosted on AWS infrastructure with scaling enabled
Key Improvements
Reduced API response time through backend optimizations
Decreased deployment time using containerization
Eliminated manual deployment steps with CI/CD automation
Improved uptime and reliability using AWS auto-scaling
Future Enhancements
Implement authentication and role-based access control
Expand support for additional AWS services
Upgrade frontend using a modern framework (e.g., React)
Add monitoring and logging for observability
Author

Naman Sharma
