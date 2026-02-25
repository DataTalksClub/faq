---
id: a1ea959c7e
question: Module “kafka” not found when trying to run producer.py
sort_order: 3
---



To resolve the "Module 'kafka' not found" error when running `producer.py`, you can create a virtual environment and install the required packages. Follow these steps:

1. **Create a Virtual Environment**
   
   Run the following command to create a virtual environment:
   
   ```bash
   python -m venv env
   ```

2. **Activate the Virtual Environment**

   - On macOS and Linux:
     
     ```bash
     source env/bin/activate
     ```
   
   - On Windows:
     
     ```bash
     env\Scripts\activate
     ```

3. **Install Required Packages**
   
   Install the packages listed in `requirements.txt`:
   
   ```bash
   pip install -r ../requirements.txt
   ```

4. **Deactivate the Virtual Environment**
   
   When you're done, deactivate the virtual environment:
   
   ```bash
   deactivate
   ```

**Note:** Ensure that Docker images are running before executing the Python file. The virtual environment is meant for running the Python files locally.