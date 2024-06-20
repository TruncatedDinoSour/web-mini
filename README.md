# This repository has been migrated to the self-hosted ari-web Forgejo instance: <https://git.ari.lt/ari/web-mini>
# web-mini

> web-mini -- efficient css and html minifer inspired by https://pypi.org/project/css-html-js-minify/

# examples

**note** `minify_html` does not handle `style` tags -- handle css minification
( only very basic stuff that works for html too ) inline urself

## singlethreaded

```py
import web_mini

print(
    web_mini.html.minify_html(
        r"""
<h1>hello world</h1>

<p>this is my very cool
website :)</p>

<pre>
int main(void) {
    return 0;
}
</pre>
"""
    )
)

print(
    web_mini.css.minify_css(
        r"""
body {
    margin: auto;
    padding: 2rem;
    max-width: 1100px;
    min-height: 100vh;
    text-rendering: optimizeSpeed;
}

li {
    margin: 0.5em;
}

code {
    white-space: pre-wrap !important;
}

@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        -webkit-animation-duration: 0.01ms !important;
        animation-duration: 0.01ms !important;

        -webkit-animation-iteration-count: 1 !important;
        animation-iteration-count: 1 !important;

        -webkit-transition-duration: 0.01ms !important;
        -o-transition-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;

        scroll-behavior: auto !important;;
    }
}
"""
    )
)
```

outputs :

```
<h1>hello world</h1> <p>this is my very cool website :)</p> <pre>
int main(void) {
    return 0;
}
</pre>
body{margin:auto;padding:2rem;max-width:1100px;min-height:100vh;text-rendering:optimizeSpeed}li{margin:.5em}code{white-space:pre-wrap !important}@media (prefers-reduced-motion:reduce){*,*::before,*::after{-webkit-animation-duration:.01ms !important;animation-duration:.01ms !important;-webkit-animation-iteration-count:1 !important;animation-iteration-count:1 !important;-webkit-transition-duration:.01ms !important;-o-transition-duration:.01ms !important;transition-duration:.01ms !important;scroll-behavior:auto !important;}}
```

## usage with threading

if ur using web-mini with threading make sure to call `compileall()` so caching doesnt get in the way

```py
import web_mini

web_mini.compileall()

# or :
# web_mini.css.css_fns.compileall()
# web_mini.html.html_fns.compileall()
```
