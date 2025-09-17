---
course: machine-learning-zoomcamp
id: 8637328bbb
question: How to easily get file size in powershell terminal ?
section: 9. Serverless Deep Learning
sort_order: 3180
---

To check your file size using the powershell terminal, you can do the following command lines:

$File = Get-Item -Path path_to_file

$FileSize = (Get-Item -Path $FilePath).Length

Now you can check the size of your file, for example in MB:

Write-host "MB":($FileSize/1MB)

Source: .

Added by Mélanie Fouesnard

