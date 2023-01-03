# Scope
This is a living document to describe aspects of the system we're not going to model but that helps inform the modeling. Some of this can be modeled in other tools, but isn't the current intent for the collaborators' objective.

# System Overview
This System of Interest is the lock system. The overall fort, door, etc. are outside the system boundary. We may still discuss/document aspects of this, but we are not designing a solar power system for the fort or deciding on fort construction material as part of a lock. External interfaces and the environment are still relevant and is discussed. TDS: In particular, note that the lock system does not actuate movement of the door itself.

## Use Cases
This section describes relevant use cases. Intent here is to capture general usage goals and what can go right or wrong.

2023.01.02 (pg): This is at the brainstorming level currently.

**TODO: Write textual use cases with success and alternate scenarios to inform the AADL modeling**

Use Cases:
- Install Lock System: How will the homeowner install the lock on the door and support equipment?
- Activate System: How will the homeowner "turn it on"?
- Deactivate System: How will the homeowner "turn it off"?
- Monitor System: How will the homeowner monitor the health and status of system?
- Safely Open Door: How will a person access the fort, which will exercise the lock?
- Safely Close Door: How does a person leave the fort in a secure (locked) state?

## Modes and States
This section describes relevant modes and states. The list assumes the system is installed, skipping disassembled/assembled or "in transit" type states.

2023.01.02 (pg): This is at the brainstorming level currently. I expect this list to generate some debate.
2023.01.02 (TDS): Note that the terms "modes" and "states" do have significance in AADL-land. Unfortunately, there are several methods for specifying modes and states. I assume for the purposes of this document we're writing that we'll use this list of states as a basis for an AGREE specification. 
However, for future work we might also consider the AADL Error Modeling Annex, AADL Behavior Annex, or AADL mode and mode-transition language features. 

**TODO: Complete brainstorming, categorize as needed, connect with transitions, remove unneeded states after discussion/iterations**

Modes and States (Assumes Installed)
- **Powered On:** System has power but is not in any other state. (TDS: May be a no-op for a non-electric implementation).
- **Powered Off:** System has no power.
- **Initialized:** System has power and has completed any initialization but is not yet operational.
- **Normal Operations:** System is fully functional - can be be locked/unlocked and  monitored - without issue.
- **Degraded:** Something is wrong - on battery backup, monitoring offline, or TBD - but Safely Open (and Close) Door use cases can still be accomplished 
- **Failsafe:** System is too degraded and must be unlocked and otherwise taken "offline"
- **Locked:** The lock itself is locked.
  - **TDS Proposes:** **Locked:** The lock mechanism is engaged (that is, the door cannot be opened without disassembly).
- **Unlocked:** The lock itself is unlocked.
  - **TDS Proposes:** **Unlocked:** The lock mechanism is disengaged (that is, the dor can be opened).

TDS: Additional states to consider
- **Door Open:** The door is physically open.
- **Door Closed:** The door is physically closed. 
- **User Lockout:** User has entered an incorrect passcode multiple times and is locked out for some period of time. 

TDS: Events to drive transitions
- **Successful User Authorization:** The user provides correct authorization (e.g., enters correct keycode)
- **Failed User Authorization:** The user fails to provide correct authorization (e.g., enters incorrect keycode)
- **User Exit Request:** The user wants to leave the fort and informs the system (e.g., via a button press)

# Glossary

| Term           | Definition    | Notes | 
| -------------  | ------------- | ------------ | 
| Fort           | An outdoor structure with walls and a door. | | 
| Lock System    | A system providing the capability to prevent the fort door from being opened in some circumstances. | |
| Lock Mechanism | The physical mechanism by which the Lock System prevents the door from opening. | | 
| User | A human who can interact with the lock | |
| User Authentication | A part of the Lock System that can verify a user-provided authorization artifact (e.g., physical key, keycode) | | 

