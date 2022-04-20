# python-morse-code-encoder
A morse code encoder written in Python.

For the record, this program outputs morse code in a goofy way:

    1.0.1.0...1.1.0.1.

Here's how you can read this:
* "1" is a − (dash).
* "0" is a · (dot).
* "." is a break.

When transmitting or playing morse, a break is a silence that is x miliseconds long (x being whatever your settings determine). A dot would be a sound for x miliseconds, and a dash is a sound for 3x miliseconds (three times x). Here, dashes are just notated as a '1' instead of three dots in a row. Breaks do not work this way, and breaks between signals, letters and words all use the same break character.
