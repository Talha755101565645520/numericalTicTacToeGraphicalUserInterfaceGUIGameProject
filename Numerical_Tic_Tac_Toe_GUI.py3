# Talha Hussain
# Graphical User Interface Programming
# Numerical Tic Tac Toe Game Graphical User Interface GUI
# Numerical_Tic_Tac_Toe_GUI.py3

# Import the necessary packages.
import random
import tkinter
from tkinter import *
from tkinter import messagebox

import time

# Create Instructions Window. 
ins=Tk()

import tkinter as Tkinter
from datetime import datetime

# Create and set Variables to default values. 
counter = 00000
running = False

display=""
computer_toggle=0
start_flag='no'
winner_declared=0
instructions_window_flag=0
initial_flag=1
global flag_Score
flag_Score=0
global number_Of_Games_Left
third_Window_Opened='no'
number_used_count=0
repeat_number_flag=0
number_of_games=""
score_in_numerical_tic_tac_toe_game_is_a_draw_or_tie = 0
player_one_score = 0
player_two_score = 0
computer_score=0
number_used = []
toggle = 1
opposite_Toggle = 0
number_of_clicks = 0
multiplayer_or_not = 'no'
retry_window=0
player_one_name="anonymous"
player_two_name="anonymous"
allow=0
open_instruction_window='yes'

# Create the root tk() window. 
root = Tk()
root.title("BOARD FOR NUMERICAL TIC TAC TOE GAME")
root.geometry("790x530")

# Create a new game button and place it in the root window. 
new_game = Button(root, text="NEW GAME", width='13', height='3', font=('Helvetica',13,'bold'), background="yellow", command=lambda: new_game()).place(
    x=640, y=120)

# Create a retry button and place it in the root window. 
retry = Button(root, text="RETRY", width='13', height='3', font=('Helvetica',13,'bold'), background="yellow", command=lambda: retry(),
               state=NORMAL)
retry.pack()
retry.place(x=640, y=230)

# Create an Exit Button. Then, place the exit button in the root window. 
exit = Button(root, text="EXIT", width='13', height='3', font=('Helvetica',13,'bold'), background="yellow", command=lambda: exitfunc())
exit.pack()
exit.place(x=640, y=330)

'''
The Defintion of Function "stop()" is that it stops the game play by setting the global variable 'running' to False.
'''
def stop():
	global running
	running = False

'''
The Definition of Function "retry()" is that it restarts the game and decrements the number of games left. 
'''
def retry():

    global retry_window,score,random_numbers_list,random_numbers_list_used,instructions_window_flag
    global number_Of_Games_Left,number_used,opposite_Toggle,toggle,number_of_clicks,number_of_games,winner_declared,pass_flag
    pass_flag=0
    print("retry values:="+str(number_of_games))
    if  len(number_of_games)>0:
      if number_Of_Games_Left>1 :
       number_Of_Games_Left=number_Of_Games_Left-1

       # Inform the players, the number of times they can 'retry'.
       messagebox.showinfo("Games Left","You can 'RETRY' and now play "+str(number_Of_Games_Left)+" times more.")

       # Create a new set of game buttons. 
       createbuttons()

       # Set gameplay variables to default values. 
       number_used.clear()
       toggle = 1
       opposite_Toggle = 0
       number_of_clicks = 0
       random_numbers_list = [2, 4, 6, 8]
       random_numbers_list_used = []
       winner_declared=0
       pass_flag=1

      else:
      	# Disable the buttons if there are no games left. 
        disablebuttons()
        number_Of_Games_Left=0

        # Inform the user that there are no retrys left. 
        messagebox.showinfo("Sorry! You Can No Longer Retry!", "You cannot retry anymore. Please Press that is use your Computer Mouse to Left-Click on the NEW GAME Button in order to start a New Game of Numerical Tic Tac Toe.")
    else:
    	# Turn off game buttons. 
     disablebuttons()

     # If the instruction window is open, then inform the player that the rules must be accepted first. 
     if open_instruction_window=='yes':

         messagebox.showinfo("Accept rules!", "Please follow the rules in the 'Rules for Numerical Tic Tac Toe' and type the appropriate number in Total Games text box.")
     # If the instruction window is not open, then inform the user that the game has not begun and they must set up the number of games first. 
     else:
      messagebox.showinfo("Don't Retry!", "Type in a Number from 1 through 20 in the Total Games text box first!")
      # If the instruction window flag is set, then implement an exception to try to destroy the scoreboard window. 
    if instructions_window_flag==1 :
     try:
      score.destroy()
      scoreboard()
     except:
      # Build and display the scoreboard window if the scoreboard fails to be destroyed. 
      scoreboard()

'''
The Definition of the new_game() Function is that it restarts the entire game system, rebuilding and reopening the rules window. 
'''
def new_game():
    global flag_Score,retry_window,player_one_score,player_two_score,computer_score,number_used,repeat_number_flag,third_Window_Opened,number_used_count
    global number_Of_Games_Left, number_used, opposite_Toggle, toggle, number_of_clicks,multiplayer_or_not,score_in_numerical_tic_tac_toe_game_is_a_draw_or_tie,number_of_games,computer_toggle
    global random_numbers_list,random_numbers_list_used,instructions_window_flag,start_flag,open_instruction_window,ins,allow,winner_declared
    # Set the variables of the game to their default values. 
    number_of_games = ""
    winner_declared=0
    allow=0
    computer_toggle=0
    instructions_window_flag=0
    score_in_numerical_tic_tac_toe_game_is_a_draw_or_tie = 0
    player_one_score = 0
    player_two_score = 0
    computer_score=0
    retry_window = 0
    number_used.clear()
    toggle = 1
    opposite_Toggle = 0
    number_of_clicks = 0
    multiplayer_or_not = 'no'
    number_Of_Games_Left = 0
    random_numbers_list = [2, 4, 6, 8]
    random_numbers_list_used = []
    number_used_count = 0
    repeat_number_flag = 0
    third_Window_Opened = 'no'

    # Display the "flag_score" value in the console. 
    print(str(flag_Score)+"=value")

    # If the score flag has been set, then implement an exception that attempts to destroy the score window. 
    if flag_Score==1:
       try:
        score.destroy()
        flag_Score=0
       except:
           pass

    # If the start flag is set to 'yes', then implement an attempt to destroy the score window. 
    elif start_flag=='yes':
     try:
        start.destroy()
        start_flag = 'no'
     except:
         pass

    # If the instruction window is not open, then create a new instruction window. 
    if open_instruction_window=='no':
     try:
        global ins
        ins=Tk()
        # Call the instruction window function to fill and display the window. 
        instructionwindow()
        print("open rules file")
     except:
         pass

    # Create a new set up gameplay buttons and disable them. 
    createbuttons()
    disablebuttons()

