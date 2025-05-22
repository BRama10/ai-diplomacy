import inspect

class IssuePublicStatement:
    def __init__(self, agent):
        self.agent_name = agent

    def __call__(self, content, attitude):
        """
        Make the action of issuing a public statement.
        Parameters:
        content (str): The content of the statement.
        attitude (str): The attitude of the statement (e.g., "positive", "negative", "neutral").
        Action Format: IssuePublicStatement(content=content, attitude=attitude)
        Execution Result:
        All other players will be notified of the statement.
        """
        output = f"{self.agent_name} just issued a public statement with attitude {attitude}: {content}"

        return output
    
