---
id: 85c83560c5
question: Creating Helper functions in Mage
section: Module 3: Orchestration
course: mlops-zoomcamp
sort_order: 1380
---

There’s no need to add the utilities functions in each sub-project when you watch the videos as there only need to be one set. Just verify the code is still the same as in Mage’s mlops repository.

As from the import statements

from mlops.utils.[...] import [...]

all refer to the same path in the main mlops “parent” project:

/[mage-mlops-repository-name]/mlops/utils/...

