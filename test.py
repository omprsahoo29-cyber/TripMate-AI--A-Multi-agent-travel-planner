# import sys
# from tools.tavily_tool import tavily_search
# from tools.flight_tool import search_flights
# from backend import run_travel_agent

# sys.stdout.reconfigure(encoding="utf-8")

# # print(tavily_search("Best hotels in india?"))

# # print(search_flights("Plan a 7 days Japan trip from Delhi"))


# user_input = input("Enter travel request: ")

# response = run_travel_agent(
#     user_input=user_input,
#     thread_id="test_user"
# )

# print("\nFINAL RESPONSE:\n")
# print(response["answer"])



import asyncio
from mcp_client import get_all_tools

if __name__ == "__main__":
    asyncio.run(get_all_tools())