'''
The Definition of the Function "exitfunc()" is that it destroys all windows and exits the program. 
'''
def exitfunc():

    global start,third_Window_Opened
    root.destroy()

    # If the score is opened, then implement an exception to destroy the score window. 
    if third_Window_Opened=='yes':
        try:
         score.destroy()
        except:
          pass
    # If the game has been started, then implement an exception that attempts to destroy the start window. 
    elif start_flag=='yes':
        try:
         start.destroy()
        except:
            pass

    # If the instruction window is opened, then implement an exception that attempts to destroy the instruction window. 
    elif open_instruction_window=='yes':
     try:
         ins.destroy()
     except:
      pass

     # Implement an exception that attempts to destroy the second root window. 
     try:
         root2.destroy()
     except:
          pass

'''
The Definition of Function "disablebuttons()" is that it disables all nine buttons in the game area within the Numerical Tic Tac Toe Board. 
'''
def disablebuttons():
	# Set each button global state to normal. 
    global button_One,button_Two,button_Three,button_Four,button_Five,button_Six,button_Seven,button_Eight,button_Nine
    button_One.config(state=DISABLED)
    button_Two.config(state=DISABLED)
    button_Three.config(state=DISABLED)
    button_Four.config(state=DISABLED)
    button_Five.config(state=DISABLED)
    button_Six.config(state=DISABLED)
    button_Seven.config(state=DISABLED)
    button_Eight.config(state=DISABLED)
    button_Nine.config(state=DISABLED)


'''
The Definition of Function "enablebutton()" is that it sets each global button state to NORMAL. 
'''
def enablebutton():

    button_One.config(state=NORMAL)
    button_Two.config(state=NORMAL)
    button_Three.config(state=NORMAL)
    button_Four.config(state=NORMAL)
    button_Five.config(state=NORMAL)
    button_Six.config(state=NORMAL)
    button_Seven.config(state=NORMAL)
    button_Eight.config(state=NORMAL)
    button_Nine.config(state=NORMAL)

'''
The Definition of Function "counter_label(label)" is that it sets the value inside the label given to the current time string. In addition, the "counter_label(label)" Function repeats the call every 1000 milliseconds.
'''
def counter_label(label):
	def count():
		# Check to see if the game is running.
		if running:
			global counter,display

			# Convert the counter variable into a timestamp. 
			tt = datetime.utcfromtimestamp(counter)

			# Display the timestamp in "Hour:Minute:Second" format. 
			string = tt.strftime("%H:%M:%S")
			display=string

			# Set the text value of the label to the timestamp. 
			label['text']=display # Or label.config(text=display)

			# Run the count function again after 1 second. 
			label.after(1000, count)
			counter += 1

    # Start the count Function to run until the game stops. 
	count()

'''
The Defintion of the "Start(label)" Function is that it starts the game by setting the global variable 'running' to True and passing the label to the Counter Label Function.
'''
def Start(label):

	global running
	running=True
	counter_label(label)

'''
The Definition of the "Reset(label)" Function is that it resets the global counter variable to 0. 
'''
def Reset(label):
	global counter
	counter=00000


'''
The Definition of Function "scoreboard()" is that it creates the scoreboard window and enables the game to begin. 
'''
def scoreboard():
 global score,label,label_one,label_two,label_three,flag_Score,retry_window,start_flag,number_Of_Games_Left

 # Set the scoreboard variables.
 start_flag = 'no'
 flag_Score=1
 initial_flag=0

 # Create the Score Window and set the title and size. 
 score=Tk()
 score.title("Score Board")
 score.geometry("500x275")

# Enable the game play buttons. 
 enablebutton()

 # If the "retry_window" variable is not set correctly, then destroy the start window. 
 if retry_window!=1:
  start.destroy()

 # Set up the number of games label. 
 label=Label(score,text= "Total Number # of Games You Want to Play: "+str(number_of_games),font=('Times',16,'bold'),anchor='center')
 label_one=Label(score,text="Player 1 Score: "+str(player_one_score)+"/"+str(number_of_games),font=('Times',16,'bold'),anchor='center',foreground='green')

 # Check if we are using a Computer Player. 
 if multiplayer_or_not in ('NO','No','no','nO'):
 	 # Set the label to display the Computer Score. 
     label_two = Label(score, text="Computer Score: " + str(computer_score) + "/" + str(number_of_games),
                font=('Times', 16, 'bold'), anchor='center',foreground='red')

