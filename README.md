# Rofi-Beats
A rofi-like menu for playing lofi radio stations on MacOS.

![demo.png](demo.png)

## Dependencies
- choose-gui (rofi/dmenu style menu for MacOS)
- mpv
- terminal-notifier

## Installation

Download the dependencies with Homebrew.

If you don't have Homebrew installed, it can quickly be set up by running the following command in your terminal:

```
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Once homebrew is installed you can add the relevant packages:

```
$ brew install choose-gui mpv terminal-notifier
```

Now clone this repository and give the script executable permissions:

```
$ git clone https://github.com/Carbon-Bl4ck/Rofi-Beats
$ cd Rofi-Beats
$ chmod +x rofi-beats
```
Now the script is ready to use!

```
./rofi-beats
```

## Linux 🐧

The linux version of this script is pretty much identical, replacing `terminal-notifier` with `notify-send`, and `choose-gui` with the aponymous `rofi`

To install `notify-send` and `rofi` enter the following:

For Ubuntu:
```
$ sudo apt install rofi notify-osd mpv
```
For Arch Linux:

```
sudo pacman -S rofi notify-osd mpv
```

Per the MacOS install clone this repository:

```
$ git clone https://github.com/Carbon-Bl4ck/Rofi-Beats
$ cd Rofi-Beats
```
Now remove the `rofi-beats` script and rename `rofi-beats-linux`:

```
$ rm rofi-beats
$ mv rofi-beats-linux rofi-beats
$ chmod +x rofi-beats
```

Now test out the script:
```
$ ./rofi-beats
```
## Usage

The script toggles the radio on and off depending on it's current state.

The script first checks to see if an instance of the radio is already playing.

If it finds the script is already playing music it kills the music. If the radio is not already playing it will launch the list of stations you can choose from.

### `mpv` arguments

You can add options in the `ARGS` variable in the script to specify those options for running mpv. The default of `--volume=60` is already added.

## Extra Tips 📝

- I'd highly recommend linking this script to a keybinding, using a tool such as [skhd](https://github.com/koekeishiya/skhd) or [sxhkd](https://github.com/baskerville/sxhkd) on linux.
- The menu highlight color can be customized by changing the hex value in the `choose` command preceded by the -b argument (default is set to 'ff79c6').
- The menu width can be changed my modifying the value after the -w tag of the `choose` command.
- `terminal-notifier` may need to be given permission to use notifications
