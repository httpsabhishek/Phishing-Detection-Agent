#  AI-Powered Phishing Email Detector using Gmail & Gemini 2.0 Flash

This project is an intelligent email scanner that analyzes your Gmail inbox using Google's **Gemini 2.0 Flash** LLM. It detects potential phishing attempts by inspecting the **subject, body, and email headers (SPF, DKIM, DMARC)**, and provides an AI-generated classification with reasoning.

##  Features

-  Fetches recent emails from your **Primary** inbox tab (ignores Promotions/Social).
-  Extracts key metadata: subject, sender, body, and headers.
-  Uses **Gemini 2.0 Flash** to analyze the content for phishing.
-  Includes SPF, DKIM, and DMARC analysis from email headers.
-  Classifies emails as **Phishing** or **Legitimate** with explanation.
-  Can be extended into a real-time email monitoring agent or dashboard.


## 🛠 Tech Stack
- Python 3.8+
- [simplegmail](https://github.com/jeremyephron/simplegmail) – Gmail API wrapper
- [LangChain](https://www.langchain.com/) + [langchain-google-genai](https://pypi.org/project/langchain-google-genai/)
- Gemini 2.0 Flash – LLM for intelligent classification

##  Setup Instructions
### 1.  Gmail API Setup
1. Enable Gmail API at: https://console.cloud.google.com/apis/library/gmail.googleapis.com
2. Download `credentials.json` and place it in your project directory.
3. On first run, you'll authenticate via your browser.
### 2. Get Gemini API Key
1. Go to: https://makersuite.google.com/app/apikey
2. Copy the API key.

![Demo of phishing detection](Demo_phishing.gif)
