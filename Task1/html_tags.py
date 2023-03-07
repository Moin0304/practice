#Write a regular expression to find the html tags that are more than 4 letters.
#Note: Html tags can be found inside <> characters and closing html tags can be found in
#the same format after / character. </>
#i.e.: <param> </param>

import re

def find_htmltag_more_4_char(*tags):
    res = []
    for tag in tags:
        if re.search(r"^<[\w]{4,}></[\w]{4,}>$", tag):
            res.append(tag)
    return res

print(find_htmltag_more_4_char("<h1></h1>", "<div></div>","<head></head>","<body></body>",
"<param></param","<title></title>","<script></script>","<article></article>","<button></botton>",
"<input></input>","<style></style>"))