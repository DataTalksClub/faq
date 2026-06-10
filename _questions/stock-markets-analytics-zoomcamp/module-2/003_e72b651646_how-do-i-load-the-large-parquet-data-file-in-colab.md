---
id: e72b651646
question: 'How do I load the large parquet data file in Colab?'
sort_order: 3
---

Either mount Google Drive and read the file from your drive, or use gdown with the --fuzzy flag to download a shared Drive link directly into the Colab session, then read it with pd.read_parquet.
