# Voicetrainer - a CircuitPython Hardware Project

The basic idea of this project is a device you could wear (ideally around your neck like a choker) that would vibrate to alert you when the pitch of your voice drops below a desired threshold frequency. 

This has been a WIP for a while but a Reddit post made me realize I'm not the only one thinking about these kinds of things. 

This is written in Python (circuitpython if we're being specific) running on a Circuitplayground Express (https://www.adafruit.com/product/3333). If you have written a bit of code before and want to start playing with hardware, this is a fantastic way to get started. More info on CircuitPython can be found here: https://learn.adafruit.com/adafruit-circuit-playground-express/what-is-circuitpython


# Demo Video / Reddit Thread
https://www.reddit.com/b3654c9a-f64d-494a-a256-63bb4adf8593

If you ended up here have never written a single line of code in your life, this is (in my opinion) THE BEST way to get started. There's just something about making an LED physically light up that makes things click better than something on a screen. 

If you're coming from an arduino/esp33 background, circuitpython is basically just higher level bindings for c++, at the end of the day it's C++ getting executed, so porting ends up being easy of you end up with performance/cost constraints, but it's honestly really fast.

Any feedback on the code is much appreciated, of you don't have a board that can run circuitpython, just submit a pull request and I'll test it out!

I'd also love to get a few "standard" voice samples to be used to evaluate different versions of the pitch detection algorithm.

If you know Python, you already know CircuitPython. This may or may not be the final platform this would end up on, but it is SO FAST for getting up and running, and easily ported to Arduino/esp8266/32 when you're ready.


I doubt many people have my identical hardware, but I will happily test any PR's and share the results with you. I think I may get a few "standardized" voice samples to be used for testing so we can compare versions, so I would appreciate getting some of those in PR's as well. 

#I want this! How can I help!

The primary thing lacking from this project, as always, is motivation. I would really love someone to come in here and make a Pull Request and solve all the problems. I hope it happens, but I'm not too optimistic about that. If anyone does submit a REALLY good PR, I'll GLADLY send you board with your PR running on it, 3D print a nice enclosure and stuff. That's the dream, but I'm fairly certain that I could pull this off alone, as I have completed two other embedded hardware projects that involved real time pitch detection that all ended up working well. Both included PCB design/fabrication and your usual supply chain nonsense...yuck. 

As always, your knowledge is much more valuable than your money. However, any financial support you can provide for development of open source software is greatly appreciated! I honestly highly anticipate this project being completed. It's already SO CLOSE, and even in its current expensive prototype state, the total hardware cost is under $30. For a finished product, the total BOM should be well under $40, depending on how we decide to make it wearable. As such, I will promise to send anyone that makes a generous contribution (>$40) either a late-stage prototype or an early-stage production model. It's not much, but it's still a better guarantee than Kickstarter! Any donations will obviously be shared with contributors!

<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=JRP9H4WPMKJZY">
  <img src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" alt="Donate with PayPal" />
</a>
