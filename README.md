Internet Defense League Anti-Censorship Mirror (Python app)
===========================================================

This project contains a simple Python Flask app to run an
[Anti-Censorship Network Mirror][1]. Run this app on your server and make the
Anti-Censorship Network stronger. Together we can beat government censorship
forever! The project is set up to be extremely easy to deploy to Heroku, but you
can run it on any Python server.

### How to set up:

1. **[Sign up for an API Key][1]**
2. Deploy the app to Heroku (or your own server)

   If you deploy to your own server, please run the `make` command to grab the
   [MaxMind GeoLite2 geolocation database][2].

3. Configure your environment variables with the following definitions:

   ```
   API_KEY=[your API key]

   DOMAIN=[Full URL to your installation of the Mirror, no trailing slash]

   SECRET_KEY=[A random string, used by Flask]
   ```

   For example, if you're running the app at https://my-mirror.herokuapp.com,
   you could configure your environment variables using the following commands:

   ```
   heroku config:set API_KEY=foo

   heroku config:set DOMAIN=https://my-mirror.herokuapp.com

   heroku config:set SECRET_KEY=bar
   ```
4. Restart server if needed. You're done!

### How to test:

Simply visit the URL for your server in a browser
(eg. https://anticensorship-mirror.herokuapp.com ). If everything is working,
you should see a weird looking binary response like this:

```
W6¼Bv¯zo{`¼8>¿Zcü]Má¥w01»ÜìØñ¤EoýØ³õLo©ãë^æóíÛ¼ë5"gQË|9Ü`YK;g=YÖ?éïË.ëãüEÙZaÔúå<"]ú¶! û¶w¬¥ÊômxÈÛý·X*ÝAä%? Ö?ÖßuiùÒ&'ñnaÛâÈìZ>vÏ¨ áUGØÛ2É÷nád¹/ÁËÌôtJ®ç÷ JÍÂm"NîÀ*Z(ø¨1¡b/ð<Ð®FF_V/lÒLò0j9Ó:X83RPÐêÃØå£Ù
```

This is the encrypted data that allows sites that embed the ACN JavaScript
code to communicate with the Network's central server. Essentially your Mirror
is a proxy server, and because the data is RSA-encrypted and digitally signed,
it's impossible to tamper with mid-stream. This protects the data against
government censors and malicious Mirror servers.

You can see that the response changes if you pass the parameter
`?_ac_force_locale=CN`.

### More information

There are tons of other ways to get involved with the Anti-Censorship Network.
To learn more, visit https://www.internetdefenseleague.org/censorship/

[1]: https://www.internetdefenseleague.org/censorship/mirror
[2]: http://dev.maxmind.com/geoip/geoip2/geolite2/