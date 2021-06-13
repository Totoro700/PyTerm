# deleteuserdata

The `clearData` command clears all user data in PyTerm ( `user_data` folder ), it uses `shutil.rmtree` to delete the folder. When you delete the user data, **all** information you stored using `info` or `info -s`, the cache made by PyTerm, text and background color, the prompt, will all be deleted. PyTerm will confirm you actually want to delete the data, before deleting it.



```
> deleteuserdata
Are you sure you want to delete all user data?     Y/N
Y
Clearing data . . .
Finished!
> 
```

In this case, the answer is yes (Y), the answer is not case sensitive.