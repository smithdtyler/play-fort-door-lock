# Scope
This is a living document to describe aspects of the system we're not going to model but that helps inform the modeling. Some of this can be modeled in other tools, but isn't the current intent for the collaborators' objective.

# System Overview
This System of Interest is the lock system. The overall fort, door, etc. are outside the system boundary. We may still discuss/document aspects of this, but we are not designing a solar power system for the fort or deciding on fort construction material as part of a lock. External interfaces and the environment are still relevant and is discussed.

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

**TODO: Complete brainstorming, categorize as needed, connect with transitions, remove unneeded states after discussion/iterations**
Modes and States (Assumes Installed)
- Powered On: System has power but is not in any other state.
- Powered Off: System has no power.
- Initialied: System has power and has completed any initialization but is not yet operational.
- Normal Operations: System is fully functional - can be be locked/unlocked and  monitored - without issue.
- Degraded: Something is wrong - on battery backup, monitoring offline, or TBD - but Safely Open (and Close) Door use cases can still be accomplished
- Failsafe: System is too degraded and must be unlocked and otherwise taken "offline"
- Locked: The lock itself is locked.
- Unlocked: The lock itself is unlocked.

