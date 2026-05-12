---
id: 8637328bbb
question: How to easily get file size in PowerShell terminal?
sort_order: 13
---

To check your file size using the PowerShell terminal, you can use the following command lines:

```powershell
$File = Get-Item -Path path_to_file
$fileSize = (Get-Item -Path $File).Length
```

Now you can check the size of your file, for example in MB:

```powershell
Write-Host "MB: " ($fileSize/1MB)
```

[Source](https://www.sharepointdiary.com/2020/10/powershell-get-file-size.html#:~:text=To%20get%20the%20size%20of,the%20file%2C%20including%20its%20size)