---
course: mlops-zoomcamp
id: 69052b9af2
question: Cannot generate pipfile.lock raise InstallationError( pip9.exceptions.InstallationError)
section: 'Module 4: Deployment'
sort_order: 1690
---

Problem description cannot generate pipfile.lock raise InstallationError( pip9.exceptions.InstallationError: Command "python setup.py egg_info" failed with error code 1

Solution: you need to force and upgrade wheel and pipenv

Just run the command line :

pip install --user --upgrade --upgrade-strategy eager pipenv wheel

