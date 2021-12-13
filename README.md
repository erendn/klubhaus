# Klubhaus
A Python chat application for peer-to-peer communication.

## Installation
### Clone the repository
```
git clone https://github.com/erendo/klubhaus.git
cd klubhaus
```

### Install dependencies
```
pip3 install -r requirements.txt
```

If PyAudio installation fails, you can download it from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) by downloading the WHL file corresponding your Python version and running the following command:
```
pip3 install <whl_file_name>.whl
```

### Run for ngrok
Since Klubhaus uses ngrok in the background, pyngrok needs to download and install it for you if you don't have it already. If you haven't used ngrok before, you will need to setup **authtoken**. You can find related instructions in ngrok's website.