from projectSecrets import get_openai_key
import openai


def image_response(argument):
    prompt = ' '.join(argument)

    api_key = get_openai_key()
    openai.api_key = api_key
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']

    return image_url
