# Get this prices
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
</p>

A python script that requests prices from [Kabum](https://www.kabum.com.br/) and add it to a spreadsheet

***

## 🤔 How to use

Requirements:

-   [Python](https://www.python.org/)


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


After installing the dependencies, just double-click the [run.bat](/run.bat) and it will fill the [spreadsheet](/sheets.xlsx) (that is pre-organized to fill max 6 products from kabum).

---

## 👨‍💻 How to change the products


To change the products that will have the prices placed on the spreadsheet, just change the urls list in [functions.py](/functions.py). This url must be from [Kabum](https://www.kabum.com.br/).

```python

urls = ['insert.your.url.here', '...']

```

*⚠️ Kabum may change the urls if they were on sale, if "ERROR" appear instead of the price, you should look into the respective product url ⚠️*


---

## 🚀 How to make it initialize with your Windows


Create a shortcut to [run.bat](/run.bat) and put it to your Startup folder. To open your Startup folder just hit Windows+R to open the “Run” box, type “shell:startup,” and then press Enter.


---

## 😱 Pending issues

When running the program, the spreadsheet will be alerted with a "damaged file" error, however this error is caused by the use of the [openpyxl](https://openpyxl.readthedocs.io/en/stable/) library.

So when opening [sheets](/sheets.xlsx) you should press "Yes" when the error appears and then "Close". This problem, unfortunately 😔, should be recurrent (not to say 100% of the time that a change is made by the script).


---

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/abacaxiguy/get_this_prices/issues).

---

## 📋 Tested in

- Windows 10

***
<h4  align="center">Developed by 🍍</h4>