# Overview #
This was my final project for my CS456 - Social and Professional Issues (Ethics), where I created an AI chatbot using Google Gemini API key. At first I wanted to create something similar to J.A.R.V.I.S from the Marvel movies, but things didn't go as plan and I had to change the project a little bit. Now it's a text-based chatbot, where it's able to use the API key and gather data before sending it back to the user in a format that they can read. It does take time to do this, so it is slower than most models.

## Environment Setup ##
For this project, I used Visual Studio Code, and was using Python 3.13. There were multiple external packages that were installed that were essential for the functionality of this project. These can be run in the VSCode terminal, as well as a terminal of your choosing:
	- google-genai: This provides the client to connect to the Gemini API
    - `py -m pip install google-genai --upgrade`
	- Flask: Used to create the web server and the UI
    - `py -m pip install Flask`

For the audio and speech, there were different packages installed.
	- speechrecognition: Used for converting speech to text
    - `py -m pip install speechrecognition`
	- pyttsx3: Cross platform text-to-speech library that utilizes the engines that your OS uses
    - `py -m pip install pyttsx3`

 ## API Key Setup ##
 To generate the API key, I used [Google AI Studio](https://aistudio.google.com/welcome?utm_source=google&utm_medium=cpc&utm_campaign=FY25-global-DR-gsem-BKWS-1710442&utm_content=text-ad-none-any-DEV_c-CRE_726057516168-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt-Gemini-Gemini%20API%20Key-KWID_2337809406845-kwd-2337809406845&utm_term=KW_google%20api%20key%20for%20gemini-ST_google%20api%20key%20for%20gemini&gclsrc=aw.ds&gad_source=1&gad_campaignid=20866959509&gbraid=0AAAAACn9t67_UcOr7ckWtvOXljNtzsfl0&gclid=Cj0KCQiA_8TJBhDNARIsAPX5qxRkdaUJSeqhL0n5gVpJquWdY-ur_o78KNAIhXPfPCberACenV0SWZ8aAqiQEALw_wcB). This was used to authenticate the script and to access the Gemini models.

 ## Execution and Configuration ##
 For the API key to run in the script, I had to set the API Key for the script to access it: `set GEMINI_API_KEY=[YOUR_KEY_HERE]`

 To execute the web application, 2 commands were needed. One only needs to be used once for that session. So once the IDE is closed and opened back up again, we have to reset where flask should look to run the program. To set Flask to the main application, this was the command that was used: `set FLASK_APP=app.py`
 app.py is the main file, it can be different for anyone that has done this project before, or if it's just named different.
 To start the web server, we just need to run `flask run`, and it'll set up the frontend, backend, and middleware for all rogram communication. Once it's running, in a web browser, the system can be accessed at `http://127.0.0.1:5000` (or at any url that was set). On that page, you can see how things work and communicate with the model.

 ## Limitations ##
 Granted that this is a chatbot made from a Gemini API key, it does have it's limits. One thing that I mentioned earlier is that it does take a little bit of time to generate answers, especially longer and more in-depth answers for the given user input. Another limit that it has is that if you ask who the model is, it was saying that it was Gemini. (Gaslighting the model didn't work either). So, if you do ask that, it will say that it's an AI model made by Google, which it is.
 Another limit is that it doesn't have any memory. For example, if your talking about a movie in one prompt, and in the next prompt the user gives says "it". The model won't know what "it" is. Also, when the page is refreshed, it loses any data/information that was on the page, since nothing is stored in memory.
