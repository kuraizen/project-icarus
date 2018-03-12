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

label start:
   #show v2
 
    scene start
    play music "eternity.mp3"
    $ player_name = ""
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "b g room.jpg") to the
    # images directory to show it.
   # play music "eternity"
    
   
    m "where am i"

    m "what am i?"

    m "how did i get here?"

    m "Who am I?"

    $ player_name = renpy.input("")
    # $ player_name = player_name.strip()
    if player_name == "":
        m "i guess i cant remember"
        m "oh..my name is rentarou katagiri"
        $ player_name = "rentarou"
    
    m "why am i here?"

    m "i dont know"

    m "im here for a reason"

    m "someone sent me here"

    m "but for what?"

    m "and why me?"


 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

   
    
    # These display lines of dialogue.
    scene dream

    sakura "Hello"

    sakura "[player_name] ..."
    
    sakura "[player_name] ... wake up"
     
    sakura "[player_name] ...please!!! "

    sakura "i need you"

    sakura "i can't do this without you"

    sakura "we dont have much time"

    m "i Know her i dont know why"

    m "she sounds in trouble"

    sakura "go on without me"

    sakura "only you can stop the calamity"

    sakura "i need you to go to !@#@!#!"

    sakura "and @#@#"

    sakura "now go!!!"

    sakura "i dont think i can make it any further"

    sakura "just leave me here"

    menu:

        "leave her":

          m "~i have to go~"
          m "i have to do it for her"

          jump leave_sakura

        "take her":

         m "i wont leave you i can't"

         sakura "I .."

         sakura "Love..."

         sakura "you.."

         sakura "..."

         sakura "..."

         

         m "NOOOO!!!"

         m "@!$#@"

         jump take_sakura

    label take_sakura:
    $ sakura_pts += 1
    $ took_sakura = True

    label leave_sakura:
    # although this is labeled as leave this is passed either if we leave or take her 
    # the purpose was to update her pts score if we took her so leaving her will not update pts
    # and taking her will not update more pts than what it was prev. updated or take away pts


    sakura "i promise we will meet again"



    scene black
    with dissolve

    #dissolve or fade
    stop music fadeout 1.0
    play music "relax.mp3"
    pause 3

    m "what was that?"
    
    m "who was that"
    
    m "i keep having the same dream of a girl calling my name" 

    m "each day my dream progresses more and feels more vivid"

    m "and she tells me i need to go somewhere"

    m "but where"

    m "its always the same dream ive had for years"

    m "but ive been having them more frequently"

    m "it used to be that i just heard her calling me"

    m "but tonight was different"

    m "it was more vivid like i was there"

    m "and she was injured"

    m "who is she?"

    m "and why did she know me"

    m "how did i know her"

    m "it was if i had known her since long ago"

    m "i felt "

    m "why am i crying"

    m "just who was that girl"

    m "~i kept thinking about that dream and before i knew it "

    m "i had fallen back to sleep~"
    

    #intro 
    $ renpy.movie_cutscene("fakelove.mpg")

    

    play music "never be alone.mp3" fadein 1.0
    
    "{b}day [day]{/b}"

    menu:
        "{b}~Alarm clock~{/b}"
        "wake up":
            jump wake

        "Sleep 10 more min":
            jump sleep

label wake:
   stop music fadeout 1.0
   "{b}~7:00 AM~{/b}"
   m "i have to get up"

   $ first_met = "Kaori"
   show kaori 
  
   #WIP@@@@@@@@@@@@@
   hide kaori

   jump day_one_morning 
   #dont run late so we walk to school meet Megumi and motoko 
   # neither are affected + kaori




