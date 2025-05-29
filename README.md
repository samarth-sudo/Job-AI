# 🤖 LinkedIn Auto Apply Bot using browser-use & GPT-4o

This project automates job applications on [LinkedIn](https://www.linkedin.com/jobs/) using the [browser-use](https://github.com/browser-use/browser-use) framework and OpenAI's `gpt-4o` model.

---

## 📌 Features

- ✅ Logs into LinkedIn
- ✅ Navigates to job listings with filters:
  - **Keyword**: `robotics engineer`
  - **Date Posted**: Past 24 hours
  - **Experience Level**: Entry & Associate
  - **Application Type**: Easy Apply
- ✅ Applies automatically to available jobs using pre-filled details

---

## 🛠 Requirements

- Python 3.9+
- OpenAI API Key
- LinkedIn account with resume uploaded
- `browser-use` and `langchain-openai`
- @software{browser_use2024,
  author = {Müller, Magnus and Žunič, Gregor},
  title = {Browser Use: Enable AI to control your browser},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/browser-use/browser-use}
}

### Installation

```bash
pip install browser-use langchain-openai python-dotenv



