# Does iOS have sideloading yet?

https://doesioshavesideloadingyet.com/

A resource to track the status of sideloading on iOS.

---

Build requirements:

* Linux or macOS
* `pandoc` 3.6.3
* Python 3

Setup build environment:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Build:

```
./build.sh -W
```

Development server (requires `darkhttpd`):

```
# terminal 1
./serve.sh

# terminal 2
./build.sh
```