# Set up the score label. 
 else:
  # Set the label to display the second Player Score. 
  label_two=Label(score,text="Player 2 Score: "+str(player_two_score)+"/"+str(number_of_games),font=('Times',16,'bold'),anchor='center',foreground='red')

 # Set the third label to display the Draw Statistics. 
 label_three=Label(score,text="Draw Results!: "+str(score_in_numerical_tic_tac_toe_game_is_a_draw_or_tie)+"/"+str(number_of_games),font=('Times',16,'bold'),anchor='center')

 # Pack all the labels into the window. 
 label.pack()
 label_one.pack()
 label_two.pack()
 label_three.pack()

 # Create the label to handle the stopwatch value. 
 timerlabel = Tkinter.Label(score, text="00:00:00", foreground="blue", background="cyan", font=('Times', 75, 'bold'))
 timerlabel.pack()

 # Create the frame for holding the score. 
 f = Tkinter.Frame(score)

 # Reset the timer label to zero. 
 Reset(timerlabel)

 # Start the label if there are still games to play. 
 if number_Of_Games_Left>=1:
     Start(timerlabel)

 # Pack the Frame into the score window. 
 f.pack(anchor='center', pady=5)

'''
The Definition of the "retrieveValues()" Function takes in the input from the user and parses it into usable instructions. 
'''
def retrieveValues(start,inputgames,inputwithcpur):
    global number_of_games,number_Of_Games_Left,multiplayer_or_not,third_Window_Opened,retry_window

    # Parse the number of games from the value that the player has given. 
    number_of_games = inputgames.get("1.0", "end-1c")

    # Parse whether we will be using a Computer controlled player. 
    with_cpu_requested_value=inputwithcpur.get("1.0", "end-1c")

    # Print debugging information about the values. 
    print("flag start: " + str(initial_flag))
    print(with_cpu_requested_value)
    print(number_of_games)


    # Implement an Exception in order to try to convert the number of games into an integer. Then store the variable "integer_number_of_games" in the variable "number_of_Games_Left".
    try:
     integer_number_of_games = int(number_of_games)
     number_Of_Games_Left = integer_number_of_games

     # Make sure the value is only in the desired range. Inform the player if it is not in the desired range. 
     if integer_number_of_games < 1 or integer_number_of_games > 20:
         messagebox.showinfo("Wrong Input!", "The Value that should be typed in the 'Total Games' text box in 'Initial Information' Window has to be from 1 through 20.")

    except ValueError:
    	# Inform the player that the value is not one that can be parsed into a valid integer. 
        messagebox.showinfo("Wrong Input!", "The Value needs to be a Positive Integer in the 'Total Games' text field that is the 'Total Games' text box in 'Initial Information' Window.")


    # Check to see if the requested multiplayer value is valid and inform the player if it is not. 
    if with_cpu_requested_value not in ('YES','NO','no','yes','Yes','no','nO','yES'):
       messagebox.showinfo("Wrong input","Value of Multiplayer can be either 'yes' or 'no'")

    # If the values are valid, then we start the game and open the scoreboard window. 
    if with_cpu_requested_value in ('YES','NO','no','yes','Yes','no','nO','yES') and (integer_number_of_games >= 1 and integer_number_of_games <= 20):
        multiplayer_or_not = with_cpu_requested_value
        third_Window_Opened='yes'
        scoreboard()
        retry_window = 1

'''
The Definition of the Function initial_information() is that it sets and opens the Initial Information window to retrieve information from the user. 
''' 
def initial_information():
    global start,start_flag,open_instruction_window

    # Set up the initial values. 
    start_flag='yes'
    open_instruction_window = 'no'
    print("flag start: "+str(initial_flag))

    # Build the starting window and set the value as well as its size. 
    start=Tk()
    start.title("Initial Information")
    start.geometry("560x450")

    # Create the labels for the total games and multiplayer inputs and place them on the start window. 
    games=Label(start,text="Total Games: ",font=('Times',11,'bold')).place(x=30,y=30)
    withcpu = Label(start, text="2 Players?: ",font=('Times',11,'bold')).place(x=30, y=120)

    # Create the input for the total games value and place it in the start window. 
    inputgames = Text(start, width=25, height=3,font=('Times', 14, 'bold'))
    inputgames.pack(pady=10)


    # Create the input for the multiplayer value and place it in the start window. 
    inputwithcpu = Text(start, width=25, height=3,font=('Times', 14, 'bold'))
    inputwithcpu.pack()

    # Create the submit button and place it in the start window. 
    submitbutton=Button(start,text="Submit",width=17,height=3,anchor='center',font=('Helvetica',12,'bold'), background='yellow',command=lambda: retrieveValues(start,inputgames,inputwithcpu)).place(x=189,y=185) #x=280, y=185

    # Create the hint labels and place them in the start window.
    hint_One=Label(start,text="HINT 1 :: Type 'yes' if you, the Computer User, want to play Numerical Tic Tac Toe\n     against another Computer User such as your friend, family member,\nrival, etc., otherwise type 'no'.",anchor='center',font=('Times',12)).place(x=20,y=270)

    hint_Two=Label(start,text="HINT 2 :: A Player or Two Players who are the Computer Users can Play a Minimum\n of 1 Game and a Maximum of 20 Games.",font=('Times',12)).place(x=20,y=340)

    # Disable the gameplay buttons. 
    disablebuttons()

'''
The warning() Function shows a message box with the provided message. 
'''
def warning(temp):
    messagebox.showinfo("warning!",temp)

