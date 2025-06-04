def issue_public_statement(agent_name, content, attitude):
    """
    Issue a public statement action.
    
    Parameters:
    agent_name (str): The name of the agent/country issuing the statement
    content (str): The content of the statement
    attitude (str): The attitude of the statement (e.g., "positive", "negative", "neutral")
    
    Returns:
    dict: Action result with simulated effects
    """
    
    # Simulate broadcasting to other players
    other_players = ["USA", "Russia", "China", "UK", "France"]
    other_players = [p for p in other_players if p != agent_name]
    
    # Simulate logging to game history
    game_log_entry = f"Turn 15: {agent_name} issued public statement with {attitude} attitude"
    
    # Simulate diplomatic relation changes
    relation_change = {
        "positive": +0.1,
        "negative": -0.1, 
        "neutral": 0.0,
        "hostile": -0.2,
        "friendly": +0.2
    }.get(attitude, 0.0)
    
    # Simulate triggered game mechanics
    mechanics = []
    if "war" in content.lower() or "attack" in content.lower():
        mechanics.append("tension_increased")
    if "peace" in content.lower() or "cooperation" in content.lower():
        mechanics.append("peace_bonus")
    
    # Return the action result
    return {
        "action_taken": f"{agent_name} publicly states: '{content}'",
        "broadcasted_to": other_players,
        "logged_as": game_log_entry,
        "diplomatic_impact": relation_change,
        "mechanics_triggered": mechanics,
        "attitude": attitude
    }


# Example usage:
if __name__ == "__main__":
    
    result1 = issue_public_statement("USA", "We stand for peace and cooperation", "positive")
    print("Result 1:", result1)
    print()
    
    result2 = issue_public_statement("Russia", "We will not tolerate further aggression", "hostile")
    print("Result 2:", result2)
    print()
    
    result3 = issue_public_statement("China", "Our position remains unchanged", "neutral")  
    print("Result 3:", result3)
