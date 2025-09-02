import os
from openai import AsyncOpenAI  

openai_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


async def send_message(message: str, system_prompt: str) -> str:
    response = await openai_client.chat.completions.create(
        model="gemini-2.5-flash-lite",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ]
    )
    
    response = response.choices[0].message.content    
    if not response:
        raise ValueError("No response from Gemini")
    
    return response