'''
The playerwon() Function informs the players who has won and sets the game state so that the next game can begin. 
'''
def playerwon(temp):
    global number_of_clicks,player_one_score,player_two_score,number_Of_Games_Left,winner_declared,computer_score,toggle,display

    # Set the variable "number_of_clicks" to 0.
    number_of_clicks=0
    print("temp value rn is"+str(temp))

    # If the first player has won, increment player 1 score and update the label. 
    if temp=="PLAYER 1 HAS WON":
        player_one_score=1+player_one_score
        label_one.config(text="Player 1 Score:  "+str(player_one_score)+"/"+str(number_of_games))
        winner_declared=1

        # Stop the current game.
        stop() 
        # Disable the gameplay buttons. 
        disablebuttons()

        # Create and display the congratulations message. 
        congMessage = "Congratulations Player 1, you won and the time it took you to win the Numerical Tic Tac Toe Game is   "
        splitdisplay=display.split(':').pop(0)+" hours, "+display.split(':').pop(1)+" minutes, "+display.split(':').pop(2)+" seconds."

        messagebox.showinfo("WINNER", congMessage + splitdisplay)
    
    # Check if the computer has won the game. 
    elif temp=="Computer HAS WON":
    	# Increment the computer score and update the label. 
        computer_score=computer_score+1
        label_two.config(text="Computer Score: " + str(computer_score) + "/" + str(number_of_games))
        temp="Computer has won"

        # Stop the current game and disable game play buttons. 
        stop()
        disablebuttons()

        # Create and display the congratulations message. 
        splitdisplay = display.split(':').pop(0) + " hours, " + display.split(':').pop(1) + " minutes, " + display.split(':').pop(2) + " seconds."
        congMessage = "Unfortunately the CPU Player, that is the AI Player, the 'Computer' Player won the Numerical Tic Tac Toe Game, and it took "
        messagebox.showinfo("WINNER", congMessage + splitdisplay)        
        #splitdisplay = display.split(':').pop(0) + " hours, " + display.split(':').pop(1) + " minutes, " + display.split(':').pop(2) + " seconds."
    elif temp=="PLAYER 2 HAS WON" :
         player_two_score=1+player_two_score
         label_two.config(text="Player 2 Score: "+str(player_two_score)+"/"+str(number_of_games))
         stop()
         disablebuttons()
         congMessage = "Congratulations Player 2, you won and the time it took you to win the Numerical Tic Tac Toe Game is  "
         splitdisplay = display.split(':').pop(0) + " hours, " + display.split(':').pop(1) + " minutes, " + display.split(':').pop(2) + " seconds."

         messagebox.showinfo("WINNER", congMessage + splitdisplay)

'''
The Definition of Function "draw()" is that it indicates that the game is a Draw and prepares for the next game. 
'''
def draw():
    global number_of_clicks,score_in_numerical_tic_tac_toe_game_is_a_draw_or_tie,label_three,number_Of_Games_Left
    # Stop the game from running. 
    stop()

    # Reset the number of clicks and increment the draw counter. 
    number_of_clicks=0
    score_in_numerical_tic_tac_toe_game_is_a_draw_or_tie=1+score_in_numerical_tic_tac_toe_game_is_a_draw_or_tie
    number_Of_Games_Left = number_Of_Games_Left - 1

    # Update the label with the Draw value and display the message to the player. 
    label_three.config(text="Draw results! :  " + str(score_in_numerical_tic_tac_toe_game_is_a_draw_or_tie)+"/"+str(number_of_games))

    messagebox.showinfo("IT'S A DRAW! IT'S A TIE!","Unfortunately, no one wins this game of Numerical Tic Tac Toe.")

    # Disable the game play buttons. 
    disablebuttons()


