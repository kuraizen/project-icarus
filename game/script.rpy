# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#movie 

#stock images


image black = "#000"


#special 
define sakura = Character("Sakura", color="cb5e9f") # dream girl

define m = Character('[player_name]', color="#c8c8ff") # main
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

# The game starts here.

call start

call day1

#call day2
#call day3
#call day4
#call day5
#call day6
return
