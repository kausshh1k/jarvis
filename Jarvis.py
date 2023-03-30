import pyttsx3 # to initialize the voice (Male/Female)
import speech_recognition as sr # to recognize the voice and to convert it into text
import datetime # to play with the date & time
import wikipedia # to search wikipedia
import webbrowser # to open something in the web browser
import os # to perform all the tasks within the system level
import random # to get random value
import smtplib # to send emails
import pywhatkit # to send whatsapp messages
import sys # to perform any system level operations
import pyautogui # to type, enter, and other keyboard and mouse operations
import getpass # to enter private info
import playsound # to play any mp3 file




'''starting of voice initializing'''

engine = pyttsx3.init('sapi5') # sapi5 is the speech API provided by microsoft
'''Now 'engine' has the access to the voice API'''

voices = engine.getProperty('voices') # to get the available voices
# print(voices[0].id,'\n', voices[1].id,'\n', voices[2].id, voices[3].id) # To print the available voices, voices[0] ---> David, voices[1] ---> Zira
engine.setProperty('voice', voices[0].id) # Setting the voice as David or Zira

'''End of voice'''



'''********  defining global speak command  *******'''

def speak(input_message): # Defining the speak fuction
    '''****** This is a global function that we are going to use in this program
    to help the assistant to speak. ****** 
    
    '''
    engine.runAndWait() # takes a default break after saying.
    engine.say(input_message) # .say() function will speak the given string
    engine.runAndWait() # takes a default break after saying.

'''*********  end of speak command; now we can use this 'speak()' command so 
        that the assistant will speak with the selected voice.   ********'''



def WishMe(): # to wish
    '''****** This is a default function that wish the user at the start. ******'''

    hour = int(datetime.datetime.now().hour) # to get the the hour using '.datetime.now().hour' of the datetime package
    if hour >= 0 and hour < 12:
        print("Hello sir, Good Morning!")
        speak("Hello sir, Good Morning!")
    elif hour >= 12 and hour < 18:
        print("Hello sir, Good Afternoon!")
        speak("Hello sir, Good Afternoon!")
    else:
        print("Hello sir, Good Evening!")
        speak("Hello sir, Good Evening!")
    print("What can I do for you?")
    speak("What can I do for you?")





'''********  To initialize the audio recognizer. This is the google audio recognizer that we're using.  *******'''

def takeCommand(): # voice to text
    '''********* This is the global function that take the input 
    from the user and convert it to the text/string *********'''
    r = sr.Recognizer() # 'r' is the speech recognizing variable
    with sr.Microphone() as source: # opening the '.Microphone()' function of the speech_recognition package
        r.adjust_for_ambient_noise(source) # to eliminate background noices
        print("Listening...") # inside .Microphone() the interpreter will listen to us.
        r.pause_threshold = 1 # gives one second without ending the 'takeCommand()' function
        audio = r.listen(source)

    try: # to avoid exceptions
        print("Recognizing...") # after listening, it will check for google.
        query = r.recognize_google(audio, language = 'en-in') # language is english-India.
        print(f"You: {query}\n") # what you said will be printed

    except Exception as e: # takes all the exceptions as 'e'
        # print("Pardon...")
        # speak("Pardon...") # If found error then return 'Pardon...'
        return 'None' # here 'None' is a string not a boolean
    query = query.lower()
    return query # returns query to 'query' variable

'''********  End of the audio recognizer.  *******'''




def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587) # default gmail
    server.ehlo() # default
    server.starttls() # default
    speak("Enter your email: ")
    email = getpass.getpass("Enter your email: ")
    speak("Enter your password: ")
    passwd = getpass.getpass("Enter your password: ")
    server.login(email, passwd)
    server.sendmail('sendermail',to , content)
    server.close()




