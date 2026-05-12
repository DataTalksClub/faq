---
id: 02bb92c002
question: How to install easily kubectl on Windows?
sort_order: 11
---

To install kubectl on Windows using PowerShell in VSCode, follow these steps:

1. **Download kubectl with curl**
   - Use the following command lines as per the [Kubernetes documentation](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/#install-kubectl-binary-with-curl-on-windows).

2. **Copy the Executable**
   - At step 3 of the tutorial, copy the `kubectl.exe` file to a specific folder on your C drive.

3. **Update the System PATH**
   - Add the folder path to the PATH in your environment variables.

You can also install `kind` similarly using the curl command on Windows by specifying a folder that will be added to the PATH environment variable.

For detailed guidance, refer to this [Medium tutorial](https://medium.com/@ggauravsigra/install-kubectl-on-windows-af77da2e6fff).