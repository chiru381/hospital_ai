from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "AI Assistant"
)

@mcp.tool()
def search_docs(query: str):

    from app.services.rag_service import retrieve_context

    return retrieve_context(query)

@mcp.tool()
def get_user(user_id: int):

    return {
        "user_id": user_id,
        "name": "Demo User"
    }

if __name__ == "__main__":
    mcp.run()