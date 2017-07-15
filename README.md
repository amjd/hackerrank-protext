## Unobfuscation Challenge by HackerRank
HackerRank recently posted a challenge on Hackathon Hackers Facebook group. There's a web page which shows you a sample text and its obfuscated version. You need to figure out a way to get the plain text from the obfuscated text.

[Link to the challenge](http://protext.hackerrank.com/)

### Obfuscation app explained
The page uses a generated font called ProText. When a normal font is used to display obfuscated text, it is shown as is, but when ProText font is used, it shows the equivalent plaintext. The obfuscated text is just a bunch of random unicode characters shown using HTML entity codes. Looks simple enough, right? Did I mention the generated font changes every 5 seconds? :P

Apart from the default page, the app also supports taking a parameter to show obfuscated version of any text, like so:

`http://protext.herokuapp.com?text=Hello+World`

Needless to say, this is what I used in my solution.

### Solution
This is an extremely simple and lazy solution, and it probably doesn't even qualify. :P But here goes...

1. Get the obfuscated version for all possible characters (`abcdefghijklmnopqrstuvwxyz1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZ`)
2. Generate a mapping between the plaintext alphabet and its obfuscated version.
3. Get the obfuscated text and convert it to plaintext using the mapping.

Since the obfuscated code changes every 5 seconds, it's important that both the requests (to get the alphabet and the text) are completed in the span of the same 5 seconds, otherwise the alphabet and text may end up using different obfuscation code and fonts. To that end, I've used `requests.session()` ([see](http://docs.python-requests.org/en/master/user/advanced/#session-objects)), so that the two requests take advantage of HTTP persistent connection, reducing the time taken significantly.

In my testing, the above workaround led to near perfect results and I was able to get the obfuscated text about 90% of the time.

The script is written in Python 3, using standard packages. To execute, type:

`python3 protext.py`

### Contribute
If you have a better approach, feel free to send a pull request.
