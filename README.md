# LinkedIn Easy Apply Automation

This project automates the process of logging into LinkedIn, searching for filtered job listings, and applying to all jobs with the **Easy Apply** option using the [`browser-use`](https://github.com/browser-use/browser-use) framework and OpenAI's `gpt-4o` model.

---

## 🚀 Features

- Logs into LinkedIn using saved credentials
- Navigates directly to a filtered job search URL
- Iterates through job cards with "Easy Apply"
- Automatically clicks:
  - Easy Apply
  - Next (if required)
  - Submit
- Logs successful applications

---

## 📂 Project Structure

```bash
.
├── example.py       # Main agent script
├── .env             # API keys and credentials
├── README.md        # Project documentation

---

##**REFERENCE**

@software{browser_use2024,
  author = {Müller, Magnus and Žunič, Gregor},
  title = {Browser Use: Enable AI to control your browser},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/browser-use/browser-use}
}
