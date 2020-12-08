import time
import datetime
import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.lang import builder
from kivy.uix.widget import Widget

lastPress = time.time()
timerContainer = []
timesContainer = []
for i in range (5):
    timesContainer.append(lastPress - lastPress)
rotation = 0
positonsy = [0.55, 0.85, 0.85, 0.55, 0.25]
positonsx = [0.2, 0.2, 0.8, 0.8, 0.5]
passedPlayers = []
playersAmount = 0
passLabels = []
pausedButton = Button()
nextButton = Button()
passButton = Button()
number = Label()
firstOfRound = 0
framesContainer = []
activeFramesContainer = []

class TimeLabelLeft(Label):
    pass

class TimeLabelRight(Label):
    pass

class Frame(Label):
    pass

class ActiveFrame(Label):
    pass

class TimerApp(App):

    def build(self):

        Window.clearcolor = (1, 1, 1, 1)
        layout = FloatLayout()

        class FirstButton(Button):
            def __init__(self):
                super(Button, self).__init__()
                self.bind(on_press=self.clickFirstButt)

            def clickFirstButt(self, *args):
                global playersAmount
                global number
                if playersAmount < 5:
                    playersAmount += 1
                if playersAmount > 0:
                    layout.remove_widget(number)
                number = Label(text=str(playersAmount))
                layout.add_widget(number)

        class GoButton(Button):
            def __init__(self):
                super(Button, self).__init__()
                self.bind(on_press=self.clickGoButt)

            def clickGoButt(self, *args):
                begin()
                layout.remove_widget(firstButton)
                layout.remove_widget(goButton)
                global firstOfRound
                global rotation
                rotation = firstOfRound = random.choice(range(playersAmount))
                layout.add_widget(framesContainer[firstOfRound])
                layout.add_widget(activeFramesContainer[firstOfRound])


        class NextButton(Button):
            def __init__(self):
                super(Button, self).__init__()
                self.bind(on_press=self.clickTimerBuilder)

            def clickTimerBuilder(self, *args):
                global rotation
                global lastPress
                global timesContainer
                layout.remove_widget(timerContainer[rotation])
                timeWhenPressed = time.time()
                timesContainer[rotation] = timesContainer[rotation] + timeWhenPressed - lastPress
                if rotation < 2:
                    timerLabel = TimeLabelRight(text=str(datetime.timedelta(seconds=round(timesContainer[rotation]))), size_hint=(0.6, 0.3), pos_hint={"center_x": positonsx[rotation], "center_y": positonsy[rotation]})
                elif rotation == 4:
                    timerLabel = Label(text=str(datetime.timedelta(seconds=round(timesContainer[rotation]))), size_hint=(0.6, 0.3), pos_hint={"center_x": positonsx[rotation], "center_y": positonsy[rotation]})
                else:
                    timerLabel = TimeLabelLeft(text=str(datetime.timedelta(seconds=round(timesContainer[rotation]))), size_hint=(0.6, 0.3), pos_hint={"center_x": positonsx[rotation], "center_y": positonsy[rotation]})
                timerContainer[rotation] = timerLabel
                layout.add_widget(timerContainer[rotation])
                lastPress = timeWhenPressed
                layout.remove_widget(activeFramesContainer[rotation])
                rotation += 1
                print("Rotation v Next " + str(rotation))
                if rotation == playersAmount:
                    rotation = 0
                    print("Rotation v Next po nulovani " + str(rotation))
                while passedPlayers[rotation] == True:
                    rotation +=1
                    if rotation == playersAmount:
                        rotation = 0
                layout.add_widget(activeFramesContainer[rotation])

        class PassButton(Button):
            def __init__(self, **kwargs):
                super(Button, self).__init__(**kwargs)
                self.bind(on_press=self.clickPass)

            def clickPass(self, *args):
                global passedPlayers
                global rotation
                global lastPress
                global timesContainer
                global firstOfRound
                global pausedButton
                layout.remove_widget(timerContainer[rotation])
                layout.remove_widget(activeFramesContainer[rotation])
                timeWhenPressed = time.time()
                timesContainer[rotation] = timesContainer[rotation] + timeWhenPressed - lastPress
                if rotation < 2:
                    timerLabel = TimeLabelRight(text=str(datetime.timedelta(seconds=round(timesContainer[rotation]))),
                                                size_hint=(0.6, 0.3), pos_hint={"center_x": positonsx[rotation],
                                                                                "center_y": positonsy[rotation]})
                elif rotation == 4:
                    timerLabel = Label(text=str(datetime.timedelta(seconds=round(timesContainer[rotation]))),
                                        size_hint=(0.6, 0.3),
                                        pos_hint={"center_x": positonsx[rotation], "center_y": positonsy[rotation]})
                else:
                    timerLabel = TimeLabelLeft(text=str(datetime.timedelta(seconds=round(timesContainer[rotation]))),
                                               size_hint=(0.6, 0.3), pos_hint={"center_x": positonsx[rotation],
                                                                               "center_y": positonsy[rotation]})
                timerContainer[rotation] = timerLabel
                layout.add_widget(timerContainer[rotation])
                lastPress = timeWhenPressed
                passedPlayers[rotation] = True
                passLabels[rotation] = Label(text="PASS", pos_hint={"center_x": positonsx[rotation], "center_y": positonsy[rotation] - 0.15 })
                layout.add_widget(passLabels[rotation])
                print("Rotation v Pass " + str(rotation))
                rotation += 1
                if rotation == playersAmount:
                    rotation = 0
                    print("Rotation v Pass po nulovani " + str(rotation))
                if all(passedPlayers):
                    print("Bingo")
                    pausedButton = PausedButton()
                    layout.add_widget(pausedButton)
                    layout.remove_widget(framesContainer[firstOfRound])
                    firstOfRound += 1
                    if firstOfRound == playersAmount:
                        firstOfRound = 0
                    rotation = firstOfRound
                    layout.add_widget(framesContainer[firstOfRound])
                else:
                    while passedPlayers[rotation] == True:
                        rotation +=1
                        if rotation == playersAmount:
                            rotation = 0
                layout.add_widget(activeFramesContainer[rotation])

        class PausedButton(Button):
            def __init__(self):
                super(Button, self).__init__()
                self.bind(on_press=self.unPauseButt)

            def unPauseButt(self, *args):
                layout.remove_widget(pausedButton)
                for i in range(playersAmount):
                    passedPlayers[i] = False
                    layout.remove_widget(passLabels[i])
                    global lastPress
                    lastPress = time.time()

        firstButton = FirstButton()
        layout.add_widget(firstButton)
        goButton = GoButton()
        layout.add_widget( goButton)

        def begin():
            global nextButton
            global passButton
            nextButton = NextButton()
            passButton = PassButton()
            layout.add_widget(nextButton)
            layout.add_widget(passButton)
            for i in range(playersAmount):
                firstFrame = Frame(text="", size_hint=(0.2, 0.2),
                                   pos_hint={"center_x": positonsx[i], "center_y": positonsy[i]})
                framesContainer.append(firstFrame)

                activeFrame = ActiveFrame(text="", size_hint=(0.2, 0.2),
                                   pos_hint={"center_x": positonsx[i], "center_y": positonsy[i]})
                activeFramesContainer.append(activeFrame)

                if i < 2:
                    timerLabel = TimeLabelRight(text=str(datetime.timedelta(seconds=round(timesContainer[i]))),
                                        pos_hint={"center_x": positonsx[i], "center_y": positonsy[i]})
                elif i == 4:
                    timerLabel = Label(text=str(datetime.timedelta(seconds=round(timesContainer[i]))),
                                           pos_hint={"center_x": positonsx[i], "center_y": positonsy[i]})
                else:
                    timerLabel = TimeLabelLeft(text=str(datetime.timedelta(seconds=round(timesContainer[i]))),
                                           pos_hint={"center_x": positonsx[i], "center_y": positonsy[i]})
                timerContainer.append(timerLabel)
                layout.add_widget(timerContainer[-1])

                passedPlayers.append(False)

                passLabels.append(Label)

        return layout

TimerApp().run()




