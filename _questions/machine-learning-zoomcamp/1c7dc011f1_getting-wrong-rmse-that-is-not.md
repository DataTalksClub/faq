---
id: 1c7dc011f1
question: Getting Wrong RMSE that is not matching or close to answer options in HW 2(Regression) of 2024 Cohort.
section: Miscellaneous
course: machine-learning-zoomcamp
sort_order: 4270
---

The following piece of code which involves shuffling is crucial to getting RMSE which is close to the ones in the answer options in the homework.

df = orig_df.copy()

base = ['ram','storage','screen','final_price']

my_df = df[base]

idx = np.arange(n)

np.random.seed(s)

np.random.shuffle(idx)

df_shuffled = my_df.iloc[idx]

df_train = df_shuffled.iloc[idx[:n_train]].copy()

df_val = df_shuffled.iloc[idx[n_train:n_train+n_val]].copy()

df_test = df_shuffled.iloc[idx[n_train+n_val:]].copy()

df_train = df_train.reset_index(drop=True)

df_val = df_val.reset_index(drop=True)

df_test = df_test.reset_index(drop=True)

y_train = df_train.final_price.values

y_val =  df_val.final_price.values

y_test = df_test.final_price.values

del df_train['final_price']

del df_val['final_price']

del df_test['final_price']

2.	if we don't get this logic right, then all the RMSE gets messed up. Do double check in your codes.

CUDA ran out of memory in google collab

Most of the time when we are trying to run the models on collab or kaggle , we tend to face the  runtime error of CUDA out of memory.

Tips to overcome this :

Reduce the batch size .

Use lower precision

Something the memory can be allocated for things which we aren’t using it recently , so try to clear the cache

Import torch 
torch.cuda.empty_cache()  // free up the GPU memory space.

Delete unnecessary variables

Follow the links below to get a deep view of it .

(added by Nikisha)

