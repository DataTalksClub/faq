---
course: mlops-zoomcamp
id: ebd339f9a5
question: Error when importing evidently package because of numpy version upgraded
section: 'Module 5: Monitoring'
sort_order: 2060
---

A new version of Numpy has just been released v 2.0.0 (on Jun 16, 2024), and this causes an import error of the package.

"`np.chararray` is deprecated and will be removed from "

419     	"the main namespace in the future. Use an array with a string "

420     	"or bytes dtype instead.", DeprecationWarning, stacklevel=2): `np.float_` was removed in the NumPy 2.0 release. Use `np.float64` instead.

Or

AttributeError: `np.float_` was removed in the NumPy 2.0 release. Use `np.float64` instead.

You can solve it by reinstalling numpy to previous version 1.26.4. Just run:

python -m pip install numpy==1.26.4

Or modify the requirements.txt to freeze the version:

numpy==1.26.4

Added by Eduardo Muñoz

Problem: Grafarna and Adminer not showing at their designated URIs after Docker Compose

Solution: If you are using a VM, you will have to forward the ports (on VS Code or any other editor)

Added by Oluwadara Adedeji

