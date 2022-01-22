# Sanakirju Simplifier

Simplify [Sanakirju](https://github.com/stscoundrel/sanakirju) XML dataset for easier parsing.

### Usage

`pipenv install`
`pipenv run python main.py`

Will generate simplified XML dataset in `src/sanakirju_simplifier/build`

### Motivation

The original dataset Sanakirju uses is huge and deeply nested set of XML. Automatically parsing it using common Node.js libraries causes some incorrectly parsed data. One example of these parsing issues would be additional XML-element inside XML-text content. Most parsers pop the element out as its own element, which makes it quite tricky to place its text content back in correct location.

Sanakirju does not really need most of that XML-data; it only needs the text elements inside them. 

### What the simplifier does.

Most of the problematic tags can just be search/replaced with regex. This simplifier just goes through the whole dataset, and resaves them as new XML-files that have fewer and less-deeply nested elements. In short, the endgoal is to find, replace and remove content that would be incorrectly parsed, while keeping text content inside them.

### Sources.

Words & translations are from [Karjalan Kielen Sanakirja](http://kaino.kotus.fi/cgi-bin/kks/kks_etusivu.cgi) created by [Institute for the Languages of Finland](https://www.kotus.fi/en). The original material is licenced under [Creative Commons International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
