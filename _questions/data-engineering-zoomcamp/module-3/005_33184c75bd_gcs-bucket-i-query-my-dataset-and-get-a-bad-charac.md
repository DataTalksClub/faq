---
id: 33184c75bd
question: GCS Bucket - I query my dataset and get a Bad character (ASCII 0) error?
sort_order: 5
---

- **Check the Schema**: Ensure that the schema of your dataset is correctly defined.

- **Formatting Issues**: You might have incorrect formatting in your files.

- **Upload Method**: Try uploading the CSV.GZ files without formatting or processing them through pandas. Use `wget` to download if necessary.