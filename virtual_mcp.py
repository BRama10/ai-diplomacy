import inspect
from action_space import IssuePublicStatement

class ActionSpaceManagement:
    def __init__(self):
        self.action_space_prompt = 'Below are the avaible actions that you can do towarsd other players:\n'

    def add_actions(self, list_of_actions):
        for action in list_of_actions:
            tools = inspect.getmembers(action, predicate=inspect.ismethod)
            for function_name, function in tools:
                if function_name == '__call__':
                    action_name = type(action).__name__
                    argument = ', '.join(list(function.__code__.co_varnames[:function.__code__.co_argcount][1:]))
                    description = ' '.join([d.strip() for d in function.__doc__.split('\n')])
                    self.action_space_prompt += f"""
Action Name: {action_name}
Action Argument: {argument}
Action Description: {description}
"""

    def remove_actions(self, list_of_actions):
        for action in list_of_actions:
            tools = inspect.getmembers(action, predicate=inspect.ismethod)
            for function_name, function in tools:
                if function_name == '__call__':
                    action_name = type(action).__name__
                    argument = ', '.join(list(function.__code__.co_varnames[:function.__code__.co_argcount][1:]))
                    description = ' '.join([d.strip() for d in function.__doc__.split('\n')])
                    self.action_space_prompt = self.action_space_prompt.replace(f"Action Name: {action_name}", "")
                    self.action_space_prompt = self.action_space_prompt.replace(f"Action Argument: {argument}", "")
                    self.action_space_prompt = self.action_space_prompt.replace(f"Action Description: {description}", "")


if __name__ == '__main__':
    action_space = ActionSpaceManagement()
    a1 = IssuePublicStatement('agent1')
    action_space.add_actions([a1])
    print(action_space.action_space_prompt)

    action_space.remove_actions([a1])
    print(action_space.action_space_prompt)