---
id: 2e729f1271
question: 'Session State: I want the user to only be able to give feedback once per
  submission (+1 or -1). When I submit text using the ask button, the buttons should
  be disabled if `st.session.submitted` is False. The issue is mainly with `st.session.submitted`,
  which gets reassigned to True again despite one feedback button being pressed.'
sort_order: 7
---

Solved:

[Refer to the solution on Streamlit Discuss](https://discuss.streamlit.io/t/streamlit-session-attributes-reassigned-somewhere/76059/2?u=mohammed2)