# ip-display

## Manipulating the LCD connected to my raspberry pi

<p align="center">
  <img src="mascot.gif" alt="Mascot" height="250px">
</p>

 ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)
 ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
 ![Neovim](https://img.shields.io/badge/NeoVim-%2357A143.svg?&style=for-the-badge&logo=neovim&logoColor=white) 
 [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 

💻 *Embedded system are the future*

---

## 📜 Description

Displaying important info on the LCD ...

---

## Requirements

<li> Tested on a raspberry pi 4</li>
<li> Install i2c-tools </li>
<li> Install python-smbus </li>
<li> Activate i2c support with raspi-config </li> 


## ⚙️ Installation

First Clone the repository:

```bash
$ git clone https://github.com/skillz4real/ip-display
$ cd ip-display
```

I keep all my python projects in virtual env so:
```bash
$ python -m venv .
$ source bin/activate
```

Install the dependencies:

```bash
$ pip install -r requirements.txt
```

Try running the different scripts and see output:
```bash
$ python3 main.py
```

Can also add commands to crontab. 

## 🌟 Features

- Displaying the raspberry pi 4 local ip address for easy sshing
- Displays the external ip
- Controllable through a button
- Displays motivational reminders
  
---

## 📚 Educational Resources

I am not an expert, I am still learning, here are the resources I use and my profiles:

<!--- [Hack The Box](https://app.hackthebox.com/profile/1776662)-->
<!--- [Try Hack Me](https://tryhackme.com/p/skillz4real)-->
<!--- [Leet Code](https://leetcode.com/skillz4real/)-->

---

## 👨‍💻 Youtube

<!-- Youtube -->

---

## 📄 License

ip-display is released under the [GNU LICENSE](LICENSE).

---

## 📞 Support

For support, feature requests, or bug reports, please file an issue in the [GitHub issue tracker](https://github.com/skillz4real/sh-scripts/issues).

---

