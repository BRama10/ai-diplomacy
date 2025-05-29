import inspect
from action_space import IssuePublicStatement

class ActionSpaceManagement:
    def __init__(self):
        self.base_prompt = 'Below are the available actions that you can do toward other players:\n'
        self.action_blocks = {}  # Store each action's complete block
    
    @property
    def action_space_prompt(self):
        """Generate the full prompt by combining base prompt with all action blocks"""
        if not self.action_blocks:
            return self.base_prompt
        
        full_prompt = self.base_prompt
        for action_block in self.action_blocks.values():
            full_prompt += action_block
        
        return full_prompt

    def add_actions(self, list_of_actions):
        for action in list_of_actions:
            tools = inspect.getmembers(action, predicate=inspect.ismethod)
            for function_name, function in tools:
                if function_name == '__call__':
                    action_name = type(action).__name__
                    argument = ', '.join(list(function.__code__.co_varnames[:function.__code__.co_argcount][1:]))
                    description = ' '.join([d.strip() for d in function.__doc__.split('\n')])
                    
                    # Store the complete action block
                    action_block = f"""
Action Name: {action_name}
Action Argument: {argument}
Action Description: {description}
"""
                    self.action_blocks[action_name] = action_block

    def remove_actions(self, list_of_actions):
        for action in list_of_actions:
            action_name = type(action).__name__
            # Simply remove the action block by its name
            if action_name in self.action_blocks:
                del self.action_blocks[action_name]


if __name__ == '__main__':
    action_space = ActionSpaceManagement()
    a1 = IssuePublicStatement('agent1')
    action_space.add_actions([a1])
    print(action_space.action_space_prompt)

    action_space.remove_actions([a1])
    print(action_space.action_space_prompt)

    agent_name = "USA"
    
    actions = [
        IssuePublicStatement(agent_name),
        SendBackChannel(agent_name),
        ThreatenAggression(agent_name),
        DeliverUltimatum(agent_name),
        ProposeTradeOrConcession(agent_name)
    ]
    
    action_space.add_actions(actions)
    
    print(action_space.action_space_prompt)
    
    back_channel = SendBackChannel("USA")
    print(back_channel("China", "We need to discuss the trade situation privately", 0))
    
    threat = ThreatenAggression("USA")
    print(threat("Russia", "Cease your military buildup or face consequences", -2))
    
    ultimatum = DeliverUltimatum("USA")
    print(ultimatum("Iran", "Halt nuclear enrichment within 30 days", "30 days", -1))
    
    trade = ProposeTradeOrConcession("USA")
    print(trade("EU", "Reduce tariffs on agricultural products", "Increase technology sharing agreements", 1))

    action_space.remove_actions([*actions])
    print(action_space.action_space_prompt)