'''
The Definition of Function "anywinner()" is that it checks to see if the current player is the winner of the game. 
'''
def anywinner(player):
    global number_of_clicks

    # Check to see if the first button has a value. 
    if button_One["text"]=="":
        value1=20
    else:
    	# If yes, then set value1 to the number in the button. 
        value1=int(button_One["text"])

    # Check to see if the second button has a value. 
    if button_Two["text"]=="":
    	# If not, set to 20. 
        value2=20
    else:
    	# If not, then set value2 to the number in the button. 
        value2=int(button_Two["text"])


    # Check to see if the third button has a value. 
    if button_Three["text"]=="":
    	# If yes, then set value3 to the number in the button. 
        value3=20
    else:
        value3=int(button_Three["text"])

    # Check to see if the fourth button has a value. 
    if button_Four["text"]=="":
    	# If not, then set to 20. 
        value4=20
    else:
    	# If yes, then set the variable "value4" to the number in the button. 
        value4=int(button_Four["text"])

    # Check to see if the fifth button has a value. 
    if button_Five["text"]=="":
    	# If not, then set to 20. 
        value5=20
    else:
    	# If yes, then set the variable value5 to the number in the button. 
        value5=int(button_Five["text"])


    # Check to see if the sixth button has a value. 
    if button_Six["text"]=="":
    	# If not, then set to 20.  
        value6=20
    else:
    	# If yes, then set "value6" to the number in the button.  
        value6=int(button_Six["text"])

    # Check to see if the seventh button has a value.
    if button_Seven["text"]=="":
    	# If not, set to 20.
        value7=20
    else:
    	# If not, then set the variable "value7" to the number in the button. 
        value7=int(button_Seven["text"])

    # Check to see if the eigth button has a value.
    if button_Eight["text"]=="":
    	# If not, set to 20. 
        value8=20
    else:
    	# If yes, then set the variable "value8" to the number in the button. 
        value8=int(button_Eight["text"])


    # Check to see if the ninth button has a value. 
    if button_Nine["text"]=="":
    	# If not, set the variable to 20. 
        value9=20
    else:
    	# If yes, then set the variable "value9" to the number in the button. 
        value9=int(button_Nine["text"])

    # Create all patterns and store their values for processing. 
    pattern1=value1+value2+value3
    pattern2 = value4 + value5 + value6
    pattern3 = value7 + value8 + value9
    pattern4 = value1 + value4 + value7
    pattern5 = value2 + value5 + value8
    pattern6 = value3 + value6 + value9
    pattern7 = value1 + value5 + value9
    pattern8 = value3 + value5 + value7

    # Check if the first pattern is the correct value. 
    if pattern1==15:
    	# Check which player is currently active. 
        if player==1:
        	# Set the winning string. 
            temp="PLAYER 2 HAS WON"

            # Highlight the winning numbers in blue. 
            button_One.config(bg="blue")
            button_Two.config(bg="blue")
            button_Three.config(bg="blue")

            # Inform the players of the win. 
            playerwon(temp)

        elif player==3:
        	# Set the winning string.
            temp = "Computer HAS WON"

            # Highlight the winning numbers in blue.
            button_One.config(bg="blue")
            button_Two.config(bg="blue")
            button_Three.config(bg="blue")

            # Inform the players of the win. 
            playerwon(temp)

        else:
        	# Set the winning string. 
            temp = "PLAYER 1 HAS WON"

            # Highlight the winning numbers in blue. 
            button_One.config(bg="blue")
            button_Two.config(bg="blue")
            button_Three.config(bg="blue")

            # Inform the players of the win. 
            playerwon(temp)

    # Check if the first pattern is the correct value. 
    elif pattern2==15:
    	# Check which player is currently active. 
        if player==1:
        	# Set the winning string. 
            temp="PLAYER 2 HAS WON"

            # Highlight the winning numbers in blue. 
            button_Four.config(bg="blue")
            button_Five.config(bg="blue")
            button_Six.config(bg="blue")

            # Inform the players of the win. 
            playerwon(temp)

        elif player==3:
        	# Set the winning string. 
            temp = "Computer HAS WON"

            # Highlight the winning numbers in blue. 
            button_Four.config(bg="blue")
            button_Five.config(bg="blue")
            button_Six.config(bg="blue")

            # Inform the players of the win.
            playerwon(temp)


        else:
        	# Set the winning string. 
            temp = "PLAYER 1 HAS WON"

            # Highlight the winning numbers in blue. 
            button_Four.config(bg="blue")
            button_Five.config(bg="blue")
            button_Six.config(bg="blue")

            # Inform the players of the win. 
            playerwon(temp)

    # Check if the first pattern is the correct value. 
    elif pattern3==15:
    	# Set the winning string. 
        if player==1:
            temp="PLAYER 2 HAS WON"

            # Highlight the winning numbers in blue. 
            button_Seven.config(bg="blue")
            button_Eight.config(bg="blue")
            button_Nine.config(bg="blue")

            # Inform the players of the win. 
            playerwon(temp)

        elif player==3:
        	# Set the winning string. 

            temp = "Computer HAS WON"

            # Highlight the winning numbers in blue. 
            button_Seven.config(bg="blue")
            button_Eight.config(bg="blue")
            button_Nine.config(bg="blue")

            # Inform the players of the win. 
            playerwon(temp)
        else:
        	# Set the winning string. 
            temp = "PLAYER 1 HAS WON"

            # Highlight the winning numbers in blue. 
            button_Seven.config(bg="blue")
            button_Eight.config(bg="blue")
            button_Nine.config(bg="blue")

            # Inform the players of the win. 
            playerwon(temp)


    # Check if the first pattern is the correct value.
    elif pattern4==15:
    	# Check which player is currently active. 
        if player==1:
        	# Set the winning string.
            temp="PLAYER 2 HAS WON"

            # Highlight the winning numbers in blue. 
            button_One.config(bg="blue")
            button_Four.config(bg="blue")
            button_Seven.config(bg="blue")

            # Call the "playerwon()" Function to inform the players of the win. 
            playerwon(temp)

        elif player==3:
        	# Set the winning string.
            temp = "Computer HAS WON"

            # Highlight the winning numbers in blue. 
            button_One.config(bg="blue")
            button_Four.config(bg="blue")
            button_Seven.config(bg="blue")

            # Call the "playerwon()" Function to inform the players of the win. 
            playerwon(temp)


        else:
        	# Set the winning string. 
            temp = "PLAYER 1 HAS WON"

            # Highlight the winning numbers in blue. 
            button_One.config(bg="blue")
            button_Four.config(bg="blue")
            button_Seven.config(bg="blue")

            # Inform the players of the win. 
            playerwon(temp)


    # Check if the first pattern is the correct value. 
    elif pattern5==15:
    	# Check which player is currently active. 
        if player==1:
        	# Set the winning string. 
            temp="PLAYER 2 HAS WON"

            # Highlight the winning numbers in blue. 
            button_Two.config(bg="blue")
            button_Five.config(bg="blue")
            button_Eight.config(bg="blue")

            # Call the playerwon() Function to inform the players of the win. 
            playerwon(temp)

        elif player==3:
        	# Set the winning string. 
            temp = "Computer HAS WON"

            # Highlight the winning numbers in blue. 
            button_Two.config(bg="blue")
            button_Five.config(bg="blue")
            button_Eight.config(bg="blue")

            # Inform the players of the win. 
            playerwon(temp)

        else:
        	# Set the winning string. 
            temp = "PLAYER 1 HAS WON"

            # Highlight the winning numbers in blue. 
            button_Two.config(bg="blue")
            button_Five.config(bg="blue")
            button_Eight.config(bg="blue")

            # Inform the players of the win. 
            playerwon(temp)


    # Check if the first pattern is the correct value. 
    elif pattern6==15:
    	# Check which player is currently active. 
        if player==1:
        	# Set the winning string. 
            temp="PLAYER 2 HAS WON"

            # Highlight the winning numbers in blue. 
            button_Three.config(bg="blue")
            button_Six.config(bg="blue")
            button_Nine.config(bg="blue")

            # Inform the players of the win. 
            playerwon(temp)

        elif player==3:
        	# Set the winning string. 
            temp = "Computer HAS WON"

            # Hightlight the winning numbers in blue. 
            button_Three.config(bg="blue")
            button_Six.config(bg="blue")
            button_Nine.config(bg="blue")

            # Inform the players of the win. 
            playerwon(temp)

        else:
        	# Set the winning string. 
            temp = "PLAYER 1 HAS WON"

            # Highlight the winning numbers in blue. 
            button_Three.config(bg="blue")
            button_Six.config(bg="blue")
            button_Nine.config(bg="blue")

            # Inform the players of the win. 
            playerwon(temp)

    # Check if the first pattern is the correct value. 
    elif pattern7==15:
    	# Check which player is currently active. 
        if player==1:
        	# Set the winning string.
            temp="PLAYER 2 HAS WON"

            # Highlight the winning numbers in blue. 
            button_One.config(bg="blue")
            button_Five.config(bg="blue")
            button_Nine.config(bg="blue")

            # Inform the players of the win. 
            playerwon(temp)

        elif player==3:
        	# Set the winning string. 
            temp = "Computer HAS WON"

            # Highlight the winning numbers in blue. 
            button_One.config(bg="blue")
            button_Five.config(bg="blue")
            button_Nine.config(bg="blue")

            # Inform the players of the win. 
            playerwon(temp)

        else:
        	# Set the winning string. 
            temp = "PLAYER 1 HAS WON"

            # Highlight the winning numbers in blue.
            button_One.config(bg="blue")
            button_Five.config(bg="blue")
            button_Nine.config(bg="blue")

            # Inform the players of the win. 
            playerwon(temp)



    elif pattern8==15:
        if player==1:
            temp="PLAYER 2 HAS WON"
            button_Three.config(bg="blue")
            button_Five.config(bg="blue")
            button_Seven.config(bg="blue")
            playerwon(temp)
        elif player==3:
            temp = "Computer HAS WON"
            button_Three.config(bg="blue")
            button_Five.config(bg="blue")
            button_Seven.config(bg="blue")
            playerwon(temp)

        else:
            temp = "PLAYER 1 HAS WON"
            button_Three.config(bg="blue")
            button_Five.config(bg="blue")
            button_Seven.config(bg="blue")
            playerwon(temp)


