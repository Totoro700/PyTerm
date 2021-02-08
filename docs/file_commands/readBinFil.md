# openBinFil

The `openBinFil` command opens a binary file (for opening *text* files, look for `openFil.md`). It will ask for the **full** file name, like `app.exe` ***OR*** the full file directory, like `C:\Scripts\main.dll` (you can use forward slashes ( `/` ) instead of backslashes ( `\` )), once you press `enter`, it should print the binary file



```
> openBinFil
Full binary file name or directory? (eg. "cmd.exe" or "C:\\Python\\python.dll")
C:\text.exe
b'\xa8\xa0\xb0\xa0\xb8\xa0\xc0\xa0\xc8\xa0\xd0\xa0\xd8\xa0\xe0\xa0\xf0\xa0\xf8\xa0\x08\xa1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

```

​                                                              ^

It should print something like that |, but longer (because it's binary)