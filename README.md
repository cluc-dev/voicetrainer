# Voicetrainer - a CircuitPython Hardware Project

This has been a WIP for a while but a Reddit post made me realize I'm not the only one thinking about these kinds of things. 

This is written in Python (circuitpython if we're being specific) running on a Circuitplayground Express (https://www.adafruit.com/product/3333). If you have written a bit of code before and want to start playing with hardware, this is a fantastic way to get started. More info on CircuitPython can be found here: https://learn.adafruit.com/adafruit-circuit-playground-express/what-is-circuitpython


If you ended up here have never written a single line of code in your life, this is (in my opinion) THE BEST way to get started. There's just something about making an LED physically light up that makes things click better than something on a screen. 

If you're coming from an arduino/esp33 background, circuitpython is basically just higher level bindings for c++, at the end of the day it's c++ getting executed, so porting ends up being easy of you end up with performance/cost constraints, but it's honestly really fast.

Any feedback on the code is much appreciated, of you don't have a board that can run circuitpython, just submit a pull request and I'll test it out!

I'd also love to get a few "standard" voice samples to be used to evaluate different versions of the pitch detection algorithm.

If you know Python, you already know CircuitPython. This may or may not be the final platform this would end up on, but it is SO FAST for getting up and running, and easily ported to Arduino/esp8266/32 when you're ready.


I doubt many people have my identical hardware, but I will happily test any PR's and share the results with you. I think I may get a few "standardized" voice samples to be used for testing so we can compare versions, so I would appreciate getting some of those in PR's as well. 



[
  ![Donate with PayPal]
  (https://raw.githubusercontent.com/stefan-niedermann/paypal-donate-button/master/paypal-donate-button.png)
]
(https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=JRP9H4WPMKJZY)
