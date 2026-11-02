<div align="center">

# 📣 AI Social Media Campaign Manager

**Analyse your audience, generate posts with Gemini and publish to social platforms from one dashboard.**

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"> <img src="https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" alt="Gemini"> <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=white" alt="React"> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white" alt="JavaScript"> <img src="https://img.shields.io/badge/Tailwind%20%C2%B7%20daisyUI-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="Tailwind · daisyUI">

</div>

<p align="center"><img src="assets/home-page.jpeg" alt="AI Social Media Campaign Manager screenshot" width="85%"></p>

## 📌 Overview

Enter a business account's username and the app analyses its audience, generates new posts (text and images) tailored to that audience with Google Gemini, and tracks how the posts perform. It is a Flask REST API with a React dashboard.

## ✨ Features

- **Audience analysis:** followers and engagement data via Twitter and Instagram APIs on RapidAPI
- **Content generation:** post text with Gemini, images via a Stable Diffusion XL endpoint and Unsplash
- **Publishing:** post to X/Twitter through OAuth (`tweetPost.py`), Facebook helpers included
- **Performance metrics:** charts of how published content performs
- **Dashboard:** React + Tailwind/daisyUI front end

## 🚀 Getting Started

```bash
git clone https://github.com/KamranUmer/social-media-campaign.git
cd social-media-campaign
cp .env.example .env               # add your API keys

# Backend (Flask)
cd backend && chmod +x local_setup.sh && ./local_setup.sh && ./local_run.sh

# Frontend (React)
cd ../frontend && npm install && npm run dev
```

API keys are read from environment variables. Never commit your `.env` file.

## 📁 Project Structure

```
social-media-campaign/
├── backend/      # Flask API: analysis, generation, posting
├── frontend/     # React dashboard
├── assets/       # screenshots
└── .env.example  # required environment variables
```

---

<div align="center">

Built by <a href="https://github.com/KamranUmer"><b>Kamran Umer</b></a> · ⭐ Star the repo if you find it useful

</div>
