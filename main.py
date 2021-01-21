from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.core.window import Window
import sys

# Below are all the global variables required for the application

number_of_players = 2

Players = []

toggle_list = []

round_counter = 1

cards_dealt = 7

trump = 'Clubs'

player_entry = 0


# class PlayerInfo stores all the information for each player, such as name, bid and score.
class PlayerInfo:
    Name = ""
    Bid = 0
    Score = 0
    Hands_Won = 0

    # the initialization function simply sets the player's name to an empty string, and all numeric values to zero
    def __init__(self):
        self.Name = ""
        self.Bid = 0
        self.Score = 0
        self.Hands_Won = 0


# class Bid_Win_Layout takes care of the layout of the screen during the game, as well as on the final screen
class Bid_Win_Layout(GridLayout):

    # the initialization function builds the very first bid screen upon starting the game.
    def __init__(self, **kwargs):
        super(Bid_Win_Layout, self).__init__(**kwargs)
        self.clear_widgets()

        self.rows = 3

        self.inside1 = GridLayout(cols=2, size_hint_y=0.1)
        self.inside1.cols = 2
        self.inside1.add_widget(Label(text='Cards Dealt: ' + str(cards_dealt)))
        self.inside1.add_widget(Label(text='Trump Suit: ' + trump))
        self.add_widget(self.inside1)

        self.inside = GridLayout()
        if number_of_players <= 4:
            self.inside.cols = number_of_players
        elif number_of_players >= 4:
            self.inside.rows = 2
        for i in range(number_of_players):
            toggle_list.append(
                ToggleButton(text=f'{Players[i].Name}\nBid: {str(Players[i].Bid)}'
                                  f'\nHands Won: {str(Players[i].Hands_Won)}'
                                  f'\nScore: {str(Players[i].Score)}',
                             group='bid_toggles', background_color=[0, 0.75, 0.75, 1]))
        for i in range(number_of_players):
            self.inside.add_widget(toggle_list[i])

        self.add_widget(self.inside)

        self.inside2 = GridLayout()
        self.inside2.rows = 3
        self.inside2.cols = 3

        self.inside2.zero = Button(text='0', font_size=40, background_color=[0, 1, 0, 1])
        self.inside2.zero.bind(on_press=self.bid_pressed)
        self.inside2.add_widget(self.inside2.zero)

        self.inside2.one = Button(text='1', font_size=40, background_color=[0, 1, 0, 1])
        self.inside2.one.bind(on_press=self.bid_pressed)
        self.inside2.add_widget(self.inside2.one)

        self.inside2.two = Button(text='2', font_size=40, background_color=[0, 1, 0, 1])
        self.inside2.two.bind(on_press=self.bid_pressed)
        self.inside2.add_widget(self.inside2.two)

        self.inside2.three = Button(text='3', font_size=40, background_color=[0, 1, 0, 1])
        self.inside2.three.bind(on_press=self.bid_pressed)
        self.inside2.add_widget(self.inside2.three)

        self.inside2.four = Button(text='4', font_size=40, background_color=[0, 1, 0, 1])
        self.inside2.four.bind(on_press=self.bid_pressed)
        self.inside2.add_widget(self.inside2.four)

        self.inside2.five = Button(text='5', font_size=40, background_color=[0, 1, 0, 1])
        self.inside2.five.bind(on_press=self.bid_pressed)
        self.inside2.add_widget(self.inside2.five)

        self.inside2.six = Button(text='6', font_size=40, background_color=[0, 1, 0, 1])
        self.inside2.six.bind(on_press=self.bid_pressed)
        self.inside2.add_widget(self.inside2.six)

        self.inside2.seven = Button(text='7', font_size=40, background_color=[0, 1, 0, 1])
        self.inside2.seven.bind(on_press=self.bid_pressed)
        self.inside2.add_widget(self.inside2.seven)

        self.inside2.next = Button(text='Next', font_size=40, background_color=[0, 1, 0, 1])
        self.inside2.next.bind(on_press=self.bid_pressed)
        self.inside2.add_widget(self.inside2.next)

        self.add_widget(self.inside2)

        self.inside3 = GridLayout(size_hint_y=1.5)
        self.again = Button(text="Play Again", font_size=40, background_color=[0, 1, 0.1, 1])
        self.quit = Button(text="Quit", font_size=40, background_color=[1, 0, 0.25, 1])

    # update_to_bids is the function that updates the screen so that bids cah be entered, and so that
    # the toggle buttons have the appropriate bid for each player
    def update_to_bids(self):
        self.clear_widgets()
        self.rows = 3

        global cards_dealt
        global trump
        if round_counter == 1 or round_counter == 14:
            cards_dealt = 7
        elif round_counter == 2 or round_counter == 13:
            cards_dealt = 6
        elif round_counter == 3 or round_counter == 12:
            cards_dealt = 5
        elif round_counter == 4 or round_counter == 11:
            cards_dealt = 4
        elif round_counter == 5 or round_counter == 10:
            cards_dealt = 3
        elif round_counter == 6 or round_counter == 9:
            cards_dealt = 2
        elif round_counter == 7 or round_counter == 8:
            cards_dealt = 1

        if round_counter == 1 or round_counter == 6 or round_counter == 11:
            trump = 'Clubs'
        elif round_counter == 2 or round_counter == 7 or round_counter == 12:
            trump = 'Diamonds'
        elif round_counter == 3 or round_counter == 8 or round_counter == 13:
            trump = 'Hearts'
        elif round_counter == 4 or round_counter == 9 or round_counter == 14:
            trump = 'Spades'
        elif round_counter == 5 or round_counter == 10:
            trump = 'No Trump'

        self.inside1 = GridLayout(cols=2, size_hint_y=0.1)
        self.inside1.cols = 2
        self.inside1.add_widget(Label(text='Cards Dealt: ' + str(cards_dealt)))
        self.inside1.add_widget(Label(text='Trump Suit: ' + trump))
        self.add_widget(self.inside1)

        self.inside = GridLayout()
        if number_of_players <= 4:
            self.inside.cols = number_of_players
        elif number_of_players >= 4:
            self.inside.rows = 2
        for i in range(number_of_players):
            toggle_list[i] = (
                ToggleButton(text=f'{Players[i].Name}\nBid: {str(Players[i].Bid)}'
                                  f'\nHands Won: {str(Players[i].Hands_Won)}'
                                  f'\nScore: {str(Players[i].Score)}',
                             group='bid_toggles', background_color=[0, 0.75, 0.75, 1]))
        for i in range(number_of_players):
            self.inside.add_widget(toggle_list[i])

        self.add_widget(self.inside)

        self.inside2 = GridLayout()
        self.inside2.rows = 3
        self.inside2.cols = 3

        self.inside2.zero = Button(text='0', font_size=40, background_color=[0, 1, 0, 1])
        self.inside2.zero.bind(on_press=self.bid_pressed)
        self.inside2.add_widget(self.inside2.zero)

        self.inside2.one = Button(text='1', font_size=40, background_color=[0, 1, 0, 1])
        self.inside2.one.bind(on_press=self.bid_pressed)
        self.inside2.add_widget(self.inside2.one)

        self.inside2.two = Button(text='2', font_size=40, background_color=[0, 1, 0, 1])
        self.inside2.two.bind(on_press=self.bid_pressed)
        self.inside2.add_widget(self.inside2.two)

        self.inside2.three = Button(text='3', font_size=40, background_color=[0, 1, 0, 1])
        self.inside2.three.bind(on_press=self.bid_pressed)
        self.inside2.add_widget(self.inside2.three)

        self.inside2.four = Button(text='4', font_size=40, background_color=[0, 1, 0, 1])
        self.inside2.four.bind(on_press=self.bid_pressed)
        self.inside2.add_widget(self.inside2.four)

        self.inside2.five = Button(text='5', font_size=40, background_color=[0, 1, 0, 1])
        self.inside2.five.bind(on_press=self.bid_pressed)
        self.inside2.add_widget(self.inside2.five)

        self.inside2.six = Button(text='6', font_size=40, background_color=[0, 1, 0, 1])
        self.inside2.six.bind(on_press=self.bid_pressed)
        self.inside2.add_widget(self.inside2.six)

        self.inside2.seven = Button(text='7', font_size=40, background_color=[0, 1, 0, 1])
        self.inside2.seven.bind(on_press=self.bid_pressed)
        self.inside2.add_widget(self.inside2.seven)

        self.inside2.next = Button(text='Next', font_size=40, background_color=[0, 1, 0, 1])
        self.inside2.next.bind(on_press=self.bid_pressed)
        self.inside2.add_widget(self.inside2.next)

        self.add_widget(self.inside2)

    # update_to_wins is a member function that updates the screen so that the number of hands won by each player can
    # be entered, it is also called to keep the information on the screen current
    def update_to_wins(self):
        self.clear_widgets()
        self.rows = 3

        global cards_dealt
        global trump
        if round_counter == 1 or round_counter == 14:
            cards_dealt = 7
        elif round_counter == 2 or round_counter == 13:
            cards_dealt = 6
        elif round_counter == 3 or round_counter == 12:
            cards_dealt = 5
        elif round_counter == 4 or round_counter == 11:
            cards_dealt = 4
        elif round_counter == 5 or round_counter == 10:
            cards_dealt = 3
        elif round_counter == 6 or round_counter == 9:
            cards_dealt = 2
        elif round_counter == 7 or round_counter == 8:
            cards_dealt = 1

        if round_counter == 1 or round_counter == 6 or round_counter == 11:
            trump = 'Clubs'
        elif round_counter == 2 or round_counter == 7 or round_counter == 12:
            trump = 'Diamonds'
        elif round_counter == 3 or round_counter == 8 or round_counter == 13:
            trump = 'Hearts'
        elif round_counter == 4 or round_counter == 9 or round_counter == 14:
            trump = 'Spades'
        elif round_counter == 5 or round_counter == 10:
            trump = 'No Trump'

        self.inside1 = GridLayout(cols=2, size_hint_y=0.1)
        self.inside1.cols = 2
        self.inside1.add_widget(Label(text='Cards Dealt: ' + str(cards_dealt)))
        self.inside1.add_widget(Label(text='Trump Suit: ' + trump))
        self.add_widget(self.inside1)

        self.inside = GridLayout()
        if number_of_players <= 4:
            self.inside.cols = number_of_players
        elif number_of_players >= 4:
            self.inside.rows = 2
        for i in range(number_of_players):
            toggle_list[i] = (
                ToggleButton(text=f'{Players[i].Name}\nBid: {str(Players[i].Bid)}'
                                  f'\nHands Won: {str(Players[i].Hands_Won)}'
                                  f'\nScore: {str(Players[i].Score)}',
                             group='bid_toggles', background_color=[0, 0.75, 0.75, 1]))
        for i in range(number_of_players):
            self.inside.add_widget(toggle_list[i])

        self.add_widget(self.inside)

        self.inside2 = GridLayout()
        self.inside2.rows = 3
        self.inside2.cols = 3

        self.inside2.zero = Button(text='0', font_size=40, background_color=[1, 0, 0, 1])
        self.inside2.zero.bind(on_press=self.win_pressed)
        self.inside2.add_widget(self.inside2.zero)

        self.inside2.one = Button(text='1', font_size=40, background_color=[1, 0, 0, 1])
        self.inside2.one.bind(on_press=self.win_pressed)
        self.inside2.add_widget(self.inside2.one)

        self.inside2.two = Button(text='2', font_size=40, background_color=[1, 0, 0, 1])
        self.inside2.two.bind(on_press=self.win_pressed)
        self.inside2.add_widget(self.inside2.two)

        self.inside2.three = Button(text='3', font_size=40, background_color=[1, 0, 0, 1])
        self.inside2.three.bind(on_press=self.win_pressed)
        self.inside2.add_widget(self.inside2.three)

        self.inside2.four = Button(text='4', font_size=40, background_color=[1, 0, 0, 1])
        self.inside2.four.bind(on_press=self.win_pressed)
        self.inside2.add_widget(self.inside2.four)

        self.inside2.five = Button(text='5', font_size=40, background_color=[1, 0, 0, 1])
        self.inside2.five.bind(on_press=self.win_pressed)
        self.inside2.add_widget(self.inside2.five)

        self.inside2.six = Button(text='6', font_size=40, background_color=[1, 0, 0, 1])
        self.inside2.six.bind(on_press=self.win_pressed)
        self.inside2.add_widget(self.inside2.six)

        self.inside2.seven = Button(text='7', font_size=40, background_color=[1, 0, 0, 1])
        self.inside2.seven.bind(on_press=self.win_pressed)
        self.inside2.add_widget(self.inside2.seven)

        self.inside2.next = Button(text='Next', font_size=40, background_color=[1, 0, 0, 1])
        self.inside2.next.bind(on_press=self.win_pressed)
        self.inside2.add_widget(self.inside2.next)

        self.add_widget(self.inside2)

    # update_to_final is only called once per game, at the end to display the final scores, and give the player
    # the option to either play again, or quit
    def update_to_final(self):
        self.clear_widgets()
        self.rows = 3

        self.inside3 = GridLayout(size_hint_y=1.5)
        self.inside3.rows = number_of_players + 1
        self.inside3.add_widget(Label(text='The Final Scores Are:', font_size=40))
        for i in range(number_of_players):
            self.inside3.add_widget(Label(text=Players[i].Name + ': ' + str(Players[i].Score), font_size=40))
        self.add_widget(self.inside3)

        self.again = Button(text="Play Again", font_size=40, background_color=[0, 1, 0.1, 1])
        self.again.bind(on_release=self.same)
        self.add_widget(self.again)

        self.quit = Button(text="Quit", font_size=40, background_color=[1, 0, 0.25, 1])
        self.quit.bind(on_release=done)
        self.add_widget(self.quit)

    # same is called when the player pushes the play again button, it restarts the game with the same players
    # after setting all relevant values to 0
    def same(self, instance):
        global round_counter
        global trump
        for i in range(number_of_players):
            Players[i].Bid = 0
            Players[i].Score = 0
            Players[i].Hands_Won = 0
        round_counter = 1
        trump = 'Clubs'
        self.update_to_bids()

    # win_pressed is called whenever a button is pressed on the screen to select the number of hands,
    # it updates data appropriately depending on the toggle selected and the button pressed.
    def win_pressed(self, instance):
        global round_counter
        try:
            wins = int(instance.text)
            for i in range(number_of_players):
                if toggle_list[i].state == 'down':
                    Players[i].Hands_Won = wins
                    self.update_to_wins()
                    break
        except ValueError:
            net_hands = 0
            for i in range(number_of_players):
                net_hands += Players[i].Hands_Won
            if net_hands != cards_dealt:
                invalidNumberOfHandsWon()
                self.update_to_wins()
                return
            round_counter += 1
            for i in range(number_of_players):
                if Players[i].Bid == Players[i].Hands_Won:
                    Players[i].Score += ((Players[i].Hands_Won * 5) + 5)
                elif Players[i].Bid < Players[i].Hands_Won:
                    Players[i].Score -= (5 * (Players[i].Hands_Won - Players[i].Bid))
                elif Players[i].Bid > Players[i].Hands_Won:
                    Players[i].Score -= (5 * (Players[i].Bid - Players[i].Hands_Won))
            if round_counter <= 14:
                self.update_to_bids()
            else:
                self.update_to_final()

    # bid_pressed is called whenever a button is pressed on the screen to select the bids for each player,
    # it updates data appropriately depending on the toggle selected and the button pressed.
    def bid_pressed(self, instance):
        try:
            bid = int(instance.text)
            for i in range(number_of_players):
                if toggle_list[i].state == 'down':
                    Players[i].Bid = bid
                    self.update_to_bids()
                    break
        except ValueError:
            self.update_to_wins()


