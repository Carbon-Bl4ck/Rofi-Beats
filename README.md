# Rofi-Beats
A rofi-like menu for playing lofi radio stations on MacOS.

![demo.png](demo.png)

## Dependencies
- choose-gui (rofi/dmenu style menu for MacOS)
- mpv
- terminal-notifier

## Installation

Download the dependencies with Homebrew.

If you don't have Home brew installed, it can quickly be set up by running the following command in your terminal:

```
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Once homebrew is installed you can add the relevant packages:

```
$ brew install choose-gui mpv terminal-notifier
```

Now clone this repository and give the script executable permissions

```
$ git clone https://github.com/Carbon-Bl4ck/Rofi-Beats
$ cd Rofi-Beats
$ chmod +x rofi-beats
```
Now the script is ready to use! 

```
./rofi-beats
```

## Usage

The script toggles the radio on and off depending on it's current state. The script first checks to see if an instance of the radio is already playing. If it finds the script is already playing music it kills the music. If the radio is not already playing it will launch the list of stations you can choose from.

## Extra Tips 📝

I'd highly recommend linking this script to a keybinding, using a tool such as skhd: https://github.com/koekeishiya/skhd
