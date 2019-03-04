import evdev
from evdev import InputDevice, categorize  # import * is evil :)
dev = InputDevice('/dev/input/event4')

# If you set debug to True, you will get a response on every keystroke
debug=False
# If set to True, it will convert the output-string to lower-case. Otherwise it will be all in UPPERCASE
lowercase=True
# If set to True, the script will not print any non-symbol characters and ignore any unknown keys
printable_only=True



output_string=""

if (not printable_only):
# Original from stack-exchange post
# Provided as an example taken from my own keyboard attached to a Centos 6 box:
  scancodes = {
    # Scancode: ASCIICode
    0: None, 1: u'ESC', 2: u'1', 3: u'2', 4: u'3', 5: u'4', 6: u'5', 7: u'6', 8: u'7', 9: u'8',
    10: u'9', 11: u'0', 12: u'-', 13: u'=', 14: u'BKSP', 15: u'TAB', 16: u'Q', 17: u'W', 18: u'E', 19: u'R',
    20: u'T', 21: u'Y', 22: u'U', 23: u'I', 24: u'O', 25: u'P', 26: u'[', 27: u']', 28: u'CRLF', 29: u'LCTRL',
    30: u'A', 31: u'S', 32: u'D', 33: u'F', 34: u'G', 35: u'H', 36: u'J', 37: u'K', 38: u'L', 39: u';',
    40: u'"', 41: u'`', 42: u'LSHFT', 43: u'\\', 44: u'Z', 45: u'X', 46: u'C', 47: u'V', 48: u'B', 49: u'N',
    50: u'M', 51: u',', 52: u'.', 53: u'/', 54: u'RSHFT', 56: u'LALT', 100: u'RALT'
  }
else:
  # Version with only printable keys/characters AND 'CRLF'
  scancodes = {
    # Scancode: ASCIICode
    0: None, 1: u'', 2: u'1', 3: u'2', 4: u'3', 5: u'4', 6: u'5', 7: u'6', 8: u'7', 9: u'8',
    10: u'9', 11: u'0', 12: u'-', 13: u'=', 14: u'', 15: u'', 16: u'Q', 17: u'W', 18: u'E', 19: u'R',
    20: u'T', 21: u'Y', 22: u'U', 23: u'I', 24: u'O', 25: u'P', 26: u'[', 27: u']', 28: u'CRLF', 29: u'',
    30: u'A', 31: u'S', 32: u'D', 33: u'F', 34: u'G', 35: u'H', 36: u'J', 37: u'K', 38: u'L', 39: u';',
    40: u'"', 41: u'`', 42: u'', 43: u'\\', 44: u'Z', 45: u'X', 46: u'C', 47: u'V', 48: u'B', 49: u'N',
    50: u'M', 51: u',', 52: u'.', 53: u'/', 54: u'', 56: u'', 100: u''
  }
 
for event in dev.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        data = evdev.categorize(event)  # Save the event temporarily to introspect it
        if data.keystate == 1:  # Down events only
            # If we specified we want 'printable only', we also ignore any unknown key-events like multimedia keys
            if (printable_only):
                key_lookup = scancodes.get(data.scancode) or u''
            else:
                key_lookup = scancodes.get(data.scancode) or u'UNKNOWN:{}'.format(data.scancode)  # Lookup or return UNKNOWN:XX
            if (debug):
                print ('You Pressed the %s key!' % key_lookup)  # Print it all out!
            if (key_lookup == "CRLF"):
                # This is the point where we have the input'ed line in 'output_string', in all CAPS.
                # If you want to do anything else than printing it, you would put that code here.
                # We, however, just print
                if(lowercase):
                    print(output_string.lower())
                else:
                    print(output_string)
                output_string=""
            else:
                output_string=("%s%s"% (output_string,key_lookup))


            
