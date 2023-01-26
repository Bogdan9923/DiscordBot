from projectSecrets import get_openai_key
import openai


def query_response(argument):
    prompt = ' '.join(argument)

    api_key = get_openai_key()
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.6
    )

    return response['choices'][0]['text']
