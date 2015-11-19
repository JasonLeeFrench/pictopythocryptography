pictopythocryptography ❤️❤️❤️
======================

a python script for turning classic works of literature to emojis (?!?!?), inspired by [this WSJ article](http://blogs.wsj.com/japanrealtime/2015/11/19/meet-the-author-who-translates-classic-literature-into-emoji/).

Why worry about typing out all those emoji when we can get a computer to do it for us? 😊

For example:

>> It was the best of times, it was the worst of times...

... becomes...

>> 🍦🌲 💧🍎🐍 🌲🎩🐘 🎱🐘🐍🌲 🏢🐸 🌲🍦🐵🐘🐍, 🍦🌲 💧🍎🐍 🌲🎩🐘 💧🏢🏃🐍🌲 🏢🐸 🌲🍦🐵🐘🐍...


Install
-------

```
  git clone https://github.com/JasonLeeFrench/pictopythocryptography
  cd ./pictopythocryptography
  [sudo] python setup.py install
```

Usage
-----

``
pictopythocryptography [input] [emoji] [output]
``

where:

* input is your input text (defaults to input.txt)
* emoji is a text file containing emojis seperated by line breaks, corresponding to each letter you want replaced (defaults to emoji.txt)
* output is the text file to write to (defaults to output.txt)