label sleep:
    stop music fadeout 1.0
    show bedroom day
    with dissolve
    m "five more minutes"

    "{b}~8:00 AM~{/b}"
    #WAKES UP LATE!!! scene my room mess desk 
    m "IM LATE!!!"
    
    #footsteps sound downstairs
    #rushes scene
    
    m "maybe i should get something quick to eat"
    define ate = False
    menu:

        "get someting quick to eat":
          #will be extra late and meet motoko 
         jump eat1

        "dont eat anything im running late already":
         jump dont_eat1

    label eat1:

       $ ate = True
       show living room evening
       with dissolve

       m "well i guess some leftover Mg tonalds"

       show food 2
       with dissolve
       #show food sandwich 
       m ""
       m "i need to hurry or i'll be late to the opening ceremony"

       jump transport
    label dont_eat1:

       $ ate = False 
       m "i dont have time to get something to eat"

       jump transport

   




label game:


label day_one_morning:

#meets megumi and motoko 



jump day_one_day


####


label transport:

     #show street
    show house exterior
    with dissolve
    m "i need to hurry what should i take? "
    menu:

      "go on bike":
        jump bike

      "go on bus":
        jump bus

      "go by foot":
        jump foot

      "give up and go home": 
        jump go_home

    label bike:
      $ first_met = "Akane"
      "i'll get to school faster if i take my bike"


      #show bike and bike riding 
      

      jump day_one_day

    label bus:
       $ first_met = "Nagisa"

       m "~i think i'll take the bus or i'll have to walk from the parking lot to class, ~"
       m "~the bus will drop me off in front of my hall~"
       
       m "~ i got on the bus nearest my house and to my luck it just in time~"

       m "~i looked for an empty seat but they seemed to be all taken~"

       nagisa "uhm...you can sit here if you want"

       m "~ i looked toward what seemed to be a shy girl she had a petite figure wiht short hair"

       m "thank you"

       m "~either though she didnt look like the glamourus type she had put on a really nice perfume"

       m "and was well dressed"
       "ate = [ate]"
       #talks
       if(ate == False):
         m "~{b} ...groak..churn{/b}"

         nagisa "he.he..he.giggle what was that"

         $ nagisa_pts += 1

         m "oh my god how embarrrasing"
         
         nagisa "did you not have breakfast this morning"

         m "well i over slept and didnt have the time to get something to eat"

       m "~we talked for a bit before i knew it we were at school~"

       jump day_one_day

    label foot:
       m  "its not that far i might make it if i run"

       if(ate == True):
         m "grlk..maybe it was a bad idea to eat that much my stomach is getting upset"
       
         m "~i kept running~"

       megumi "HEY WATCH OUT!!!"


       "SMASH"

       $ first_met = "Megumi"
       
       m "as if in an anime or a manga someone crashed into me and landed on the floor"

       megumi "im sorry im late to class and was in a hurry here let me help you"

       m "thanks.."

       m "well i was also late this morning and came running to school too"

       megumi "well i guess we both overlept huh so whats your name"

       if (ate == True):
         m "~it seemed that my stomach finally caught up with my body and ~"

         megumi "im ..blauh"

         m "~and as luck would have it my stomach had a really good sense of humour~"

         megumi "uhm are you ok.."

         m "yeah im okay"

         m "sorry so whats your name"

         $ megumi_pts += 1

         megumi "well blaah my name is megumi"

       else:

         m "my name is [player_name] nice to meat umm"

         megumi "im Megumi"



       jump day_one_day


    label go_home:

      #show home
      #show bed 
      m "i'm going back to sleep i'll just go tomorrow besides its the first day what can go wrong"
       
      jump day_two_morning


 ################     
label day_one_day:

    
    
    











    show bedroom_night 
    with dissolve

    m "today was fun "
    m "i cant remember the last day something exciting happened"
    m "i hope im able to meet new friends and enjoy my first year in Tokyo U"

    
    m "as i drift to sleep i cant help but think about [first_met]"
###########   
label day_two:

label day_two_morning:


   #day update
   $ day += 1



   "{b}day [day]{/b}"


   #day updated
    

label day_three:


label day_four:

label day_five:

label day_six:

   
    m "oh well"
    # This ends the game.

  
    return
