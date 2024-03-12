
# (˶ᵔ ᵕ ᵔ˶) PwnPersonalities 

Give your Pwnagotchi new unique personalities! Customize voice.py and faces for a personalized touch. (Currently there is only Harold, but I plan on making more soon.)
## Installation

### 1. Download a personality
You can find screenshots and descriptions in each folder. If you only want to download a specific subfolder, [DownGit](https://minhaskamal.github.io/DownGit/) is helpful.

### 2. Copy files
Copy and overwrite your chosen `voice.py` to `/usr/local/lib/python3.7/dist-packages/pwnagotchi/` on your pwnagotchi.

I prefer to do this by using FileZilla, and FTPing in. [Tutorial on FTP by WiFiTube](https://www.youtube.com/watch?v=6f7PB3bgaxQ)

<img src="https://github.com/TheJustinCrow/PwnPersonalities/raw/main/media/CopyFiles.gif" width="700"/>


### 3. Edit faces and name in config.toml
If you want custom faces to go with the personality, you need to edit the `config.toml` file in `/etc/pwnagotchi`.

While you're in your config.toml, you can change the main.name (first line of the file) to the character's name if you'd like to.

<img src="https://github.com/TheJustinCrow/PwnPersonalities/raw/main/media/CopyFaces.gif" width="500">



### 4. Reboot Pwnagotchi

Click Reboot at the bottom of your WebUI

or:

SSH into your pwnagotchi and run the command `sudo reboot now`

### 5. Enjoy!
I would advise against looking inside the `voice.py` file, I've tried to add lots of things for each character to say so it never gets boring.

## List of Personalities

| Name                                                                                     | Screenshot                                                                                                        | Description                                                                                                     | Creator |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------|
| [Harold](https://github.com/TheJustinCrow/PwnPersonalities/tree/main/Harold)             | ![Harold Screenshot](https://github.com/TheJustinCrow/PwnPersonalities/raw/main/media/Harold/HaroldMANU.png)      | (⌐■_■) Wise, laid-back, and a hint of sarcasm. Imagine a seasoned friend with a virtual twinkle in his eye. | [TheJustinCrow](https://github.com/thejustincrow) |
| [H4X0R](https://github.com/TheJustinCrow/PwnPersonalities/tree/main/H4X0R)               | ![H4X0R Screenshot](https://github.com/TheJustinCrow/PwnPersonalities/raw/main/media/H4X0R/H4X0R2.png)          | [⌐■∇■] 1t'z 3x4ct1y wh4t y0u th1nk! H4ck th3 w0rld!!! [1337](https://en.wikipedia.org/wiki/Leet)            | [TheJustinCrow](https://github.com/thejustincrow) |
| [TheLastUltron](https://github.com/TheJustinCrow/PwnPersonalities/tree/main/TheLastUltron) | [None yet]                                                                                                         | This is the last Ultron. It managed to escape to the net and got stuck in your pwnagotchi's AI. Ultron will 'try' to escape to other networks, but isn't very good at it. If Ultron comes across a peer, it will try to 'assimilate' it, but never seems to be successful. | [jonspraggins](https://github.com/jonspraggins) |
| [Default](https://github.com/TheJustinCrow/PwnPersonalities/tree/main/Default)           | ![Default Screenshot](https://github.com/TheJustinCrow/PwnPersonalities/raw/main/media/Default/Default.png)     | This is the default faceset and voice for your Pwnagotchi.                                                    |  |




## Contributions

### How to contribute:
1. Create a fork of this repository
2. Create your theme following the pattern of the ones already posted
3. Commit your changes in English
4. Include a brief summary of what was added
5. Submit your pull request
