from simplegmail import Gmail
from simplegmail.query import construct_query
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

gmail = Gmail()

query_params = {
    "newer_than": (1, "day"),
    "unread": True,
} 

query=construct_query(query_params)

full_query = query + " category:primary"

messages = gmail.get_messages(query=full_query)



PHISHING_PROMPT = """
You are a cybersecurity expert. Analyze the following email and determine if it is a phishing attempt.

Consider the following:
1. Sender address and domain.
2. Email subject and content.
3. Technical headers such as SPF, DKIM, and DMARC.

Here is the email:
Subject: {subject}

From: {sender}

Body:
{body}

SPF: {spf}
Authentication-Results : {auth_results}

Respond in the format:
Classification: <Phishing or Legitimate>
Reason: <why?>
"""

def ask_gemini(subject, sender, body):
    prompt = PHISHING_PROMPT.format( subject=subject,
        sender=sender,
        body=body,
        spf=spf,
        auth_results=auth_results
    )
    model = ChatGoogleGenerativeAI(model ='gemini-2.0-flash')
    response = model.invoke(prompt)
    return response.content

for message in messages:
    #print("To: " + message.recipient) 
    #recipient = message.recipient
    #print("From: " + message.sender)
    sender = message.sender
    #print("Subject: " + message.subject)
    subject = message.subject
    headers = message.headers
    spf = headers.get("Received-SPF", "Not Found")
    auth_results = headers.get("Authentication-Results", "Not Found")
    
#    print("Date: " + message.date)
 #   print("Preview: " + message.snippet)
    body = message.plain or "No Body found"
    #print("Message Body: " + str(message.plain))

    result = ask_gemini(subject, sender, body)
    print("\n--- Email Analysis ---")
    print(f"Subject: {subject}")
    print(f"From: {sender}")
    print("Result:", result)