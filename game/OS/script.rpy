# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#movie 

#stock images


image black = "#000"


#special 
define sakura = Character("Sakura", color="cb5e9f") # dream girl

define m = Character('[player_name]', color="#c8c8ff") # main

define m_nvle = Character('[player_name]',color="#006bbf",kind=nvl) # char nvle

define first_name = ""

define last_name = ""
#female
define kaori = Character("Kaori",color="cba1e9") # childhood friend


define tomori = Character("Tomori",color="47003b") # mysterious girl dilinquent bossy

define nagisa = Character("nagisa",color="d0003b") # quite girl

define akane = Character("Akane",color="ff5b8d") # friendly happy girl tsundere

define megumi = Character("Megumi",color="ffcd71") # nice girl

define motoko = Character("Motoko",color="411632") # cold hearted kuudere black hair girl

#male


#images
image kaori blue normal = "sylvie blue normal.png"

#backgrounds and scenes


#variables and constants
define first_met = "" # k kaori mo motoko 0-5

define sakura_pts = 0

define took_sakura = False

define kaori_pts = 0

define tomri_pts = 0

define nagisa_pts = 0

define akane_pts = 0

define megumi_pts = 0

define motoko_pts = 0




#other var


define day = 1


#atributes

#will get changed at start main attribute
define main_attributes = -1
define main_personality = "" #char personality 
#reserved outgoing proud happy-golucky muscle 
define second_attr = ""
# intellegent muscle airhead normal mean cunning 



define intellect = 0 #intellect
define intuition = 0 #social
define athletic = 0  #athletic 

# char starts with goodness and meanness that chages based on decisions

define goodness = 50 #def
define meanness = 10 #def

define maturity = 50 #immatture <30 mature >100

# The game starts here.






call start

call day1

#call day2
#call day3
#call day4
#call day5
#call day6
return
