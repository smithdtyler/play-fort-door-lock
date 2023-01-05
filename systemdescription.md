# Scope
This is a living document to describe aspects of the system we're not going to model but that helps inform the modeling. Some of this can be modeled in other tools, but isn't the current intent for the collaborators' objective.

# System Overview
This System of Interest is the lock system. The overall fort, door, etc. are outside the system boundary. We may still discuss/document aspects of this, but we are not designing a solar power system for the fort or deciding on fort construction material as part of a lock. External interfaces and the environment are still relevant and is discussed. In particular, note that the lock system does not actuate movement of the door itself.

## Use Cases
This section describes relevant use cases. Intent here is to capture general usage goals and what can go right or wrong.

**TODO: Write textual use cases with success and alternate scenarios to inform the AADL modeling**

Use Cases:
- Install Lock System: How will the homeowner install the lock on the door and support equipment?
- Maintain System: How will the homeowner adjust/maintain the system over time? Specifically thinking adjusting for seasons (i.e., temperature changes).
- Activate System: How will the homeowner "turn it on"?
- Deactivate System: How will the homeowner "turn it off"?
- Monitor System: How will the homeowner monitor the health and status of system?
- Safely Open Door: How will a person access the fort, which will exercise the lock?
- Safely Close Door: How does a person leave the fort in a secure (locked) state?
- Play in the Fort: What will normal play be? How will the system support continuous in/out, door propped open, a ball being bounced around and impacting system equipment?

## Elements
This section describes elements of the lock system as well as elements outside the system boundary relevant to the lock system.

- Fort: A required, physical component that is outside the system boundary. Essentially where all elements (except optional remote) is installed.
- Door Assembly: The door and door frame. The door frame is assumed to be where part of the lock assembly is installed. Physical components.
- Lock Assembly: The bolt and box of a lock. Using generic lock terminology, although implementation may not use the same terminololgy. The two minimum components of a lock but avoiding overly generic terms like "receptacle".  Physical components.
- Processor Assembly: The physical and logical components to suppor the lock assembly.
  - Enclosure: A physical component protecting elements of the processor assembly from the environment and accidental damage from normal play.
  - Power Supply: A logical construct of a physical component (or components) that minimally powers processor assembly components and may provide power to external components.  May also include backups, filtering/conditioning, power conversion, and more.
  - Processor: The physical, embedded computer that includes a processor to be the "brains" of the lock system.
  - Display: Physical indicators of status. May be a monitor, LCD display, or simple status LEDs.
  - Wired I/O: Any GPIO, serial, I2C, etc. interfaces between components. Assumes the system won't be fully wireless.
  - Connectors: The physical connector between wired i/o interfaces. Environmental features should be considered.
  - Wireless I/O (Optional?): The wireless interface(s) such as WiFi, Bluetooth, Zigbee, or any ISM connection between the processor assembly and any remote system. This may be used for monitoring, but is considered optional otherwise.
  - Wireless Antenna: The antenna for the wireless i/o.
  - "The Software": A placeholder to capture important software processes.
- Conduit (Optional?): Protects cabling from the environment, critters, and normal play. Technically optional until a need is validated.
- Cabling: Any cables (cat5/6, twisted pair, power, ...) between components. Assumes the system won't be fully wireless.
- Entry Pad: The device on the outside of the fort that is used to trigger user authentication for safe entry to the fort through the door. Pad implies more than a button is required for user authentication.
- Exit Button: The device on the inside of the fort that allows for safe exit from the fort through the door. Button implies no authentication is required to exit, so a simple button (or equiv) is sufficient.
- Motion Sensor (Optional?): Allows a remote monitor to detect motion inside the fort. This may be used for monitoring, but is considered optional otherwise. 
- Door Sensor (Optional?): A physical component installed on the door assembly to determine if the door is open/closed.  Example may be a hall effect sensor.
- Remote Processor Assembly (Optional?): This may be used for monitoring, but is considered optional otherwise.
  - Processor
  - Wireless I/O
  - Wireless Antenna

## States
This section describes system and component states. The list assumes the system is installed, skipping disassembled/assembled or "in transit" type states. The current intent uses information in this section as a basis for an AGREE specification. Future work may expand this to AADL Error Modeling Annex, AADL Behavior Annex, or AADL mode and mode-transition language features.

**TODO: Complete brainstorming, categorize as needed, connect with transitions, remove unneeded states after discussion/iterations**

### System Level
- **On:** System is on and must run a self-check (i.e., BIT) to determine next state.
- **Off:** System is off.
- **Operational:** System is fully functional - can be be locked/unlocked and  monitored - without issue.
- **Degraded:** Something is wrong - on battery backup, monitoring offline, or TBD - but Safely Open (and Close) Door use cases can still be accomplished 
- **Failsafe:** System is too degraded and must be unlocked and otherwise taken "offline"

| Current State | Events | Next State | Output |
| ------------- | ------ | ---------- | ------ |
| Off | Power Applied | On | The system is powered but not yet operational, so the lock mechanism must be (and stay) disengaged.
| Any | Power Removed | Off | The system has no power, so the lock mechanism must be (and stay) disengaged.
| On | BIT (Passed) | Operational | The system has completed a self-check with all components fully operational. The lock mechanism may be engaged or disengaged based on other conditions.
| Any, except Off | BIT (Degraded) | Degraded | The system has completed a self-check with something non-essential wrong. The lock mechanism may be engaged or disengaged based on other conditions.
| Any, except Off | BIT (Failed) | Failsafe | The system has completed a self-check and cannot operate. The lock mechanism must be (and stay) disengaged.

- **Locked:** The lock mechanism is engaged (that is, the door cannot be opened without disassembly).
- **Unlocked:** The lock mechanism is disengaged (that is, the door can be opened).

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
| Normal Play    | The activities by humans within the fort expected of kids and adults using a fort. As an outdoor environment, kids may be dirty (sand, dirt, mud), play more carelessly than inside (throw balls, swing sticks).  Abnormal activity would be striking components of the lock system with a hammer and destructive intent and other forms of purposeful vandalism.  | | 
| User | A human who can interact with the lock | |
| User Authentication | A part of the Lock System that can verify a user-provided authorization artifact (e.g., physical key, keycode) | | 

