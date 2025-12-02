# 🧠 AI Content Creation Assistant

A FastAPI-powered content generation system designed to help users create, refine, and optimize written content across multiple formats.

This project includes:

* A conversational web interface for interactive content creation
* Integration-ready backend to plug in any Large Language Model (OpenAI, etc.)
* Deployment-friendly setup (Vercel Free Tier supported)

---

## ✨ Capabilities

This assistant helps users generate and improve content:

* 📝 Blog posts, articles & long-form content
* 📱 Platform-specific social media posts (Twitter, LinkedIn, Instagram)
* 🛍️ Product descriptions & marketing copy
* ✍️ Editing for clarity, tone & engagement
* 🔍 SEO-optimized headlines, CTAs & meta descriptions
* 🎯 Adapts writing for audience, tone & brand voice
* #️⃣ Provides relevant, trending hashtags

> Designed to support creators, marketers, startups & content teams.

---

## 🧩 Tech Stack

| Component     | Technology                 |
| ------------- | -------------------------- |
| Backend       | FastAPI (Python)           |
| UI Rendering  | Jinja2 Templates           |
| Deployment    | Vercel Serverless          |
| Frontend Chat | HTML + JS (simple chat UI) |

---

## 🚀 Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the backend

```bash
uvicorn api.index:asgi_app --reload
```

App will be running at:

```
http://127.0.0.1:8000/
```

---

## 🌍 Deploy on Vercel

### 1️⃣ Install Vercel CLI

```bash
npm install -g vercel
vercel login
```

### 2️⃣ Deploy

```bash
vercel --prod
```

Vercel will automatically:
✔ Detect `api/index.py`
✔ Deploy as serverless FastAPI
✔ Host UI + API under one domain

---

## 📂 Project Structure

```
project/
│
├─ main.py.py         # FastAPI app entry point
│
├─ templates/
│   ├─ index.html        # Chat UI
│
│
├─ requirements.txt
└─ vercel.json          # Deployment config
```

---

## 🎮 Demo Preview
![alt text](image.png)
---

## 🔧 Customizing the Agent

Modify `SYSTEM_MESSAGE` in your backend to change:

* Personality
* Content style
* Allowed capabilities
* Branding voice

Supports ANY LLM provider via API integration.

---

## 🤝 Contribution

Contributions, feature requests & bug reports are welcome!

1. Fork the repo
2. Create a feature branch
3. PR with a detailed description

---

## ⭐ Support

If this project helps you:

→ Please **star the repo** ⭐
→ Share it with others 💡

---

## 🗣️ Contact

For collaboration or enhancements:
📩 : kiranjb9@gmail.com
🔗 GitHub: kiranjb9

