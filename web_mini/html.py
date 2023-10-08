#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""minify html"""

import re
from functools import lru_cache
from typing import Dict, List

from . import const, recache

html_fns: recache.ReCache = recache.ReCache()

TAG_REGEX: re.Pattern[str] = re.compile(r"<\w.*?>", re.I | re.MULTILINE | re.DOTALL)
TAG_PATTERNS: Dict[re.Pattern[str], str] = {}
SPACE_PATTERNS: List[re.Pattern[str]] = []


@html_fns.add_build_hook
def compile_tag_patterns() -> None:
    """compile TAG_PATTERNS"""

    if not TAG_PATTERNS:
        TAG_PATTERNS.update(
            {
                re.compile(r"<\s*pre.*>", re.I): "pre",
                re.compile(r"<\s*textarea.*>", re.I): "txt",
                re.compile(r"<\s*/\s*pre\s*>", re.I): "/pre",
                re.compile(r"<\s*/\s*textarea\s*>", re.I): "/txt",
            }
        )


@html_fns.add_build_hook
def compile_space_patterns() -> None:
    """compile SPACE_PATTERNS"""

    if not SPACE_PATTERNS:
        SPACE_PATTERNS.extend(
            [
                re.compile(r" \s+|\s +", re.MULTILINE),
                re.compile(r"\w\s+\w", re.MULTILINE),
                re.compile(r'"\s+>', re.MULTILINE),
                re.compile(r"'\s+>", re.MULTILINE),
                re.compile(
                    r"\"\s\s+\w+=\"|'\s\s+\w+='|\"\s\s+\w+=|'\s\s+\w+=",
                    re.MULTILINE,
                ),
                re.compile(r"\d\s+>", re.MULTILINE),
            ]
        )


@lru_cache
def rawtag(tag: str) -> str:
    """return raw tag"""

    compile_tag_patterns()

    for pattern, tag_name in TAG_PATTERNS.items():
        if pattern.match(tag):
            return tag_name

    return "/span" if "/" in tag else "span"


@html_fns.recache(r"<!--.*?-->", re.S)
def html_remove_comments(pat: re.Pattern[str], html: str) -> str:
    """remove html comments"""
    return pat.sub("", html)


def html_remove_style_type(html: str) -> str:
    """remove html <style> type"""
    return (
        html.replace('<style type="text/css">', "<style>")
        .replace("<style type='text/css'>", "<style>")
        .replace("<style type=text/css>", "<style>")
    )


def html_remove_script_type(html: str) -> str:
    """remove html <script> type"""
    return (
        html.replace('<script type="text/javascript">', "<script>")
        .replace("<script type='text/javascript'>", "<script>")
        .replace("<script type=text/javascript>", "<script>")
    )


def html_remove_unneeded_tags(html: str) -> str:
    """remove html <script> type"""

    for tag in const.UNNEEDED_HTML_TAGS:
        html = html.replace(tag, "")

    return html


@html_fns.recache(
    "(<\\s*pre.*>|<\\s*/\\s*pre\\s*>|<\\s*textarea.*>|<\\s*/\\s*textarea\\s*>)", re.I
)
def html_remove_whitespace(pat: re.Pattern[str], html: str) -> str:
    """remove useless html whitespace ( does not minify textarea and pre tags )"""

    tags: List[str] = []
    split: List[str] = pat.split(html)

    for idx, stag in enumerate(split):
        # if we in a tag

        if (idx + 1) % 2 == 0:
            tag: str = rawtag(stag)

            if tag.startswith("/"):
                if not tags or "/" + tags.pop() != tag:
                    raise SyntaxError(
                        f"tag {idx} ( {stag}, got {tag} ) is not closed properly"
                    )
            else:
                tags.append(tag)

            continue

        if not tags:
            temp = re.sub(r">\s+<", "> <", stag)
            split[idx] = re.sub(r"\s{2,}|[\r\n]", " ", temp)

    return "".join(split)


@html_fns.recache(r'([a-zA-Z]+)="([a-zA-Z0-9-_\.]+)"')
def html_unquote_attrs(pat: re.Pattern[str], html: str) -> str:
    """remove all html quotes on attibutes if possible"""

    compile_space_patterns()

    # iterate on a for loop cleaning stuff up on the html markup

    tag: str

    for tag in TAG_REGEX.findall(html):
        # exceptions of comments and closing tags

        if tag.startswith("<!") or tag.find("</") > -1:
            continue

        original: str = tag

        # remove white space inside the tag itself

        tag = SPACE_PATTERNS[2].sub('" >', tag)  # preserve 1 white space is safer
        tag = SPACE_PATTERNS[3].sub("' >", tag)

        for each in SPACE_PATTERNS[1].findall(tag) + SPACE_PATTERNS[5].findall(tag):
            tag = tag.replace(each, SPACE_PATTERNS[0].sub(" ", each))

        for each in SPACE_PATTERNS[4].findall(tag):
            tag = tag.replace(each, each[0] + " " + each[1:].lstrip())

        # remove quotes on some attributes

        tag = pat.sub(r"\1=\2", tag)

        if original != tag:  # has the tag been unquoted
            html = html.replace(original, tag)

    return html.strip()


def minify_html(html: str) -> str:
    """run all html stages"""

    html_fns.compileall()

    html = html_remove_comments(html)
    html = html_remove_style_type(html)
    html = html_remove_script_type(html)
    html = html_remove_unneeded_tags(html)
    html = html_remove_whitespace(html)
    html = html_unquote_attrs(html)

    return html
