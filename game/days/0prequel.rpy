
# The game starts here.

label start:
   #show v2
 
    scene start
    play music "music/eternity.mp3"
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

call day1