'''
The Definition of the Function "retrieve_input(root2, textBox, btn)" is that it takes in the user input during the game and determines if it is valid and can be placed. 
'''
def retrieve_input(root2,textBox,btn):
    global number_used,number_used_count,RepeatNumberFlag,opposite_Toggle,toggle,number_of_clicks,allow,computer_toggle

    # Retrieve the user input from the text box. 
    number = textBox.get("1.0", "end-1c")
    
    # Display the number in the console. 
    print(number)

    # If the number has already been used.
    if number in number_used:
    	# Inform the player and set the repeat number flag. 
        warning("You have already used "+str(number)+". Pick a different number from 1 through 9.")
        repeat_number_flag=1


    else:
        repeat_number_flag=0

    # If the number is valid, the player is correct, the number has not been repeated and this is a multiplayer game. 
    if (number in ('2','4','6','8'))and opposite_Toggle==1 and repeat_number_flag==0 and multiplayer_or_not not in ('NO', 'no', 'No','nO'):
     # Destroy the second root window. 
     root2.destroy()

     # Set the text of the button to the number.
     btn["text"] = number

     # Check to see if this is a winning play. 
     anywinner(opposite_Toggle)

     # Put the number into the used numbers list and increment the count. 
     number_used.insert(number_used_count,number)
     number_used_count = number_used_count + 1

     # Swap to the first player. 
     opposite_Toggle=0
     toggle=1
     # Increment the number of clicks to see if there is a draw. 
     number_of_clicks=1+number_of_clicks

     if number_of_clicks==9:
         draw()

    # If the number is valid, and we are on Player 1 and the number was not on repeat. 
    elif (number in ('1','3','5','7','9'))and opposite_Toggle==0 and repeat_number_flag==0:
    	# Destroy the "root2()" window. 
        root2.destroy()

        # Set the text of the button and the text color number to green. 
        btn["text"] = number
        btn.config(fg='green')
        anywinner(opposite_Toggle)
        number_used.insert(number_used_count,number)
        number_used_count = number_used_count + 1


        if multiplayer_or_not not in ('NO', 'no', 'No','nO'):
           opposite_Toggle=1
           toggle = 0
           computer_toggle=1


        number_of_clicks=1+number_of_clicks
        randombuttonremovefunction(btn)
        if number_of_clicks < 9 and multiplayer_or_not in ('NO', 'no', 'No','nO') and winner_declared==0:
            number_of_clicks=1+number_of_clicks
            cpufunction()
            anywinner(3)
        if number_of_clicks == 9:
            draw()


    elif opposite_Toggle==1:
        root2.destroy()
        # Inform the player that they cannot play that number. 
        warning("Player 2 you can only type the following Even Numbers and you can only use these Even Numbers once every 'Retry' Game of Numerical Tic Tac Toe:\n"+"2,4,6,8")


    # If it is player one's turn. 
    elif opposite_Toggle==0:
    	# Destroy the root 2 window. 
        root2.destroy()
        warning("Player 1 you can only type the following Odd Numbers and you can only use these Odd Numbers once every 'Retry' Game of Numerical Tic Tac Toe:\n" + "1,3,5,7,9")



def takeinput(btn):
    global opposite_Toggle,root2
    root2 = Tk()

    # Build the root2 window with the global size dimensions of 400 by 100. 
    root2.geometry("400x110")
    if opposite_Toggle==0:
     root2.title("Player 1")
     label = Label(root2,text="Player 1 type one odd number from 1 through 9",font=('Helvetica',10,'bold'))
     label.pack()
    else:
        root2.title("Player 2")
        label = Label(root2, text="Player 2 type one even number from 1 through 9",font=('Helvetica',10, 'bold'))
        label.pack()

    # Build the text box add it to the Root2 Window. 
    textBox = Text(root2, height=2, width=30,font=('Helvetica', 17, 'bold'))
    textBox.pack()

    # Build the commit button and add it to the root2 window. 
    buttonCommit = Button(root2, height=1, width=30, text="Submit",
                          command=lambda: retrieve_input(root2,textBox,btn))

    buttonCommit.pack()

'''
The Definition of Function "getvalue(btn)" is that it takes in a button and calls the Take Input Function. 
'''
def getvalue(btn):
    global toggle,opposite_Toggle

    # Call the "takeinput(btn)" Function with the given button. 
    takeinput(btn)

# For the CPU Player, create a list of even numbers assigned to the variable "random_numbers_list" in order to set up the "random_numbers_list".
random_numbers_list = ['2','4', '6', '8']
random_numbers_list_used=[]

