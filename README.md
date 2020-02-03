# web2py-desktop 
How to make web2py Windows & Macintosh binaries with pyinstaller and [pywebview](https://github.com/r0x0r/pywebview).
Forked from [nicozanf/web2py-pyinstaller](https://github.com/nicozanf/web2py-pyinstaller). Read your documentation for more details.

## Instructions(for Windows x64 bits)
1. Get a clean Windows 10 (Windows 10 Home 64 bit, under Virtualbox in my case).
2. Grab and install the official Python program: I've got version 3.7.4, 64 bit (https://www.python.org/ftp/python/3.7.2/python-3.7.3-amd64.exe ) + select "add Python 3.7 to PATH" during its setup if Python 3.
3. Update tools with
```
python -m pip install --upgrade pip
pip install --upgrade setuptools
```
4. Grab latest [web2py source](https://mdipierro.pythonanywhere.com/examples/static/web2py_src.zip) (you need at least 2.18.3 for needed changes in gluon\admin.py). Unzip it in a dedicated folder, in this example `C:\web2py`- so that you have `C:\web2py\web2py.py` inside.
5. Install PyInstaller with
```
pip install pyinstaller
```
6. Install requirements with:
```
pip install -t site-packages cefpython3
pip install -t site-packages pywebview
```
See [HOWTO-modules](https://github.com/bruino/web2py-pyinstaller/blob/master/HOWTO-modules.md) for more details.

7. (For Windows 7) download and install the free Microsoft Visual C++ Redistributable per Visual Studio 2017, 64 bit version.

8. Copy from this repository `start.py` to `C:\web2py\`.

9. Copy `build_web2py.py`, `web2py.win.spec` and `web2py.win_no_console.spec` from this repository to `C:\web2py\`

10. Open a CMD and go to `C:\web2py`. Run:
```
python build_web2py.py`
```
If everything goes fine, you'll obtain the 64 bit binary build zipped as `C:\web2py\web2py_win.zip`.
