# 🇩🇪 Deutsch Vocabulary Trainer

A simple command-line Python application to help practice and build English–German vocabulary.

---

## 📌 Overview

This project allows you to:
- Add new vocabulary words
- Store them in a CSV file
- Practice translations interactively

It is designed as a beginner-friendly Python project with a clean modular structure.

---

## 🚀 Features

- ➕ Add English–German word pairs
- 📂 Store vocabulary in a CSV file
- 🧠 Practice mode to test your knowledge
- 🧱 Modular code structure (separated logic)

---
## 🏗️ Project Structure
deutsch-vocabulary-trainer/
│
├── main.py # Entry point of the program
│
├── functions/
│ ├── init.py
│ ├── menu.py # Handles user menu
│ ├── add_word.py # Logic for adding words
│ ├── practice.py # Practice/quiz logic
│ └── file_handler.py # CSV read/write operations
│
├── vocabulary/
│ └── words.csv # Stores vocabulary data
│
└── README.md
---

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/yourusername/deutsch-vocabulary-trainer.git
cd deutsch-vocabulary-trainer