---
id: 2e729f1271
question: "Streamlit: why does `st.session_state.submitted` reset to `True`, so the
  +1 / -1 feedback buttons stay enabled and accept more than one vote per answer?"
sort_order: 7
---

Two things cause it. Fix both:

1. Initialize the flag only when it is missing. A plain
   `st.session_state.submitted = False` at the top of the script runs again on
   every rerun and overwrites whatever the buttons just set.
2. Call `st.rerun()` after a button changes the flag. Streamlit runs the script
   top to bottom, so widgets that were already drawn in this run keep the
   `disabled` value they were created with. Without the rerun, the buttons only
   catch up on the next interaction.

```python
import streamlit as st

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "feedback" not in st.session_state:
    st.session_state.feedback = []

question = st.text_input("Your question")

if st.button("Ask"):
    st.session_state.submitted = True
    st.rerun()

col_up, col_down = st.columns(2)

with col_up:
    if st.button("+1", disabled=not st.session_state.submitted):
        st.session_state.feedback.append((question, +1))
        st.session_state.submitted = False
        st.rerun()

with col_down:
    if st.button("-1", disabled=not st.session_state.submitted):
        st.session_state.feedback.append((question, -1))
        st.session_state.submitted = False
        st.rerun()

st.write(st.session_state.feedback)
```

Setting `submitted` back to `False` inside each feedback branch is what limits
the user to one vote: the buttons render disabled until the next "Ask".

See the [Session State
docs](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state)
and the [original discussion on Streamlit
Discuss](https://discuss.streamlit.io/t/streamlit-session-attributes-reassigned-somewhere/76059/2).
