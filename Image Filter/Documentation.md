# Value Filter
This is a python program that will apply a Value filter to your main screen (number 1 at Display Settings).

That means it will only show the value of colors in the window.

The program is running in the background, so if you press the shortcut at any point, it will open the Filter window.
If you are in Task Manager, the shorcut doesn't work for some reason.

If you have the Filter window open and press pause shorcut, it will freeze and the content won't be updated until you unpause it again (with the same shorcut).

# config.txt
"resolution_downscale": how many times will the filter window be smaller than original resolution.
Must be a number, any number (1+)
"shorcut": keys required to start and close the filter window
"pause": keys required to freeze and unfreeze the filter window

# Install
Check out InstallationGuide.

# Compatibility
The program requires an NVIDIA GPU with CUDA cores. How to check: Find your GPU at the bottom of Task Manager -> Performance.

Type into google: does [my gpu] have CUDA cores
