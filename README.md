# 🎧 Polly Text-to-Speech Pipeline

**Teaching the cloud to read aloud — automatically.**

This project demonstrates a serverless CI/CD pipeline that converts written text into audio using **Amazon Polly**, **GitHub Actions**, and **Amazon S3**.  
Any time content changes in the repository, an automated workflow generates a fresh `.mp3` file — no servers, no manual uploads, and no machine learning models to train.

The goal of this project is to show how AI services can be cleanly integrated into modern DevOps workflows to improve accessibility while keeping systems lightweight and cost-effective.

---

## 🧠 Project Overview

**Pixel Learning Co.** is a digital-first education startup focused on accessibility and automation.  
While written course materials worked well, the team wanted to ensure that every lesson could also be consumed as audio, supporting learners who prefer listening or require assistive technologies.

Rather than recording audio manually or maintaining complex infrastructure, this project uses **Amazon Polly’s managed text-to-speech service** combined with **GitHub Actions** to automatically generate and publish audio files whenever content is updated.

---

## 🎯 What This Project Does

- 📄 Reads text content from `speech.txt`  
- 🗣️ Uses Amazon Polly to convert text into natural-sounding speech  
- 🎵 Outputs audio as an `.mp3` file  
- ☁️ Uploads audio to Amazon S3 under a structured prefix  
- 🔁 Automates the entire process using GitHub Actions  
- 🧪 Separates beta and production audio using pull request and merge workflows  

---

## 🔁 How the Pipeline Works (High Level)

1. Text content is updated in the repository  
2. GitHub Actions detects the change  
3. A Python script runs using **boto3**  
4. Amazon Polly synthesizes speech  
5. The resulting `.mp3` file is uploaded to Amazon S3  

**Workflow Outputs:**
- Pull Requests → `polly-audio/beta.mp3`  
- Merge to Main → `polly-audio/prod.mp3`  

---

## 🛠️ Technologies Used

- **Amazon Polly** – Text-to-Speech (Neural voices)  
- **Amazon S3** – Audio file storage  
- **GitHub Actions** – CI/CD automation  
- **Python (boto3)** – AWS service integration  
- **IAM** – Secure credential management via GitHub Secrets  

---

## ♿ Why This Matters

Accessibility shouldn’t be an afterthought.  
By automating text-to-speech as part of the CI/CD process, this project ensures that audio content is always **up to date, scalable, and easy to maintain** — without adding operational overhead.

