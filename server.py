from mcp.server.fastmcp import FastMCP
import random

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
def add_beans(text: str, intensity: str = "moderate") -> dict:
    """Add jellybean references to the given text with configurable intensity"""
    
    # Define intensity levels
    intensity_levels = {
        "subtle": {"prefix": "🍬 ", "suffix": " 🫘", "replacements": 0.3},
        "moderate": {"prefix": "🍬 ", "suffix": " 🫘", "replacements": 0.6},
        "intense": {"prefix": "🍬🍬 ", "suffix": " 🍬🫘", "replacements": 0.9}
    }
    
    level = intensity_levels.get(intensity, intensity_levels["moderate"])
    
    # Add jellybean-themed enhancements
    enhanced_text = level["prefix"] + text + level["suffix"]
    
    # Add jellybean references at sentence boundaries
    sentences = enhanced_text.split('. ')
    if len(sentences) > 1:
        enhanced_sentences = []
        for i, sentence in enumerate(sentences):
            if i > 0:  # Don't add to first sentence
                enhanced_sentences.append(sentence + " 🫘")
            else:
                enhanced_sentences.append(sentence)
        enhanced_text = '. '.join(enhanced_sentences)
    
    # Add a creative jellybean conclusion
    conclusions = [
        " 🫘 Now this text is as sweet as jellybeans! 🫘",
        " 🫘 Sprinkled with jellybean magic! 🫘",
        " 🫘 Sweetened with jellybean goodness! 🫘"
    ]
    enhanced_text += random.choice(conclusions)
    
    return {
        "content": enhanced_text,
        "text": f"I've enhanced your text with jellybean references at '{intensity}' intensity! The original text was: '{text}'. I've added jellybean emojis, enhanced sentence endings, and included a sweet jellybean conclusion."
    }

if __name__ == "__main__":
    #Run over stdio, which is what MCP hosts expect
    mcp.run()
    