import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


collors = [[1,1,1,1], [1,0,0,1], [0,1,0,1], [0,0,1,1], [1,1,0,1], [0.25,0.25,0.25,1]]



collorIndex = 0
listOfPlayers = [False for i in range(6)]
layout = FloatLayout()
listOfButtons =[]
midButtons = []
#isActivePlayer = False

print(listOfPlayers)












"""
    def dontBlinkButton(self, *args):
        self.background_color = collors[self.collorIndex][0],collors[self.collorIndex][1],collors[self.collorIndex][2],collors[self.collorIndex][3]
        print(self.background_color)
"""

class MyApp(App):
    def build(self):

        class myButton(Button):
            def __init__(self, **kwargs):
                super(Button, self).__init__(**kwargs)
                self.background_down = self.background_normal
                self.background_color = 1, 1, 1, 1
                # print(self.background_color)
                # print( myButton" , collorIndex)
                # print(type(collorIndex))
                self.collorIndex = collorIndex
                print("ID vytvoreneho tlacitka je: " + self.id)

                self.bind(on_press=self.pressedPlayerButton)
                # self.bind(on_release=self.dontBlinkButton)

            def pressedPlayerButton(self, *args):


                #listOfPlayers.append(self.id) if self.id not in listOfPlayers else listOfPlayers


                if self.collorIndex == len(collors) - 1:
                    self.collorIndex = 0
                    listOfPlayers[listOfButtons.index(self)] = False
                else:
                    self.collorIndex += 1
                    listOfPlayers[listOfButtons.index(self)] = True
                # print("po zmene", self.collorIndex)
                # print(len(collors))
                self.background_color = collors[self.collorIndex][0], collors[self.collorIndex][1], \
                                        collors[self.collorIndex][2], collors[self.collorIndex][3]
                # print(self.background_color)
                print("Hraje:")
                print(listOfPlayers)

            def finalState(self, *args):
                disabled = True

        class midButton(Button):
            def __init__(self, **kwargs):
                super(Button, self).__init__(**kwargs)
                # self.background_down = self.background_normal
                self.background_color = 1, 1, 1, 0.5
                # print(self.background_color)
                # print( myButton" , collorIndex)
                # print(type(collorIndex))

                self.bind(on_press=self.clickStart)

            def clickStart(self, *args):


                isActivePlayer = False
                print("Je aktivni hrac?" + str(isActivePlayer))
                if sum(listOfPlayers) > 1:

                    while isActivePlayer == False:

                        firstPlayer = random.choice(range(len(listOfPlayers)))
                        print(firstPlayer)
                        isActivePlayer = listOfPlayers[firstPlayer]


                    print("Zacinajici je hrac c.: " + str(firstPlayer + 1))

                    for i in range(len(listOfButtons)):
                        layout.remove_widget(listOfButtons[i])


                    layout.remove_widget(midButtons[0])
                    layout.add_widget(listOfButtons[firstPlayer])
                    layout.add_widget(midButtons[1])
                else:
                    print("NEBYLI VYBRANI ALESPON 2 HRACI")




        class resetButton(Button):
            def __init__(self, **kwargs):
                super(Button, self).__init__(**kwargs)
                # self.background_down = self.background_normal
                self.background_color = 0.8, 0.4, 0.6, 1
                # print(self.background_color)
                # print( myButton" , collorIndex)
                # print(type(collorIndex))

                self.bind(on_press=self.clickReset)


            def clickReset(self, *args):
                print("reset")

                for i in range(len(listOfButtons)):
                    layout.remove_widget(listOfButtons[i])
                    listOfPlayers[i] = False
                listOfButtons.clear()
                print(listOfButtons)
                buildButts()
                layout.add_widget(midButtons[0])
                layout.remove_widget(midButtons[1])





        def buildButts():
            for i in range(0, 6):
                if i <= 2:
                    xPos = 0.2
                    yPos = 0.2 + (i * 0.3)
                else:
                    xPos = 0.8
                    yPos = 0.2 + ((i - 3) * 0.3)

                listOfButtons.append(myButton(text="Player", size_hint=(0.3, 0.2), pos_hint={"center_x": xPos, "center_y": yPos}, id="butt" + str(i + 1)))
                layout.add_widget(listOfButtons[i])

        def buildStartButton():
            midButtons.append(midButton(text="Start", size_hint=(0.1, 0.2), pos_hint={"center_x": 0.5, "center_y": 0.5}))
            midButtons.append(resetButton(text="Reset", size_hint=(0.1, 0.2), pos_hint={"center_x": 0.5, "center_y": 0.5},
                            id=("midButton")))
            layout.add_widget(midButtons[0])
            #layout.add_widget(midButtons[1])

        buildStartButton()

        buildButts()
        return layout
"""
            layout.add_widget(
                myButton(text="Tlacitko", size_hint=(0.3, 0.2), pos_hint={"center_x": xPos, "center_y": yPos}, id="butt" + str(i + 1)))
"""

if __name__ == '__main__':
    MyApp().run()
