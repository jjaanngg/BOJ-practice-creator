# ⚔️ PRD-Creator: BOJ Practice Automation Tool

**PRD-Creator** (Problem Random Defense Creator) is an automation tool designed for creating randomized problem set practices on [Baekjoon Online Judge](https://www.acmicpc.net/), using Solved.ac API and Selenium.

This tool handles the full pipeline from problem sampling to group practice creation, storing history in MongoDB for future reference.

---

## 🔧 Features

- 🔐 Auto login to BOJ with CAPTCHA checkpoint handling  
- 📦 Fetch problems from Solved.ac by tier range (Bronze ~ Platinum)  
- 🎯 Randomized problem selection with filtering (no duplicates)  
- 🗓️ Automatic scheduling by tier (1-week / 2-week periods)  
- 📝 Practice creation on BOJ group page using Selenium  
- 🧠 MongoDB integration for tracking created sets  

---

## 🗂️ Tech Stack

- Python 3.x  
- Selenium WebDriver  
- MongoDB (via pymongo)  
- dotenv, requests

---

## 📁 Project Structure

