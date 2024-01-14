Discord Interactions API (Python wrapper)
========
A drop in library to provide requests and responses to the Discord Interactions API

### Why does this exist? Why not just use one of the other popular python discord libraries like discord.py?

For anyone except myself I would recommend you do so, however if you're still interested here are some reasons this exists.

1. I find all of the libraries to be too bloated and difficult to modify, due to being tightly coupled.

> This library defines abcs and allows anyone to use their own implementations inplace of the ones provided by the library

2. I don't have any interest in using the websocket library.

> Discord has made it quite clear over the years that they are only begrudingly supporting the websocket library and discourage its use.

3. Startup times are significant and make serverless infra more difficult

> This library does not load anything unless you ask it to, meaning you have more control over reducing cold startup times

4. This is an old library, made during the discord.py archival.

> I wanted a clean way to translate python code into the json schema, which wasn't available at the time.

5. I don't like typing shenanigans

> Annotations are core to this library. But it's the bare minimum required, I have no interest in having to learn TypeVars, etc.


## Installing

```
python3 -m pip install -U git+https://github.com/SilicalNZ/DiscordInterPythons
```

## Requirements
- Python 3.10
- asyncio
- aiohttp
- PyNaCl