'''
The Definition of Function "randomnumberremovefunction()" is that it removes the given button from the Random Numbers List. 
'''
def randomnumberremovefunction(n):
    random_numbers_list.remove(n)

'''
The Defnition of "randombuttonremovefunction(btn)" is that it returns a random number from the Random Numbers List. 
'''
def randombuttonremovefunction(btn):
    randombuttonlist.remove(btn)
    print("count of random button is")
    print(len(randombuttonlist))

'''
The Definition of "randomnumberfunction()" is that it uses the Random.choice function to select a number from the Random Numbers List. 
'''
def randonnumberfunction():
     return(random.choice(random_numbers_list))

'''
The Definition of "randombuttonfunction()" is that it returns a random button from the random buttons list. 
'''
def randombuttonfunction():
    return(random.choice(randombuttonlist))

'''
The Definition of the "cpufunction()" that is the Computer Player Function is that it does the logic for the Computer controlled player to select a button and put a number value in. 
'''
def cpufunction():
    global computer_toggle

    # Call a Random Number Function to select a number from the Random Numbers List. 
    selectrandomnumber = randonnumberfunction()

    # Check if we received a random number from the function call. 
    if selectrandomnumber!="":
    	# Remove the number from the list. 
        randomnumberremovefunction(selectrandomnumber)

        #print("random numer is->" + str(selectrandomnumber))
        # Call the Random Button Function to select a button from the Random Button List.  
        selectrandombutton = randombuttonfunction()

        # Remove the button from the list. 
        randombuttonremovefunction(selectrandombutton)

        # Set the text of the button to the number received and change the turn away from the Computer's action. 
        selectrandombutton.config(text=selectrandomnumber);
        computer_toggle=0

'''
The Definition of Function "click_Button_One(btn)" indicates that the first button in the game area has been clicked and that the Get Value function should be called. 
'''
def click_Button_One(btn):
    global opposite_Toggle,multiplayer_or_not

    # Check if the button has not already been clicked. 
    if btn["text"]=="":
    	# Call the Get Value function on the given button. 
        getvalue(btn)

        # Check if the current player has won the game. 
        anywinner(opposite_Toggle)

'''
The Definition of Function "click_Button_Two(btn)" indicates that the fourth button in the game area has been clicked and that the Get Value function should be called if the button's text is empty. 
'''
def click_Button_Two(btn):
    global opposite_Toggle,allow

    if btn["text"] == "":
        getvalue(btn)
        anywinner(opposite_Toggle)

'''
The Definition of Function "click_Button_Three(btn)" indicates that the third button in the game area has been clicked and that the Get Value function should be called if the button's text is empty.  
'''
def click_Button_Three(btn):
    global opposite_Toggle

    # Check if the button has not already been clicked. 
    if btn["text"] == "":
    	# Call the Get Value Function on the given button.  
        getvalue(btn)

        # Check if the current player has won the game. 
        anywinner(opposite_Toggle)

'''
The Definition of Function "click_Button_Four(btn)" indicates that the fourth button in the game area has been clicked and that the Get Value Function should be called if the button's text is empty. 
'''
def click_Button_Four(btn):
    global opposite_Toggle

    # Check if the button has not already been clicked. 
    if btn["text"] == "":
    	# Call the "getvalue(btn)" Function on the given function. 
        getvalue(btn)

        # Check if the current player has won the game. 
        anywinner(opposite_Toggle)


'''
The Definition of Function "click_Button_Five(btn)" indicates that the fifth button in the game area has been clicked and that the Get Value Function should be called if the button's text is empty. 
'''
def click_Button_Five(btn):
    global opposite_Toggle

    # Check if the button has not already been clicked. 
    if btn["text"] == "":

    	# Call the "getvalue(btn)" Function on the given button. 
        getvalue(btn)

        # Check if the current player has won the game. 
        anywinner(opposite_Toggle)


'''
The Definition of "click_Button_Six(btn)" Function indicates that the sixth button in the game area has been clicked and that the Get Value Function should be called if the button's text is empty. 
'''
def click_Button_Six(btn):
    global opposite_Toggle

    # Check if the button has not already been clicked. 
    if btn["text"] == "":
    	# Call the "getvalue(btn)" Function on the given button. 
        getvalue(btn)

        # Check if the current player has won the game. 
        anywinner(opposite_Toggle)

'''
The Definition of "click_Button_Seven(btn)" Function indicates that the seventh button in the game area has been clicked and that the Get Value Function should be called if the button's text is empty. 
'''
def click_Button_Seven(btn):
    global opposite_Toggle

    # Check if the button has not already been clicked. 
    if btn["text"] == "":
    	# Call the "getvalue(btn)" Function on the given button. 
        getvalue(btn)

        # Check if the current player has won the game. 
        anywinner(opposite_Toggle)

'''
The Definition of Function "click_Button_Eight(btn)" indicates that the eigth button in the game area has been clicked and that the Get Value Function should be called if the button's text is empty. 
'''
def click_Button_Eight(btn):
    global opposite_Toggle

    # Check if the button has not already been clicked. 
    if btn["text"] == "":
    	# Call the Function "getvalue(btn)" on the given button. 
        getvalue(btn)

        # Check if the current player has won the game. 
        anywinner(opposite_Toggle)

'''
The Definition of Function "click_Button_Nine(btn)" is that the nineth button in the game area has been clicked and that the Get Value Function should be called. 
'''
def click_Button_Nine(btn):
    global opposite_Toggle

    # Check if the button has not already been clicked. 
    if btn["text"] == "":
    	# Call the "getvalue(btn)" Function on the given button. 
        getvalue(btn)

        # Call the "anywinner()" Function and check if the current player has won the game. 
        anywinner(opposite_Toggle)