def assistant():
    try:
        alarm_time = ''
        chrome = "C://Program Files//Google//Chrome//Application//chrome.exe %s"
        chrome_incognito = "C://Program Files//Google//Chrome//Application//chrome.exe %s --incognito"
        brave_path = "C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe %s" # --incognito
        brave_path_incognito = "C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe %s --incognito" # 
        WishMe()
        # try:
        while True:
            # try:*-
        # if 1:
            query = takeCommand() # query takes audio in text format
            # converting the input voice into lowercase text and sending it to take command function
            if 'wikipedia' in query: # after getting 'query' form 'takeCommand()' we're using it for our use.
                speak('Searching Wikipedia...')
                query = query.replace('wikipedia',"") # search great khali in 
                query = query.replace('search',"") # search great khali in 
                query = query.replace('jarvis',"") # search great khali in 
                results = wikipedia.summary(query, sentences = 2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.get(chrome).open("youtube.com")
                speak("Opening sir!")

            elif 'open whatsapp' in query:
                webbrowser.get(chrome).open("web.whatsapp.com")
                speak("Opening sir!")

            elif 'open google' in query:
                webbrowser.get(chrome).open("google.com")
                speak("Opening sir!")

            elif 'open cbit' in query:
                webbrowser.get(chrome).open("learning.cbit.org.in")
                speak("Opening sir!")

            elif 'open snapchat' in query:
                webbrowser.get(chrome).open("snapchat.com")
                speak("Opening sir!")

            elif 'open incognito' in query:
                webbrowser.get(chrome_incognito).open(" ")
                speak("Opening sir!")

            elif 'play music' in query: # works
                music_dir = 'C:\\Users\\user\\Documents\\Programming\\JARVIS\\songs' 
                songs = os.listdir(music_dir) # creates the list of files from the songs directory
                print(songs) # prints the list of songs
                i = random.randint(0,4)
                os.startfile(os.path.join(music_dir, songs[i])) # just playing the first song, use random module to play random songs.

            # elif 'play next song' in query:
            #     music_dir = 'C:\\Users\\user\\Documents\\Programming\\Batch 36 - 40\\songs' 
            #     songs = os.listdir(music_dir) # creates the list of songs from the songs directory
            #     print(songs) # prints the list of songs
            #     i += 1
            #     try:
            #         os.startfile(os.path.join(music_dir, songs[i])) # just playing the first song, use random module to play random songs.
            #     except Exception as e:
            #         continue
                
            elif "screenshot" in query:
                ss = pyautogui.screenshot()
                n = random.randint(1,1000000)
                path = "C://Users//user//Documents//Programming//JARVIS"
                ss.save(path + f"//_screenshot{n}.png")
                speak("Yes sir! I took the screenshot")

            elif 'what is the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strTime)
                speak(f"Sir, the time is {strTime}")

            elif 'alarm' in query: # this is take the time
                speak('Sir, when should I set the alarm: ')
                alarm_time = input("Time(H:M:S) : ")
                alarm_time = datetime.datetime.strptime(alarm_time, '%H:%M:%S').time()
                # while True:
                #     now = datetime.datetime.now().strftime("%H:%M:%S")
                #     # time = time.strftime("%H:%M:%S")
                #     if now == alarm_time:
                #         playsound.playsound("C:\\Users\\user\\Documents\\Programming\\Batch 36 - 40\\crazy-frog-ringtone-21168.mp3")
                #     elif now>alarm_time:
                #         break

            if alarm_time: # this is to check the time if given any
                # print(type(alarm_time))
                if alarm_time.hour == datetime.datetime.now().hour:
                    if alarm_time.minute +2 >= datetime.datetime.now().minute:
                        if alarm_time.minute <= datetime.datetime.now().minute:
                            speak("Sir, it's time to wake up.")
                            playsound.playsound("C:\\Users\\user\\Documents\\Programming\\Batch 36 - 40\\crazy-frog-ringtone-21168.mp3")
                            alarm_time = None
                    elif datetime.datetime.now().minute <= alarm_time.minute:
                        continue
                    else:
                        speak(f"Sir, you've missed the alarm at {alarm_time.hour}{alarm_time.minute}")
                        alarm_time = ''

            elif 'type' in query:
                speak('Tell me, what shall I type?')
                type_data = takeCommand()
                pyautogui.typewrite(type_data)

            elif 'enter' in query:
                pyautogui.press('enter')

            elif 'open code' in query:
                codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'email' in query:
                try:
                    speak("To whom should I send? \tPlease enter the receivers email: ")
                    to = getpass.getpass("Sir please enter the receiver's email: ")
                    speak("What should I send?")
                    content = takeCommand()
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir, email not sent.")

            elif 'whatsapp message' in query:
                # pywhatkit.sendwhatmsg('+918500260324', 'Message text', 21, 9)
                speak("sir what should I send?")
                message = takeCommand()
                speak("Sir, when should I send the message?")
                time = takeCommand()
                if 'instantly'in time:
                    pywhatkit.sendwhatmsg_instantly('+919390845689', message, wait_time=10)
                elif 'now' in time:
                    pywhatkit.sendwhatmsg_instantly('+919390845689', message, wait_time=10)
                    speak(f"Sir your message is sent")
                # pywhatkit.sendwhatmsg

            # elif 'whatsapp group' in query:
            #     # speak("Sir which group should I select?")
            #     # groupName = takeCommand()
            #     speak("sir what should I send?")
            #     message = takeCommand()
            #     pywhatkit.sendwhatmsg_to_group("D8hp0RsbZIg5yWkJEaelY3", message, time_hour =datetime.datetime.now().hour, time_min=datetime.datetime.now().minute + 1, wait_time=10)

            elif 'sleep' in query:
                print("Okay sir, I'm going to sleep.")
                speak("Okay sir, I'm going to sleep.")
                break

            elif 'you need some rest' in query:
                print("Okay sir, I'm going to sleep.")
                speak("Okay sir, I'm going to sleep.")
                break

            elif 'quit' in query:
                print("Thanks for your time sir, have a good day.")
                speak("Thanks for your time sir, have a good day.")
                sys.exit()
                
    except Exception as e:
        speak("Pardon!")




if __name__=='__main__':
# if __name__ == '__main__':
    def main():
        while True:
            permission = takeCommand()

            if "wake up" in permission:
                assistant()

            elif "hi" in permission:
                assistant()

            elif "goodbye" in permission:
                print("Thanks for your time sir, have a good day.")
                speak("Thanks for your time sir, have a good day.")
                sys.exit()

            elif "quit" in permission:
                print("Thanks for your time sir, have a good day.")
                speak("Thanks for your time sir, have a good day.")
                sys.exit()
    main()