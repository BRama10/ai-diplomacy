# AI diplomacy

## Action Space Design

Each player will be implemented as one agent + one MCP. 

All actions are included in action_space.py

**Each action is implemented as a function class** including methods of

-- initialization

-- function call

-- format checker

I am also thinking about adding an execution method for each action class.

The virtual_mcp.py manages the actions for each agent/player, where we can easily add and delete available actions for this player. For each agent/player, we initializes their own MCP. The actions classses need to be initialized as class object and then add to the MCP. The MCP will generate the action space prompt to send to the LLM endpoint.


## Profile Design 



## Negotiation Flow Design
