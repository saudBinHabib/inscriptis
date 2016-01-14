# inscriptis

A python based HTML to text converter based on SpiffWikiMarkup by Samuel Abel.

# Usage

```python
# Jusage examples
# Beautifulsoup4 must be installed since it is used to clean up the html befor processing

# The module can be used as follows:
from inscriptisn import get_cleartext

# single url
# The "http://" prefix must be also entered since urllib will not
url = "http://www.informationscience.ch"
clear_text = get_cleartext(url)
print(clear_text)

# for multiple urls use a list and loop through them.
# A automatic recognision if its a single url or multiple urls is not implemented yet
urls = ["http://www.informationscience.ch", "http://www.informationswissenschaft.ch"]
clear_texts = []

clear_texts.append(get_cleartext(url) for url in urls)

print(clear_texts)

# To get the runtime of the script you can call the module with "get_runtime=True"
url = "http://www.informationscience.ch"
clear_text, runtime = get_cleartext(url, get_runtime=True)
print("It took {} seconds to convert the html to cleartext\n".format(runtime))
print(clear_text)
```
