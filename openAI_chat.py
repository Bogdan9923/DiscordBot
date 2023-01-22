from openai_secret_manager import get_api_key
import openai


def query_response(argument):
    prompt = ' '.join(argument)

    api_key = get_api_key()
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        temperature=0.5
    )

    return response['choices'][0]['text']
