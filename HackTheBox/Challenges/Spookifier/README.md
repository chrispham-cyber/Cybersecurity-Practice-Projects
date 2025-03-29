### :dart: SOLUTION :dart:
Firstly, we try XSS to the search bar: `<script>alert(1)</script>
![](./img/1.png)

We can see that it responses. But XSS is used for manipulating the user experience, and there is no user here. So we should another payload (SSTI): `${{7*'7'}}`
![](./img/2.png)

We can see it returns `7777777`, so it is a `JINJA2` type, let try this: `${self.module.cache.util.os.popen('whoami').read()}`
![](./img/3.png)

We are `root` now, so let find the flag.
![](./img/4.png)