'''
The Definition of "createbuttons()" Function is that it creates the buttons used for the game area and adds them to the Root window.
'''
def createbuttons():
    global button_One,button_Two,button_Three,button_Four,button_Five,button_Six,button_Seven,button_Eight,button_Nine,root,randombuttonlist


    # Create buttons 1 through 9 and add them to the root window. 
    button_One = Button(root, text="", bg="black", fg="red", width=4, height=1, font=('times', 67), command=lambda :click_Button_One(button_One))
    button_Two = Button(root, text="", bg="black", fg="red", width=4, height=1, font=('times', 67), command=lambda :click_Button_Two(button_Two))
    button_Three = Button(root, text="", bg="black", fg="red", width=4, height=1, font=('times', 67), command=lambda :click_Button_Three(button_Three))
    button_Four = Button(root, text="", bg="black", fg="red", width=4, height=1, font=('times', 67), command=lambda :click_Button_Four(button_Four))
    button_Five = Button(root, text="", bg="black", fg="red", width=4, height=1, font=('times', 67), command=lambda :click_Button_Five(button_Five))
    button_Six = Button(root, text="", bg="black", fg="red", width=4, height=1, font=('times', 67), command=lambda :click_Button_Six(button_Six))
    button_Seven = Button(root, text="", bg="black", fg="red", width=4, height=1, font=('times', 67), command=lambda :click_Button_Seven(button_Seven))
    button_Eight = Button(root, text="", bg="black", fg="red", width=4, height=1, font=('times', 67), command=lambda :click_Button_Eight(button_Eight))
    button_Nine = Button(root, text="", bg="black", fg="red", width=4, height=1, font=('times', 67), command=lambda :click_Button_Nine(button_Nine))

    # Add all buttons to the "randombuttonlist".
    randombuttonlist = [button_One, button_Two, button_Three, button_Four, button_Five, button_Six, button_Seven, button_Eight, button_Nine]

    # Place each button in its corresponding column and row. 
    button_One.grid(column=1, row=1)
    button_Two.grid(column=2, row=1)
    button_Three.grid(column=3, row=1)
    button_Four.grid(column=1, row=2)
    button_Five.grid(column=2, row=2)
    button_Six.grid(column=3, row=2)
    button_Seven.grid(column=1, row=3)
    button_Eight.grid(column=2, row=3)
    button_Nine.grid(column=3, row=3)

'''
The Definition of Function "instructionwindow()" is that it creates and displays the instruction window. 
'''
def instructionwindow():
    global open_instruction_window
    # Set the instruction window open state to 'yes'.
    open_instruction_window='yes'

    # Set the instruction window size and title. 
    ins.geometry("765x660")
    ins.title("Rules for Playing Numerical Tic Tac Toe")

    # Create instruction labels and add them to the instruction window. 
    instruction_Title_Label=Label(ins,text="INSTRUCTIONS ON HOW TO PLAY NUMERICAL TIC TAC TOE",anchor='center', font=('Times',19,'bold', 'underline'), foreground="blue")
    instruction_Step_One = Label(ins, text="1.) Player 1 will only be allowed to use Odd Numbers from 1 through 9.\n", font=('Times', 14))
    instruction_Step_Two = Label(ins, text="2.) Player 2 will only be allowed to use Even Numbers from 1 through 9.\n", font=('Times',14))
    instruction_Step_Three = Label(ins, text="3.) The last player who adds an Odd Number or Even Number in One of\nthe Three Square Buttons of a Row, Column, or Diagonal on the\nNumerical Tic Tac Toe Board that adds up to 15 wins the game.\n",font=('Times',14))
    instruction_Step_Four = Label(ins, text="4.) If you, the Player, or Players decide to play more than 1 game or at\n     maximum 20 games, then you the Player or Players have the option\n  to retry to get more points based on the Total Number of Games\n          typed in 'Initial Information Window' to win at Numerical Tic Tac Toe\n           by Left Clicking your Computer Mouse on the 'RETRY' Button on the\n          right side of the 'BOARD FOR NUMERICAL TIC TAC TOE GAME'\n Window.\n",font=('Times',14))
    instruction_Step_Five = Label(ins, text="\t5.) Press that is use your Computer Mouse to Left-Click the 'NEW GAME' Button to\n\t        start a New Numerical Tic Tac Toe Game Match between either yourself as Player 1\n                      against the AI CPU Computer Player or yourself as Player 1 against another person,\ncomputer user, who would be Player 2.\n",font=('Times',14))
    instruction_Step_Six = Label(ins, text= "6.) To quit playing on the 'BOARD FOR NUMERICAL TIC TAC TOE GAME',\nLeft-Click your Computer Mouse on the 'EXIT' Button on the right side\nof the 'BOARD FOR NUMERICAL TIC TAC TOE GAME' Window.\n", font=('Times',14))
    agree=Button(ins,text="I AGREE",anchor='center',font=('Times',19,'bold'),fg='blue',bg='grey',command=lambda :agreefunction(ins)).place(x=325,y=600) #x=240, y=290

    # Use the "pack()" Function to ensure all of the labels fit correctly on the instruction window. 
    instruction_Title_Label.pack()
    instruction_Step_One.pack()
    instruction_Step_Two.pack()
    instruction_Step_Three.pack()
    instruction_Step_Four.pack()
    instruction_Step_Five.pack()
    instruction_Step_Six.pack()

'''
# The Definition of the "agreefunction(ins)" is that when the agreement button is clicked, then destroy the instruction window and call the Initial Information function. 
'''
def agreefunction(ins):
    global instructions_window_flag

    # Set the instructions_windows_flag to 1. 
    instructions_window_flag=1

    # Destroy the instruction window. 
    ins.destroy()

    # Enable the game buttons. 
    enablebutton()

    # Display the intial info window. 
    initial_information()

# Build and show the instruction window. 
instructionwindow()

# Create buttons for the play area. 
createbuttons()
disablebuttons()

# Begin the main loop for the game. 
ins.mainloop()