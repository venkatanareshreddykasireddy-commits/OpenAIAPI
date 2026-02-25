
from openai import OpenAI

def main():
    
    # Create a client — authenticates and configures the API connection
    client = OpenAI(api_key="YOUR_API_KEY_HERE")

    # Send a request to the Chat Completions endpoint
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "What is the OpenAI API?"}
        ]
    )
    
    # Print the response from the API
    print(response)

if __name__ == "__main__":
    main()