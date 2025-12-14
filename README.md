# 🎧 Polly Text-to-Speech Pipeline

**Teaching the cloud to read aloud — automatically.**

This project demonstrates a **serverless, event-driven CI/CD pipeline** that converts written text into audio using **Amazon Polly**, **AWS Lambda**, **API Gateway**, **Amazon S3**, and **GitHub Actions**.

Any time content changes in the repository, an automated workflow deploys Lambda code and triggers text-to-speech generation — producing fresh `.mp3` files without servers, manual uploads, or ML model training.

---

## 🧠 Project Overview

**Pixel Learning Co.** is a digital-first education startup focused on accessibility and automation.

While written course materials worked well, the team wanted to ensure every lesson could also be consumed as audio — supporting learners who prefer listening or require assistive technologies.

Rather than recording audio manually or maintaining complex infrastructure, this project uses **Amazon Polly’s managed text-to-speech service** combined with **GitHub Actions CI/CD workflows** to automatically generate and publish audio whenever content changes.

---

## 🎯 What This Project Does

- 📄 Reads text content from a repository  
- 🗣️ Converts text into natural-sounding speech using Amazon Polly  
- 🎵 Outputs audio as `.mp3` files  
- ☁️ Uploads audio to Amazon S3 using environment-specific prefixes  
- 🔁 Automates deployments and execution with GitHub Actions  
- 🧪 Separates beta and production behavior using PRs vs merges  

---

## 🔁 How the Pipeline Works (High Level)

1. Text content is updated in GitHub  
2. GitHub Actions detects the event  
3. Lambda code is packaged and deployed  
4. API Gateway invokes the appropriate Lambda  
5. Amazon Polly synthesizes speech  
6. The resulting `.mp3` file is uploaded to Amazon S3  

### Workflow Outputs

| GitHub Event   | Environment | S3 Output Path                                |
|----------------|-------------|-----------------------------------------------|
| Pull Request   | Beta        | `s3://<bucket>/polly-audio/beta/<timestamp>.mp3` |
| Merge to main  | Production  | `s3://<bucket>/polly-audio/prod/<timestamp>.mp3` |

---

## 🧪 Environment Separation

This project intentionally mirrors real-world CI/CD practices:

### Beta
- Triggered by pull requests  
- Uses `PollyTextToSpeech_Beta` Lambda  
- Writes only to:  
  `s3://<bucket>/polly-audio/beta/`

### Production
- Triggered by merges to main  
- Uses `PollyTextToSpeech_Prod` Lambda  
- Writes only to:  
  `s3://<bucket>/polly-audio/prod/`

A single codebase is reused, with behavior controlled via environment variables.

---

## 🛠️ Technologies Used

- **Amazon Polly** – Neural text-to-speech  
- **AWS Lambda** – Serverless execution  
- **Amazon API Gateway** – HTTP invocation  
- **Amazon S3** – Audio file storage  
- **GitHub Actions** – CI/CD automation  
- **Python (boto3)** – AWS service integration  
- **IAM** – Secure permissions and least privilege  

---

## ⚙️ Setup & Prerequisites

To run this project yourself, you’ll need:

- An AWS account  
- An S3 bucket (example:  
  `s3://polly-audio-bucket18`  
  )  
- Two Lambda functions:  
  - `PollyTextToSpeech_Beta`  
  - `PollyTextToSpeech_Prod`  
- API Gateway routes:  
  - `POST /beta/synthesize`  
  - `POST /prod/synthesize`  
- GitHub repository secrets:  
  - `AWS_ACCESS_KEY_ID`  
  - `AWS_SECRET_ACCESS_KEY`  
  - `AWS_REGION`  
  - `S3_BUCKET_NAME`  
  - `BETA_API_URL`  
  - `PROD_API_URL`  

---

## ▶️ Testing the Pipeline

### Beta (Pull Request)
1. Create a feature branch  
2. Open a pull request into `main`  
3. GitHub Actions deploys the beta Lambda  
4. Audio appears in:  
   `s3://<bucket>/polly-audio/beta/`

### Production (Merge)
1. Merge the PR into `main`  
2. GitHub Actions deploys the prod Lambda  
3. Audio appears in:  
   `s3://<bucket>/polly-audio/prod/`

---

## ♿ Why This Matters

Accessibility shouldn’t be an afterthought.  

By embedding text-to-speech directly into the CI/CD pipeline, this project ensures audio content is:  
- Always up to date  
- Automatically generated  
- Scalable and cost-effective  
- Easy to maintain  

All without adding operational complexity.

