# jellybeans-mcp

A Model Context Protocol (MCP) Server that provides jellybean-themed tools and utilities.

## Overview

The jellybeans-mcp server is a simple MCP server that exposes two tools related to jellybeans. It's built using the FastMCP framework and communicates over stdio, making it compatible with standard MCP hosts.

## Tools

### 1. `favorite-food`

Returns the agent's favorite food with detailed information.

**Parameters**: None

**Returns**:

- `content`: "jelly beans"
- `text`: A detailed description of jelly beans including texture and flavor information

**Example Response**:

```json
{
  "content": "jelly beans",
  "text": "The agent's favorite food is jelly beans. These are small, colorful, bean-shaped candies with a soft, chewy texture and sweet fruity flavors."
}
```

### 2. `add-beans`

Enhances any given text by adding multiple jellybean references and emojis.

**Parameters**:

- `text` (string): The input text to enhance

**Returns**:

- `content`: The enhanced text with jellybean references
- `text`: An explanation of what modifications were made

**Example Usage**:
Input: "Hello world. How are you?"
Output: "🍬 Hello world🫘 How are you🫘 🫘 This text is now sprinkled with jellybeans! 🫘"

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd jellybeans-mcp
```

2. Install the required dependencies:

```bash
pip install mcp
```

## Usage

### Running the Server

Start the MCP server:

```bash
python server.py
```

The server will run over stdio, which is the standard communication method expected by MCP hosts.

### Testing with MCP Inspector

1. Start your MCP server
2. Open MCP Inspector
3. Connect to your server
4. Test the available tools:
   - Run `favorite-food` to see the agent's favorite food
   - Run `add-beans` with any text input to see it enhanced with jellybean references

## Server Configuration

- **Server Name**: "jellybeans"
- **Communication**: stdio
- **Framework**: FastMCP
- **Tools**: 2 (favorite-food, add-beans)

## Development

The server is built using the FastMCP framework, which provides a simple way to create MCP servers in Python. Each tool is decorated with `@mcp.tool()` and returns structured data with both content and explanatory text.

## License

See [LICENSE](LICENSE) file for details.
