import html
import re
import requests
import string

ALPHABET = "abcdefghijklmnopqrstuvwxyz1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_obfuscated_text(text):
	obfuscated_text_html = re.findall('<h1>(.*)</h1>', text)[0]
	return html.unescape(obfuscated_text_html)

with requests.session() as s:
	r1 = s.get("http://protext.herokuapp.com/?text=abcdefghijklmnopqrstuvwxyz1234567890%20ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	r2 = s.get("http://protext.herokuapp.com/")

	obfuscated_alphabet = get_obfuscated_text(r1.text)
	obfuscated_text = get_obfuscated_text(r2.text)

	translation_table = str.maketrans(obfuscated_alphabet, ALPHABET)
	print("Decoded text is:", obfuscated_text.translate(translation_table))