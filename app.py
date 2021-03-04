#!/usr/bin/env python3

import logging
import socket
import random
from flask import Flask, request

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][%(levelname)-8.8s][%(name)s:%(lineno)d]-> %(message)s",
    handlers=[logging.StreamHandler()],
)

hostname = socket.gethostname()
colors = ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "purple", "red", "silver", "teal", "yellow"]
color = random.choice(colors)

html = """
<html>
<head lang="en">
    <meta charset="utf-8">
    <title></title>
    <style type="text/css">
    .main{{
        text-align: center;
        background-color: white;
        border-radius: 20px;
        margin: auto;
        position: absolute;
        font-size: 35;
        color: {};
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
    }}
    </style>

</head>
<body>
    <div class="main">hello from "{}"</br>client ip: "%s"</br>font color: "{}"</div>
</body>
</html>
""".format(color, hostname, color)

app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def func():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    logger.info("client ip: %s", ip)
    page = html % ip
    return page


if __name__ == "__main__":
    app.run("0.0.0.0", "8080")
