from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Math")

@mcp.tool()
def add(a:int,b:int)->int:
    """_sumary_
    Add to numbers
    """
    return a+b

@mcp.tool()
def multiple(a:int,b:int)->int:
    """Multiply to numbers"""
    return a*b

#the transport "stdio" argument tells the server to
#Use standard I/p and O/p stdin and stdout to recieve and respond to the tool function calls
if __name__ == "__main__":
    mcp.run(transport="stdio") 
    

