# MGCTool
A python tool for encoding and decoding messages using the Mendicino Grid Cipher with support for keys.

## What is the Mendicino Grid Cipher?
- The Mendicino Grid Cipher is a grid-based cipher that encodes by finding each plaintext letter in a 5x5 grid and returning one of the letters adjacent to it in as determined by an incrementing compass rose. The grid can be set up using a key word or phrase for greater cipher strength and must omit one letter (Q by default). The compass rose may be reset after every word or let to run continuously.

## Getting Started
- Simply download and run the python script. It will ask you for all the information needed successfully encode or decode a message.

## Limitations
- Special characters and numbers can only be passed through to the ciphertext or omitted, not encoded
- There is currently no good way to encode or decode **.txt** or **.json** files, everything must be typed or pasted into the program
- All arguments must be entered into the program every time it is run
