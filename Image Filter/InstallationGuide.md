# Install python
Go to: https://www.python.org/downloads/
and install the latest version.

## MAKE SURE TO INCLUDE PYTHON IN PATH, IT WILL ASK YOU FOR THIS OPTION, A LITTLE CHECKBOX

# Instal CUDA Toolkit

Go to: https://developer.nvidia.com/cuda-downloads
and install the toolkit.

# Install Value Filter
Copy the "Value Filter" folder from P:/GRAPHICS/SP_color_tool somewhere to your pc.

Open Terminal inside your Value Filter folder (type cmd to path and enter).

Type: pip install -r requirements.txt

# Customize settings
Open config.json in a text editor of your choice (notepad, vs, vim ...).
Edit the settings to your liking. To get key codes, open KeyCode.py and it will show you the key codes of keys you are pressing.

If you change the settings while the program is running, you need to manually close it and reopen it again. Close process: Task Manager -> Details -> pythonw.exe. Then open ImageFilterStartup.pyw.

# Launch on pc start
Go to shell:startup (either as path, or Win + R). Copy a shortcut of ImageFilterStartup.pyw into this folder.
