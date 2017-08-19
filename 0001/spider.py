#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Life's pathetic, have fun ♡~ Nasy.

Excited without bugs::

    O._.O
    ((=)) +1s

* author: Nasy
* date: Aug 19, 2017
* email: sy_n@me.com
* file: spider.py
* license: MIT

This one is used to crawl the table on this page::
    http://py4e-data.dr-chuck.net/comments_42.html

Just a simple example.

Copyright © 2017 by Nasy. All Rights Reserved.
"""
import requests as req
import bs4

# THEURL = input("Enter:\n> ")
THEURL = "http://py4e-data.dr-chuck.net/comments_42.html"


def main() -> None:
    """Do main function."""
    # Get the website
    html = req.get(THEURL)
    content = bs4.BeautifulSoup(html.content, "html.parser")  # or lxml

    # Get tr
    trs = content.select("tr")
    for tag_tr in trs:
        # Get td
        tag_td = tag_tr.select("td")
        name, comment = tag_td[0], tag_td[1]
        print("name:", name.text, "comment:", comment.text)


if __name__ == "__main__":
    main()
