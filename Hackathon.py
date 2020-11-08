import cs112_f20_week10_linter
from cmu_112_graphics import *
from tkinter import *
import random
import pyttsx3
import textwrap
from Jokes import jokes, cleaner
from gordonRamsay import GRNegative
from Motivation import motivation
from DonaldTrump import tweets

engine = pyttsx3.init()

def jokeGen():
    jokeClean = False
    Clean = False
    while jokeClean == False:
        i = random.randint(0,len(jokes) - 1)
        joke = jokes[i]
        temp = joke.lower()
        for word in cleaner:
            if word in temp:
                Clean = False
                break
            else:
                Clean = True
        if Clean:
            jokeClean = True
    return joke

def GRNGen():
  i = random.randint(0, len(GRNegative)-1)
  return GRNegative[i]

def appStarted(app):
  app.grPic = app.loadImage('/Users/raehash/Desktop/CMU Freshman Year/15-112/Hackathon/GR.jpeg')
  app.grQuote = False
  app.trumpPic = app.loadImage('/Users/raehash/Desktop/CMU Freshman Year/15-112/Hackathon/Trump.jpeg')
  app.trumpList = tweets
  app.trumpQuote = False
  app.johnPic = app.loadImage('/Users/raehash/Desktop/CMU Freshman Year/15-112/Hackathon/John.jpeg')
  app.johnQuote = False
  app.motivationPic = app.loadImage('/Users/raehash/Desktop/CMU Freshman Year/15-112/Hackathon/Motivation.jpeg')
  app.motivationList = motivation
  app.motivationQuote = False
  app.kosbiePic = app.loadImage('/Users/raehash/Desktop/CMU Freshman Year/15-112/Hackathon/pain.jpeg')
  app.kosbieList = ["Carpe Diem"]
  app.kosbieQuote = False
  app.returnStatement = ""

def mousePressed(app,event):
  if 50 < event.x < 200 and 100 < event.y < 200:
    app.returnStatement = GRNGen()
    app.grQuote = True
    app.kosbieQuote = app.trumpQuote = app.johnQuote = app.motivationQuote = False
    engine.say(app.returnStatement)
    engine.runAndWait()
  elif 300 < event.x < 450 and 100 < event.y < 200:
    i = random.randint(0,len(app.trumpList)-1)
    app.returnStatement = app.trumpList[i]
    app.trumpQuote = True
    app.grQuote = app.grQuote = app.johnQuote = app.motivationQuote = False
    engine.say(app.returnStatement)
    engine.runAndWait()
  elif 50 < event.x < 200 and 350 < event.y < 450:
    app.returnStatement = jokeGen()
    app.johnQuote = True
    app.kosbieQuote = app.grQuote = app.trumpQuote = app.motivationQuote = False
    engine.say(app.returnStatement)
    engine.runAndWait()
  elif 300 < event.x < 450 and 350 < event.y < 450:
    i = random.randint(0,len(app.motivationList)-1)
    app.returnStatement = app.motivationList[i]
    app.motivationQuote = True
    app.kosbieQuote = app.trumpQuote = app.grQuote = app.johnQuote = False
    engine.say(app.returnStatement)
    engine.runAndWait()
  elif 175 < event.x < 325 and 225 < event.y < 325:
    i = random.randint(0,len(app.kosbieList)-1)
    app.returnStatement = app.kosbieList[i]
    app.kosbieQuote = True
    app.motivationQuote = app.trumpQuote = app.grQuote = app.johnQuote = False
    engine.say(app.returnStatement)
    engine.runAndWait()



def redrawAll(app,canvas): 
    canvas.create_rectangle(0,0,app.width,app.height, fill = "light yellow")
    canvas.create_image(125,150,image=ImageTk.PhotoImage(app.grPic))
    canvas.create_text(125,210, text = 'Insults')
    canvas.create_image(375,150,image=ImageTk.PhotoImage(app.trumpPic))
    canvas.create_text(375,210, text = 'Tweets')
    canvas.create_image(125,400,image=ImageTk.PhotoImage(app.johnPic))
    canvas.create_text(125,465, text = 'Jokes')
    canvas.create_image(375,400,image=ImageTk.PhotoImage(app.motivationPic))
    canvas.create_text(375,465, text = 'Motivational Quotes')
    canvas.create_image(250,275,image=ImageTk.PhotoImage(app.kosbiePic))
    canvas.create_text(250,335, text = 'Favorite Kosbie Phrases')

    if app.grQuote:
      canvas.create_rectangle(50,202,200,220, outline = "red")
    elif app.trumpQuote:
      canvas.create_rectangle(300,202,450,220, outline = "red")
    elif app.johnQuote:
      canvas.create_rectangle(50,452,200,475, outline = "red")
    elif app.motivationQuote:
      canvas.create_rectangle(300,452,450,475, outline = "red")
    elif app.kosbieQuote:
      canvas.create_rectangle(175,327,325,345, outline = "red")

    canvas.create_text(app.width/2, 30, text = "Quote Generator: The best app for quotes", font = "Palatino 28 bold")
    canvas.create_text(app.width/2, 57, 
    text = "Press the Celebrities Face to get a Quote", font = "Palatino 14")
    canvas.create_text(app.width/2, 75, text = "By Gabriel Medina-Jaudes, Raehash Shah, Carson Stuart, Roshni Surpur",
    font = "Times 12")
    canvas.create_rectangle(50,480,450,540, fill = "light blue")
    wrapper = textwrap.TextWrapper(width = 65)
    finalQuote = wrapper.fill(text = app.returnStatement)
    canvas.create_text(app.width/2,510,text=finalQuote)



def main():
    #cs112_f20_week10_linter.lint()
    runApp(width=500, height=560)

if __name__ == '__main__':
    main()