# class Bid_Win_Page initially displays a button to start the game, and then adds the gridlayout created by
# Bid_Win_Layout so that the game can be played. the gridlayout is added after the Start_Bid member function is called
# when the "Start" button is pressed
class Bid_Win_Page(Screen):
    def Start_Bid(self):
        self.clear_widgets()
        self.add_widget(Bid_Win_Layout())
        nowOnBidPage()


# class PlayersPage allows the user to add the name of each player according to the number of players entered on the
# first screen
class PlayersPage(Screen):
    player_name = ObjectProperty(None)

    # reset clears the text entry window so that another name can be entered
    def reset(self):
        self.player_name.text = ""

    # Submit checks that the name field is not empty, and then adds the name entered to the players list.
    def Submit(self):
        global player_entry
        name = str(self.player_name.text)
        not_filled_in = ""
        if name != not_filled_in:
            Players[player_entry].Name = name
            player_entry += 1
            if player_entry == number_of_players:
                self.reset()
                sm.current = "bids_wins"
            else:
                self.reset()
        else:
            invalidPlayerName()


# class StartPage asks the user to enter a number of players, checks that the number is valid,
# and then proceeds to PlayersPage
class StartPage(Screen):
    n = ObjectProperty(None)

    # Start_Game verifies that the number of players entered is valid, and then proceeds to PlayersPage
    def Start_Game(self):
        try:
            number_players = int(self.n.text)
            not_filled_in = ""
            if number_players != not_filled_in and number_players > 1:
                self.modify_player_num()
                for i in range(number_players):
                    Players.append(PlayerInfo())
                self.reset()
                sm.current = "players"
            else:
                invalidNumberOfPlayers()
                self.reset()
        except ValueError:
            invalidNumberOfPlayers()
            self.reset()

    # reset clears the text entry field
    def reset(self):
        self.n.text = ""

    # modify_player_num updates the global variable number_of_players with the correct number of players as entered
    def modify_player_num(self):
        global number_of_players
        number_of_players = int(self.n.text)


