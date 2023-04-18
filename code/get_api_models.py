import openai

def get_api_models():
    """
    Returns a list of available OpenAI API models.
    """
    models = []
    try:
        models = openai.Model.list()
        models = [model.id for model in models['data']]
    except Exception as e:
        handle_error(e)
    return models
