---
id: 0482efe115
question: Get_feature_names() not found
section: Miscellaneous
course: machine-learning-zoomcamp
sort_order: 4010
---

Problem: In the course this function worked to get the features from the dictVectorizer instance: dv.get_feature_names(). But in my computer did not work. I think it has to do with library versions and but apparently that function will be deprecated soon:

Old:

New:

Solution: change the line dv.get_feature_names() to list(dv.get_feature_names_out))

Ibai Irastorza