# WindowManager allows for navigation between different screens
class WindowManager(ScreenManager):
    pass


# done ends the program
def done(instance):
    sys.exit()


# each of functions invalidNumberOfPlayers through to nowOnBidPage opens a popup window to either display an error
# message, or to give instructions to the user.
def invalidNumberOfPlayers() -> None:
    pop = Popup(title="Invalid Player Number",
                content=Label(text='Invalid number of players,\n please enter an integer greater than 1.'),
                size_hint=(None, None),
                size=(800, 800))
    pop.open()


def invalidPlayerName() -> None:
    pop = Popup(title="Invalid Player Name",
                content=Label(text='Invalid player name,\n please enter the name\n of one of the players.'),
                size_hint=(None, None),
                size=(800, 800))
    pop.open()


def invalidNumberOfHandsWon() -> None:
    pop = Popup(title="Invalid Number of Hands Won",
                content=Label(text='The number of hands won\ndoes not match the\nnumber of cards dealt.'
                                   '\nPlease enter the number of hands won\nby each player.'),
                size_hint=(None, None),
                size=(800, 800))
    pop.open()


def nowOnBidPage() -> None:
    pop = Popup(title='Now On Bid Page',
                content=Label(text='Please enter the bid\nfor each player,\nthen press "Next" when ready'
                                   '\ngreen buttons mean the current page\nis for entering bids,\n'
                                   'red buttons mean the current page\nis for entering the number of hands won.'),
                size_hint=(None, None),
                size=(800, 800))
    pop.open()


# kv and the builder insure that the kivy file is opened properly
kv = Builder.load_file('score.kv')

# sm is used to set the current screen
sm = WindowManager()

# each of the screens that will be used later is created and named
screens = [StartPage(name="start"), PlayersPage(name="players"), Bid_Win_Page(name="bids_wins")]
for screen in screens:
    sm.add_widget(screen)

# the initial screen is set to start
sm.current = "start"


# class ScoreApp creates the app and changes the background colour
class ScoreApp(App):
    def build(self):
        Window.clearcolor = (0.208, 0.396, 0.302, 1)
        return sm


if __name__ == '__main__':
    ScoreApp().run()
