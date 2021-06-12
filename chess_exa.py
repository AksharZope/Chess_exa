import pygame as pg
import speech_recognition as sr
import pyttsx3
import keydict

pg.init()

engine = pyttsx3.init()

screen = pg.display.set_mode((800,600))

background_img = pg.image.load("images/homescreen.jpg")


screen.blit(background_img, (0, 0))
while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_s:


                r = sr.Recognizer()
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)

                    engine.say("Speak Anything :")
                    engine.runAndWait()

                    audio = r.listen(source)

                text = r.recognize_google(audio)
                print("you said ",text)




                for keyword in keydict.keydict:
                    if keyword in text:
                        sayText, image = keydict.keydict[keyword]
                        image = pg.image.load("images/" + image)
                        screen.blit(image,(190,125))

                        pg.display.update()

                        engine.say(sayText)
                        engine.runAndWait()

                              
                    if text == "home":
                        screen.blit(background_img,(0,0))
                



    pg.display.update()
