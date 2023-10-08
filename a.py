#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""css"""

from warnings import filterwarnings as filter_warnings

from web_mini import html


def main() -> int:
    """entry / main function"""

    for _ in range(1):
        print(
            html.minify_html(
                r"""
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ari::web -&gt; Index</title>

    <meta name="description" content="hello" />
    <meta name="keywords" content="gay" />
    <meta
      name="robots"
      content="follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large"
    />
    <meta property="og:type" content="website" />

    <meta name="color-scheme" content="dark" />
    <meta name="theme-color" content="black" />

    <link rel="manifest" href="/manifest.json" />

    <script type="text/javascript">
    console.log(1);
    </script>

    <style type=text/css>
      /* CSS Styles */
      body {
        background-color: #f2f2f2;
        font-family: Arial, sans-serif;
      }
      h1 {
        color: blue;
        text-decoration: underline;
      }
      .container {
        width: 80%;
        margin: 0 auto;
        padding: 20px;
        background-color: white;
        border: 1px solid black;
        border-radius: 5px;
      }
    </style>
  </head>

  <body>
    <!-- hello world -->

    <h1>hi world how are you :3</h1>

    <br />

    <div class="container">
      <h1>Welcome to Example HTML File</h1>
      <p>This is a paragraph.</p>
      <ul>
        <li>Unordered list item 1</li>
        <li>Unordered list item 2</li>
      </ul>
      <ol>
        <li>Ordered list item 1</li>
        <li>Ordered list item 2</li>
      </ol>
      <a href="https://www.example.com">Link to Example Website</a>
      <img src="example.jpg" alt="Example Image" />
      <table>
        <tr>
          <th>Header 1</th>
          <th>Header 2</th>
        </tr>
        <tr>
          <td>Data 1</td>
          <td>Data 2</td>
        </tr>
      </table>
      <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required />
        <br />
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required />
        <br />
        <input type="submit" value="Submit" />
      </form>
    </div>

    <pre>
hello world
uwu
    </pre>
  </body>
</html>

<!-- hello world :3
how are you ? -->
"""
            )
        )

    return 0


if __name__ == "__main__":
    assert main.__annotations__.get("return") is int, "main() should return an integer"

    filter_warnings("error", category=Warning)
    raise SystemExit(main())
