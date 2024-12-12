import PyInstaller.__main__

PyInstaller.__main__.run([
    'client.py',
    '--onefile',
    '--noconsole',
    '--distpath', 'building/dist',
    '--workpath', 'building/build',
    '--specpath', 'building/spec',
    '--icon', 'icon.ico',  # Set the path to your icon file
    '--name', 'mariouwu'  # Set the desired name for the executable
])
