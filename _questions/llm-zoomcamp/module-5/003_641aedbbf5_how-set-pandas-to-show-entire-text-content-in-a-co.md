---
id: 641aedbbf5
images:
- description: 'image #1'
  id: image_1
  path: images/llm-zoomcamp/image_603bbc41.png
question: How set Pandas to show entire text content in a column. Useful to view the
  entire Explanation column content in the LLM-as-judge section of the offline-rag-evaluation
  notebook
sort_order: 3
---

By default, Pandas truncates text content in a column to 50 characters. To view the entire explanation provided by the judge LLM for a non-relevant answer, use the following instruction:

```python
pd.set_option('display.max_colwidth', None)
```

### Explanation:

- **Option:** `display.max_colwidth`
- **Type:** `int` or `None`
- **Description:** Sets the maximum width in characters of a column in the representation of a pandas data structure. When a column overflows, a "..." placeholder is used in the output. Setting it to 'None' allows unlimited width.
- **Default:** 50

Refer to the [official documentation](https://pandas.pydata.org/docs/user_guide/options.html) for more details.

<{IMAGE:image_1}>
