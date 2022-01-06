[![Github](https://img.shields.io/github/license/hansatcode/HCSAuto?style=flat-square)](https://github.com/HanSatCode/HCSAuto/blob/main/LICENSE)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FHanSatCode%2FHCSAuto&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=true)](https://hits.seeyoufarm.com)


## Intro
```
This program will be stop from updating after February 1, 2022.
After this time, we cannot guarantee that the program will work normally for the target.
```
HCSAuto is a program that automatically diagnoses various people with background work in a Windows environment.<br/>
This program is based on Selenium and ChromeDriver.

## Caution
```
Please use it while following the quarantine rules for each city and province.
If you have any abnormal symptoms, you can stop using it and change it directly by accessing the app or website.
The user himself is responsible for the damage that occurs after use.
```
## Setup
Prior to use, [Chrome for desktop](https://www.google.com/intl/ko/chrome/) and [ChromeDriver](https://chromedriver.chromium.org/home) are required.
```
1. Run and install the Chrome installer for desktop.
2. Check the current version of Chrome for desktop by entering 'chrome://version/' in the address bar.
3. Download the ChromeDriver for the Chrome version for the desktop.
4. Insert the downloaded file into the 'src' folder of the package.
```
For Python releases, [Python3](https://www.python.org/) and Selenium are required.
```
1. Download and install the 'Python3.x.x' installer.
2. Open the 'command prompt (cmd)' to enter "pip3 install Selenium" and wait for the installation to complete.
```
## Using
This program supports Windows Alert or Discord Alert.<br/>
In the case of Windows Alert, it does not display an alert if it ends normally.
```
1. Edit "Data.csv" and enter it in the order of [school name, work target name, date of birth, 6 digits of password].
   If there are more than two people to work on, enter new data through line change.
2. Select and run the platform you want to receive an alert on.
```
## Tip
If you want to completely turn off the console of 'ChromeDriver', you can do the following.
```
1. Find the path "(Python installation path)\Python38-32\Lib\site-packages\selenium\webdriver\common" and open the folder.
2. Modify the 'service.py' file, add and save 'creationflags=0x080000' as the last factor of the 'subprocess.Popen' function.
```
```python
self.process = subprocess.Popen(cmd, env=self.env,
                                close_fds=platform.system() != 'Windows',
                                stdout=self.log_file,
                                stderr=self.log_file,
                                stdin=PIPE,
                                creationflags=0x08000000)
```
