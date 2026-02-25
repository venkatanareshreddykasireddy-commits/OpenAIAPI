
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
    
# Print the response content from the API
    # The choices field is a list — grab the first item
    print(response.choices[0])
    # That Choice has a .message attribute
    print(response.choices[0].message)
    # And .message has a .content attribute - the plain text string
    result = response.choices[0].message.content
    print(result)

if __name__ == "__main__":
    main()