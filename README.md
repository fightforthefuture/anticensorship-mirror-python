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
4. Drink a beer (or a non-alcoholic beverage), you're done.

### More information

There are tons of other ways to get involved with the Anti-Censorship Network.
To learn more, visit https://www.internetdefenseleague.org/censorship/

[1]: https://www.internetdefenseleague.org/censorship/mirror
[2]: http://dev.maxmind.com/geoip/geoip2/geolite2/