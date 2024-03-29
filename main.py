win=0 #this helps me mark the beginning and end of the game 
direction=0 #quantifying directions also helps me track the direction commands 
section=1 #sections are numbered so its easy to track the progress of the player

#item list and status

def direction(compass):#gives the direction a number
  if compass=="w" or compass.lower()=="west":
    return 1
  if compass=="n" or compass.lower()=="north":
    return 2
  if compass=="e" or compass.lower()=="east": 
    return 3
  if compass=="s" or compass.lower()=="south":
     return 4
  else:
    return 0


def beach(userinput):#direction options for on the beach 
  if direction(userinput)==1:
    print("""
You walk down to the small cabin only to 
find it abandoned. The doorstep is filled 
with a worn welcome mat and two dead 
plants. to the north, behind the shed is 
an old fishing dock. the beach reaches from
east to west and to the south of you a rocky 
cliff marks the end of the sandy shore.
          """)
    return 2
  elif direction(userinput)==3:
    print("The beach doesnt seem to end.")
    return 1
  elif direction(userinput)==4:
    print("""
you stare up at the cliff, Debating your
rock climbing abilities before deciding 
your feet are better off on solid ground
and returning to the beach.
""")
    return 1
  elif direction(userinput)==2:
    print("""
the open ocean is so peaceful. You wade
through the shallow water then swim out
to sea. The farther from the shore you
swim the lighter and brighter the world
seems. You close your eyes for a moment
and when you open them, you find 
yourself back on the beach.
    """)
    return 1
  elif direction(userinput)==0:
    print(f"you cant {userinput} here.")
    return 1
    
#items by the shack
FoundKey=False
enterance=False
enteranceUnlocked=False
Key=False

def searchKey():
  if Key==True:
    print("you found a key")
    Key=False
  else:
    print("theres nothing to find")

  
def outShack(userinput):#direction options for the shack
  if direction(userinput)==3:
    print("You are on the beach")
    return 1
  if direction(userinput)==2:
    print("you are on an old fishing dock")
  if  "search" in userinput.lower() or "search"==userinput.lower():
    searchKey()
    return 2
  else:
    print("you cant go that direction.")
    return 2

instructions=input("Would you like instructions? (Y or N):")
if instructions=="Y":
  print("INSERT INSTRUCTIONS")

print("""
You wake up to the grating noise of seaguls,
and the scratch of sand shifting in your 
socks. You rub your eyes groggly and look 
around. You are on an entirely empty beach.
It seems to span infinitly from east to 
west. You squint a bit until you can make 
out a small cabin to the west. To the south
of you a rocky cliff marks the end of the 
beach.

""")

while win==0:
  Key=False
  command=input("enter command: ")
  if section==1:
    section=beach(command)
  elif section==2:
    if FoundKey==False:
      Key=True
    section=outShack(command)
    print(FoundKey,Key)
    
  


  
    
  



