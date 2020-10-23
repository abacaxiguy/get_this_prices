# get_this_prices

A python script that requests prices from Kabum.com.br and add it to a spreadsheet


## How to use

Requirements:

- [Python](https://www.python.org/)


First and foremost, to run this script its necessary that you create your virtual environment in this folder:

```bat
python -m venv venv
```


With the venv set, you need to install the [dependencies.txt](/dependencies.txt):

```bat
call venv/Scripts/activate.bat

pip install -r dependencies.txt

call venv/Scripts/deactivate.bat
```


Create a shortcut to [run.bat](/run.bat) and put it to your Startup folder, to open your Startup folder just hit Windows+R to open the “Run” box, type “shell:startup,” and then press Enter.
