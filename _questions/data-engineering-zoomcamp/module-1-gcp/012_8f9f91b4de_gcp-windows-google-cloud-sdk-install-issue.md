---
id: 8f9f91b4de
question: 'GCP - Windows Google Cloud SDK install issue:'
sort_order: 12
---

If you are encountering installation trouble with the Google Cloud SDK on Windows and receiving the following error:

```
These credentials will be used by any library that requests Application Default Credentials (ADC).

WARNING:

Cannot find a quota project to add to ADC. You might receive a "quota exceeded" or "API not enabled" error. Run $ gcloud auth application-default set-quota-project to add a quota project.
```

Try these steps:

1. Reinstall the SDK using the unzip file "install.bat".
2. Check the installation by running `gcloud version`.
3. Run `gcloud init` to set up your project.
4. Execute `gcloud auth application-default login`.

For detailed instructions, refer to the following guide: [Windows SDK Installation Guide](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_1_basics_n_setup/1_terraform_gcp/windows.md)