---
id: bcab9ba104
question: 'For deployment, should I use a monolith (one container) or split the frontend and backend?'
sort_order: 1
---

Both work. A monolith (bundling the frontend build inside the backend container) is simpler to deploy, but on a free tier like Render the whole app sleeps. A split setup (static site + web service) keeps the frontend fast while the backend wakes up, but runs two instances and uses more hours. For the course either is fine - pick the monolith for simplicity unless free-tier cold starts bother you.
