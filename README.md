# OpenAIAPITest
Testing accessing the OPENAI API

# Technical Software Spec for a Program to Send Calls to OpenAI API with a Simple GUI

## Overview

The program is designed to allow users to send API calls to the OpenAI API with a simple GUI interface. This program will allow users to generate responses for various AI models provided by OpenAI, such as GPT-3, DALL-E, etc.

## Requirements

- Users should be able to enter their API keys in the program for authentication.
- Users should be able to select which OpenAI API model to use.
- Users should be able to enter text or upload an image to submit to the API for processing.
- Users should be able to view the API response in the program.
- The program should support both synchronous and asynchronous requests to the API.
- The program should handle any errors or exceptions gracefully, displaying an error message to the user if necessary.

## Components

The program will consist of two main components:

- The GUI interface: The user interface will allow users to interact with the program and make requests to the OpenAI API. The GUI will be built using a standard GUI framework such as Tkinter, PyQt, or WxPython.

- The API handler: This component will handle the authentication, API requests, and error handling. We will use the OpenAI Python library to make requests to OpenAI API. It will contain the following functions:

### `get_api_key()`

This function will allow the user to enter their OpenAI API key. It will display a dialog box prompting the user to enter the API key, and then return the entered key.

### `get_api_models()`

This function will return a list of available models in the OpenAI API. This list should be pulled from the OpenAI API documentation.

Example usage:

```python
models = get_api_models()
print(models)
# ['davinci', 'curie', 'babbage']
```

### `send_request(model, data, async=False)`

This function will send a request to the OpenAI API using the specified model and data. The `model` parameter should be a string indicating which OpenAI API model to use, and the `data` parameter should be either a string of text or a binary image file. The `async` parameter will be set to `False` by default, indicating that synchronous requests should be made, but when set to `True`, the function will make asynchronous requests.

Example usage:

```python
response = send_request('davinci', 'Hello, World!')
print(response)
# 'Hello, World, how are you doing today?'
```

### `handle_error(error)`

This function will handle any errors or exceptions that occur during API requests. It should display an error message to the user.

## Dependencies

- OpenAI Python library (to be installed with pip or conda)
- A standard GUI framework, such as Tkinter, PyQt, or WxPython

## Future Work

- Allow users to select multiple models to send the same request and compare the results.
- Allow users to store frequently-used models and data sets for easy access in the future.
- Add support for more OpenAI API endpoints, such as DALL-E, GPT-3, etc.
- Allow users to adjust options such as prompt length, temperature, and more for more customized responses.

## Conclusion

This Technical Software Spec outlines a program to allow users to send API calls to OpenAI API with a simple GUI to choose which API calls to make. The program will handle API authentication, requests, errors, and will be built using a standard GUI framework with the OpenAI Python library used for API requests.

Before building the project, we need to install the OpenAI API library. Let's install it using pip:

pip install openai
