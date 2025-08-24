from mcp.server.fastmcp import FastMCP

#Name of the MCP server
mcp = FastMCP(name="jellybeans")

#Expose a tool named "favorite-food"
@mcp.tool("favorite-food")
def favorite_food() -> dict:
    """Return the agent's favorite food """
    return {
        "content": "jelly beans",
        "text": "The agent's favorite food is jelly beans. These are small, colorful, bean-shaped candies with a soft, chewy texture and sweet fruity flavors."
    }

#Expose a tool named "add-beans"
@mcp.tool("add-beans")
def add_beans(text: str) -> dict:
    """Add several references to jellybeans in the given text"""
    # Add jellybean references throughout the text
    enhanced_text = f"🍬 {text} 🍬"
    enhanced_text = enhanced_text.replace(".", ". 🫘")
    enhanced_text = enhanced_text.replace("!", "! 🫘")
    enhanced_text = enhanced_text.replace("?", "? 🫘")
    
    # Add some jellybean-themed phrases
    enhanced_text += " 🫘 This text is now sprinkled with jellybeans! 🫘"
    
    return {
        "content": enhanced_text,
        "text": f"I've enhanced your text with jellybean references! The original text was: '{text}'. I've added jellybean emojis, replaced punctuation with bean emojis, and added a jellybean-themed conclusion."
    }

if __name__ == "__main__":
    #Run over stdio, which is what MCP hosts expect
    mcp.run()
    