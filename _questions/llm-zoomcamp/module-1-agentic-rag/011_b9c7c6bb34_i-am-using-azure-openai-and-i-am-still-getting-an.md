---
id: b9c7c6bb34
question: 'I am using Azure OpenAI and I am still getting an error of Error code:
  400 - {''error'': {''message'': "Missing required parameter: ''tools[0].function''.",
  ''type'': ''invalid_request_error'', ''param'': ''tools[0].function'', ''code'':
  ''missing_required_parameter''}}?'
sort_order: 11
---

Modify the `get_weather_tool` JSON to be the following:

```json
get_weather_tool = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a specific city or generate fake data",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The name of the city to get the weather for."
                }
            },
            "required": ["city"],
            "additionalProperties": false
        }
    }
}
```