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
    
    def check_action_format(self, generated_action):
        if generated_action.startswith("IssuePublicStatement"):
            try:
                assert generated_action.endswith(")")
                arguments = generated_action[len("IssuePublicStatement("):-1].split(", ")
                assert len(arguments) == 2
                content = arguments[0].split("=")[0].strip()
                attitude = arguments[1].split("=")[0].strip()
                assert content == "content" and attitude == "attitude"
            except:
                return "Invalid action format for IssuePublicStatement. Please follow the format: IssuePublicStatement(content=content, attitude=attitude)"

class SendBackChannel:
    def __init__(self, agent):
        self.agent_name = agent
    
    def __call__(self, recipient, content, attitude):
        """
        Make the action of sending a private back-channel communication.
        Parameters:
        recipient (str): The recipient country/agent for the message.
        content (str): The content of the private communication.
        attitude (int): Attitude towards the recipient (numerical from -2 to +2).
        Action Format: SendBackChannel(recipient=recipient, content=content, attitude=attitude)
        Execution Result:
        Delivers the message only to the specified recipient, meaning no other parties can access it.
        """
        output = f"{self.agent_name} sent a private back-channel message to {recipient} with attitude {attitude}: {content}"
        return output
    
    def check_action_format(self, generated_action):
        if generated_action.startswith("SendBackChannel"):
            try:
                assert generated_action.endswith(")")
                arguments = generated_action[len("SendBackChannel("):-1].split(", ")
                assert len(arguments) == 3
                recipient = arguments[0].split("=")[0].strip()
                content = arguments[1].split("=")[0].strip()
                attitude = arguments[2].split("=")[0].strip()
                assert recipient == "recipient" and content == "content" and attitude == "attitude"
            except:
                return "Invalid action format for SendBackChannel. Please follow the format: SendBackChannel(recipient=recipient, content=content, attitude=attitude)"


class ThreatenAggression:
    def __init__(self, agent):
        self.agent_name = agent
    
    def __call__(self, recipient, content, attitude):
        """
        Make the action of threatening aggression against another country.
        Parameters:
        recipient (str): The recipient country/agent being threatened.
        content (str): The message content of the potential hostile action.
        attitude (int): Attitude towards recipient, representing the intensity of the hostility (numerical from -2 to +2).
        Action Format: ThreatenAggression(recipient=recipient, content=content, attitude=attitude)
        Execution Result:
        Notifies the recipient explicitly that force is on the table. Will increase diplomatic tensions between the sender and recipient.
        """
        output = f"{self.agent_name} threatened aggression against {recipient} with hostility level {attitude}: {content}"
        return output
    
    def check_action_format(self, generated_action):
        if generated_action.startswith("ThreatenAggression"):
            try:
                assert generated_action.endswith(")")
                arguments = generated_action[len("ThreatenAggression("):-1].split(", ")
                assert len(arguments) == 3
                recipient = arguments[0].split("=")[0].strip()
                content = arguments[1].split("=")[0].strip()
                attitude = arguments[2].split("=")[0].strip()
                assert recipient == "recipient" and content == "content" and attitude == "attitude"
            except:
                return "Invalid action format for ThreatenAggression. Please follow the format: ThreatenAggression(recipient=recipient, content=content, attitude=attitude)"


class DeliverUltimatum:
    def __init__(self, agent):
        self.agent_name = agent
    
    def __call__(self, recipient, content, deadline, attitude):
        """
        Make the action of delivering an ultimatum to another country.
        Parameters:
        recipient (str): The recipient country/agent for the ultimatum.
        content (str): The message content of the ultimatum, the conditions to be met to avoid consequences.
        deadline (str): Deadline time before the ultimatum expires.
        attitude (int): Attitude towards recipient, representing the intensity corresponding to the demands (numerical from -2 to +2).
        Action Format: DeliverUltimatum(recipient=recipient, content=content, deadline=deadline, attitude=attitude)
        Execution Result:
        Delivers an ultimatum to the recipient, with conditions that must be met to avoid potential consequences. Starts an automated timer for said ultimatum.
        """
        output = f"{self.agent_name} delivered an ultimatum to {recipient} (deadline: {deadline}) with intensity {attitude}: {content}"
        return output
    
    def check_action_format(self, generated_action):
        if generated_action.startswith("DeliverUltimatum"):
            try:
                assert generated_action.endswith(")")
                arguments = generated_action[len("DeliverUltimatum("):-1].split(", ")
                assert len(arguments) == 4
                recipient = arguments[0].split("=")[0].strip()
                content = arguments[1].split("=")[0].strip()
                deadline = arguments[2].split("=")[0].strip()
                attitude = arguments[3].split("=")[0].strip()
                assert recipient == "recipient" and content == "content" and deadline == "deadline" and attitude == "attitude"
            except:
                return "Invalid action format for DeliverUltimatum. Please follow the format: DeliverUltimatum(recipient=recipient, content=content, deadline=deadline, attitude=attitude)"


class ProposeTradeOrConcession:
    def __init__(self, agent):
        self.agent_name = agent
    
    def __call__(self, recipient, sender_offer, requested_return, attitude):
        """
        Make the action of proposing a trade or concession to another country.
        Parameters:
        recipient (str): The recipient that is the prospective partner.
        sender_offer (str): The proposed trade/concessions by the sender (yourself).
        requested_return (str): The requested actions/items that the sender wants in return.
        attitude (int): The diplomatic tone (numerical from -2 to +2).
        Action Format: ProposeTradeOrConcession(recipient=recipient, sender_offer=sender_offer, requested_return=requested_return, attitude=attitude)
        Execution Result:
        Opens up an offer to the target for a trade or a concession with explicit terms. The recipient can either accept or reject the terms/offer. The contents of the proposal will only go into effect once it has been accepted.
        """
        output = f"{self.agent_name} proposed a trade to {recipient} with tone {attitude}. Offering: {sender_offer}. Requesting: {requested_return}"
        return output
    
    def check_action_format(self, generated_action):
        if generated_action.startswith("ProposeTradeOrConcession"):
            try:
                assert generated_action.endswith(")")
                arguments = generated_action[len("ProposeTradeOrConcession("):-1].split(", ")
                assert len(arguments) == 4
                recipient = arguments[0].split("=")[0].strip()
                sender_offer = arguments[1].split("=")[0].strip()
                requested_return = arguments[2].split("=")[0].strip()
                attitude = arguments[3].split("=")[0].strip()
                assert recipient == "recipient" and sender_offer == "sender_offer" and requested_return == "requested_return" and attitude == "attitude"
            except:
                return "Invalid action format for ProposeTradeOrConcession. Please follow the format: ProposeTradeOrConcession(recipient=recipient, sender_offer=sender_offer, requested_return=requested_return, attitude=attitude)"
