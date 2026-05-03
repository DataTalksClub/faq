---
id: 8d23fe792f
question: 'Authentication: Safe and easy way to store and load API keys'
sort_order: 7
---

You can store your different API keys in a YAML file that you will add to your `.gitignore` file. Be careful to never push or share this file.

For example, create a new file named `api_keys.yml` in your repository.

Then, add it to your `.gitignore` file:

```
#api_keys

api_keys.yml
```

Fill your `api_keys.yml` file:

```
OPENAI_API_KEY: "sk[...]"
GROQ_API_KEY: "gqk_[...]"
```

Save your file.

You will need the pyyaml library to load your YAML file, so run this command in your terminal:

```bash
pip install pyyaml
```

Now, open your Jupyter notebook.

You can load your YAML file and the associated keys with this code:

```python
import yaml

# Open the file
with open('api_keys.yml', 'r') as file:
    # Load the data from the file
    data = yaml.safe_load(file)

# Get the API key (Groq example here)
groq_api_key = data['GROQ_API_KEY']
```

Now, you can easily replace the `api_key` value directly with the loaded values without loading your environment variables.