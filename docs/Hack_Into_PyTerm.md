# How to hack into PyTerm

First, you have to understand where PyTerm stores data.

## Store

The `store` command let's you store things. But you can change them manually, instead of going into PyTerm and changing it! Go to the folder next to the program. Open the folder `user_data` This is the folder where PyTerm stores data. Then, open `info.txt`. That's the text you stored using PyTerm `store` command!

## Cache

Same thing, but `cache.txt`

If the cache is 1, that means you've ran PyTerm before, else it will be empty

## Color

It's the same thing for color, go to `user_data` but then click the folder `settings`, then click `color.txt`

`color.txt` will have two characters, the first is a number which will be the foreground/text color, second, is a letter ( `A` to `F` ) which defines the background color

## Prompt

The default prompt is "`>`" 

Path: `user_data/settings/prompt.txt`

Complete these steps:

- [ ] Open the `user_data` folder
- [ ] Open the `settings` folder
- [ ] Double click/open the file `prompt.txt`
- [ ] Change the text (the program will automatically add a space right after)
- [ ] Save file
- [ ] Open PyTerm

You should see the new prompt now!