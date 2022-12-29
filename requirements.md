# Informal Requirements for Door and Door Lock

1. will not allow a child to get stuck
1. can be closed/monitored against critters/teenagers
1. does not require physical keys

# Q&A Between Collaborators

## What does closed/monitored mean?
- Does the system need to close the door, or simply engage the lock?
  - TDS: I think just engage the lock. An actuator that could close the door introduces a whole new variety of safety risks. 
- Does monitored mean the state of the lock (e.g., locked/unlocked), or the inside of the fort for motion/presence of critters/teenagers?
  - TDS: Good question. Ideally both. 
- What size of critters are of interest?  Mice or raccoons?
  - Mice are going to be hard to keep out entirely, since they can fit through very small spaces. 
  - I'm planning to make this tight enough to keep our anything rat-size or larger. 
- Is a physical button, switch, or ability to actuate the lock from the inside acceptable to meet needs 1 and 3?
  - TDS: Yes. 

## Safety
- The door can always be opened from the inside
- No harm to the occupants of the fort (sharp objects, falling objects)
- No risk of electrical shock
- No risk of fire

## Power
- Power source in fort?  AC available?
  - TDS: Fort has AC power (via outdoor extension cord). Also planning on solar, possibly DC battery. 
  - TDS: I'd like the power usage to be relatively low - 10 watts would be good. 
- Desired/required battery backup?
  - TDS: I'd like this to fail safe (i.e. unlock if power goes out)

## Environmental
- What environmentals do we need to consider? Thermal, yes (min/max temps). Shock/vibration, probably not unless making components (e.g., the lock).
- What is the min/max temperature expected in the fort? Assume most parts are sheltered from the elements directly (no direct sunlight, no rain/snow on equipment, no wind). **TODO: Throw a temp sensor in the fort to gather data?**

## Communication and Control
- Also, a keypad?  Or, where’s the wifi?
  - TDS: The fort is close enough to our house that wifi makes sense as a monitoring option. 
  - TDS: I was originally thinking a keypad for entering a passcode, wifi on the board. 
- Will there be a keypad in addition to wifi?
  - TDS: I think so.  

# Open/Uncategorized Questions: 
- What level of redundancy is desired? And where?
  - TDS: I want redundancy for safety needs (i.e. I want high assurance that the kids can exit) but do not need redundancy for security (if something fails and the door does not lock, that's OK). 
- What is the budget? $100? $1000? $10000?  Not just piece-parts, but labor and material for say trenching the yard for wired connections, or adding solar per the above, and so on? (Examples are purposefully expensive sounding... I hope no yard trenching)
  - TDS: Around $100, I'm planning to use budget as a nice design-trade metric, so we'll design a couple of options at various price points and risk levels. I'm already pondering solar options, so that won't be factored into the price. 
- (For us) What ratings on enclosures and components exposed to the elements do we want?  IPxy
