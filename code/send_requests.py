import threading
from get_api_key import get_api_key

def send_request(model, data, async=False):
    """
    Sends a request to the OpenAI API using the specified model and data.
    """
    api_key = get_api_key()
    if not api_key:
        return
    openai.api_key = api_key
    try:
        if async:
            t = threading.Thread(target=send_async_request, args=(model, data))
            t.start()
        else:
            response = None
            if model == "text":
                response = openai.Completion.create(
                  engine=model,
                  prompt=data
                )
                response = response.choices[0].text
            else:
                response = "Image processing not implemented yet"
            return response
    except Exception as e:
        handle_error(e)

def send_async_request(model, data):
    """
    Sends an asynchronous request to the OpenAI API using the specified model and data.
    """
    response = send_request(model, data)
    # Do something with the response
