#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""regex cache"""

from __future__ import annotations

import re
import typing
from functools import lru_cache, wraps


class ReCache:
    """regex cache"""

    __slots__: typing.Tuple[str, str] = ("cache", "build_hooks")

    def __init__(self) -> None:
        self.cache: typing.Set[typing.Callable[[re.Pattern[str], str], str]] = set()
        self.build_hooks: typing.Set[typing.Callable[..., None]] = set()

    def add_build_hook(
        self, hook: typing.Callable[..., None]
    ) -> typing.Callable[..., None]:
        """add a build hook to compileall()"""

        self.build_hooks.add(hook)
        return hook

    def recache(
        self,
        pattern: str,
        flags: int = 0,
    ) -> typing.Callable[
        [typing.Callable[[re.Pattern[str], str], str]],
        typing.Callable[[str], str],
    ]:
        """add a function to regex cache"""

        def decorator(
            fn: typing.Callable[[re.Pattern[str], str], str]
        ) -> typing.Callable[[str], str]:
            fn._pat = pattern  # type: ignore
            fn._flags = flags  # type: ignore

            self.cache.add(fn)

            @wraps(fn)
            def wrapper(code: str) -> str:
                if fn._pat is pattern:  # type: ignore
                    fn._pat = re.compile(pattern, flags)  # type: ignore

                return fn(fn._pat, code)  # type: ignore

            return lru_cache()(wrapper)

        return decorator

    def compileall(self) -> None:
        """compile all regexes"""

        for hook in self.build_hooks:
            hook()

        for fn in self.cache:
            if isinstance(fn._pat, re.Pattern):  # type: ignore
                continue

            fn._pat = re.compile(fn._pat, fn._flags)  # type: ignore
