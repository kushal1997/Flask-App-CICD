# 🚀 CI/CD Pipeline – Jenkins & GitHub Actions

## 📘 Overview

This repository presents two automated CI/CD pipelines for deploying a simple **Flask web application** to an EC2 server.

You will find:
- Jenkins-based CI/CD setup
- GitHub Actions-based CI/CD setup
- Screenshot evidence
- Documented workflows and triggers

---

## 📚 Table of Contents

| Assignment | Title                    | Description                                     | Link                         |
|------------|--------------------------|-------------------------------------------------|------------------------------|
| 1          | Jenkins Pipeline         | CI/CD pipeline using Jenkins                    | [Jenkins README](./1_JenkinsPipeline/README.md) |
| 2          | GitHub Actions Pipeline  | CI/CD pipeline using GitHub Actions             | [GitHub Actions README](./2_GithubActionPipeline/README.md) |

---

## ✅ Assignments & Highlights

### 📌 Part 1: Jenkins CI/CD Pipeline

**Goal**: Build, test, and deploy a Flask application using a Jenkins pipeline.

📂 [`1_JenkinsPipeline`](./1_JenkinsPipeline)  
📜 Files Included:
- `app.py`, `test_app.py`, `jenkinsfile`, `requirements.txt`
- Jenkins pipeline stages: Build → Test → Deploy
- GitHub Webhook Trigger
- Email Notifications on success/failure

📸 Screenshot Highlights:
- Jenkins Setup & Plugins
- Job Configuration
- Auto Build Trigger
- Pipeline Stages
- Flask Output in Browser
- Success & Failed Email Notifications

---

### 📌 Part 2: GitHub Actions CI/CD Pipeline

**Goal**: Automate testing and deployment using GitHub Actions based on branch triggers and tags.

📂 [`2_GithubActionPipeline`](./2_GithubActionPipeline)  
📜 Files Included:
- `app.py`, `test_app.py`, `requirements.txt`, `.github/workflows/main.yml`
- Workflow Jobs: Install → Test → Build → Deploy (Staging & Production)
- Trigger Conditions: `push` to `staging`, `tag` for production
- Secrets managed via GitHub Secrets

📸 Screenshot Highlights:
- Secrets Setup
- Workflow Executions (Staging + Production)
- EC2 Output (Staging + Production)


<br>

---


