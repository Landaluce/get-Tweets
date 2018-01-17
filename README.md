# get-Tweets

# Summary

# Dependencies
Required Python 3 packagews: pip and Tweepy


# Installation
### 1. Installing Python and Anaconda
If you do not already have Python v3.6 installed on your computer, we recommend installing it through the free Anaconda distribution:

1.1 Visit Anaconda's downloads page: https://continuum.io/downloads. Locate the symbol corresponding to your operating system on the screen and click it.

1.2 Download the Python 3.6 version 64-Bit (x86) Installer by clicking on the green Download button.

1.3 Follow the instructions corresponding to your oprating system:
  
  **Linux instructons**: After locating the install script (e.g., in Downloads/ by typing ```cd Downloads``` in a terminal), run the (bash) shell installer by typing the following into your terminal:'''bash Anaconda3-5.0.1-Linux-x86_64.sh'''
  
**Note:** A newer version of Anaconda may have a new version number; check your exact filename.

You should now verify that we have installed it correctly. To do this, follow the instructions below:

Open an new terminal window. This is important to ensure that your $PATH includes Anaconda.
Type: ```python -V``` (capital v) and hit the ```Enter``` key.


You should see a response that looks like: ```Python 3.6.0 :: Anaconda 5.0.1 (64-bit)```. If you do not see ```:: Anaconda 5.0.1``` then you did not open a new terminal window or you did not update your PATH variable during the Anaconda installation. We recommend that you uninstall Anaconda and try to install it again, following the instructions above. To uninstall Anaconda, type ```rm -rf ~/anaconda3```, replacing anaconda3 with the name of the Anaconda directory, if it is different. Hit the ```Enter``` key.


  **MacOS instructons**: Double-click the installer application icon (it will be called something like Anaconda3-5.0.1-MacOSX-x86_64.pkg) and follow the instructions on the screen.
  
You should now verify that we have installed it correctly. To do this, Open a terminal window. If you are unfamiliar with how to access a terminal window, search for “terminal” in Spotlight. You should see a window appear with a command-line prompt. Type ```python -V``` (capital v) and hit the ```Enter``` key.


You should see a response that looks like: ```Python 3.6.0 :: Anaconda 5.0.1 (64-bit)```. If you do not see ```:: Anaconda 5.0.1``` then your PATH variable was not updated during the Anaconda installation. We recommend that you uninstall Anaconda and try to install it again, following the instructions above. To uninstall Anaconda, type ```rm -rf ~/anaconda3```, replacing anaconda3 with the name of the Anaconda directory, if it is different. Hit the ```Enter``` key.
  
   **Windows instructons**:Double-click the installer application icon (it will be called something like Anaconda3-5.0.1-Windows-x86_64.exe) and follow the instructions on the screen.

**Note:** The installation location is not important; however, make sure that you check the option to Add Anaconda to my PATH environment variable (make sure both boxes are checked). This will ensure that Windows knows that you want to use the Anaconda distribution of Python when you launch Lexos. This is especially important if you already have a different version of Python installed.

When the process is complete, select Finish to finish the installation of Anaconda.

You should now verify that we have installed it correctly. To do this, Open a Windows Command Prompt. If you are unfamiliar with how to access the Command Prompt, hit [WindowsKey] + [R] to bring up the Run box and type ```cmd.exe``` into the text field. Then hit the ```Enter``` key. A black Command Prompt window should appear. Type ```python -V``` (capital v) and hit the ```Enter``` key.

You should see a response that looks like: ```Python 3.6.0 :: Anaconda 5.0.1 (64-bit)```. If you do not see ```:: Anaconda 5.0.1``` then your PATH variable was not updated during the Anaconda installation. We recommend that you uninstall Anaconda and try to install it again, following the instructions above. To uninstall Anaconda, go to your computer's Control Panel, choose ```Add or Remove Programs``` or ```Uninstall a program``` and then select ```Python 3.6 (Anaconda)```.
    
### 2. Installing Additional Python Packages

   2.1 Begin my making sure that your package installer (pip) is up to date. In your terminal type ```pip install -U pip``` (capital u) and hit the ```Enter``` key. Your terminal window will display some information showing you the update process. Once that is completed, you can now use 'pip' (python package installer) in the next step.
   
   2.2 In your terminal type ```pip install tweepy``` and hit the ```Enter``` key.

### 3. Downloading and Extracting get-Tweets

3.1 Download get-Tweets: Got to https://github.com/Landaluce/get-Tweets, click on the green ```clone or download``` button, and cick on ```Download ZIP```.

3.2 Once the get-Tweets zip archive has downloaded, right-click on the zip icon (in your Downloads), and select Extract. Choose where you would like to install get-Tweets and click Extract. If you wish, you may change the name of the extracted folder from get-Tweets-master to get-Tweets. In the instructions below, we will assume that you did this and that you extracted the get-Tweets folder to the Desktop.

### 4. Setting up Twitter's API credentials:
Follow the [twitter startup directions](twitter_startup_directions.pdf)

### 5. Starting and Launching get-Tweets
#### Important: Close your current terminal window and open a new one.

5.1 avigate to the get-Tweets folder by typing ```cd Desktop/get-Tweets``` and hit the ```Enter``` key.
    
5.2 Type ```python get-Tweets.py``` and hit the ```Enter``` key. 

You are all set. Now, you should see the following menu:

    1. Pull tweets from timeline
	  2. Search tweets
	  3. Exit
	  What would you like to do? 
    
**Quitting get-Tweets:** To quit get-Tweets, simply choose the the third option in the menu or cose the terminal.
