import google.generativeai as genai
import os


os.environ["API_KEY"] = "AIzaSyA-Nq3sVeNf-Z9WXWfJ5dHbRc5WxLz4WkQ"
genai.configure(api_key=os.environ["API_KEY"])

model1 = genai.GenerativeModel('gemini-1.5-flash')
print('gemini model imported')
