---
id: 768fa21d6b
question: Where does pipenv create environments and how does it name them?
section: 5. Deploying Machine Learning Models
course: machine-learning-zoomcamp
sort_order: 1930
---

It creates them in

OSX/Linux: ~/.local/share/virtualenvs/folder-name_cyrptic-hash

Windows: C:\Users\<USERNAME>\.virtualenvs\folder-name_cyrptic-hash

Eg: C:\Users\Ella\.virtualenvs\code-qsdUdabf (for module-05 lesson)

The environment name is the name of the last folder in the folder directory where we used the pipenv install command (or any other pipenv command). E.g. If you run any pipenv command in folder path ~/home/user/Churn-Flask-app, it will create an environment named Churn-Flask-app-some_random_characters, and it's path will be like this: /home/user/.local/share/virtualenvs/churn-flask-app-i_mzGMjX.

All libraries of this environment will be installed inside this folder. To activate this environment, I will need to cd into the project folder again, and type pipenv shell. In short, the location of the project folder acts as an identifier for an environment, in place of any name.

(Memoona Tahira)

