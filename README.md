# Crowdbox

Crowdbox is a Heroku-inspired hosting platform. The difference being that each app is funded
by donations in the style of Wikipedia. Because of its donation-based funding model only public
Github repositories can be hosted on it.

[Crowdbox Homepage](http://crowdbox.io)

Crowdbox is built on [Deis](http://deis.io/).

Getting Started
---------------

* Install the Crowdbox client using [pip](http://www.pip-installer.org/en/latest/installing.html):

```
$ pip install crowdbox
```

* Go to the local version of your Github repository:

```
$ cd <my-application-repo>
$ crowdbox create
Creating application... done, created opdemand-example--ruby--sinatra
```

* Use `crowdbox deploy` to deploy your application.
_NB. This step will eventually be added to a `git push` hook_

```
$ crowdbox deploy
From https://github.com/opdemand/example-ruby-sinatra
 * branch            master     -> FETCH_HEAD
Already up-to-date.
       Ruby app detected
-----> Compiling Ruby/Rack
-----> Using Ruby version: ruby-1.9.3
-----> Installing dependencies using Bundler version 1.3.2
       Running: bundle install --without development:test --path vendor/bundle --binstubs vendor/bundle/bin --deployment
       Using rack (1.5.2)
       Using rack-protection (1.5.0)
       Using tilt (1.3.6)
       Using sinatra (1.4.2)
       Using bundler (1.3.2)
       Your bundle is complete! It was installed into ./vendor/bundle
       Bundle completed (0.34s)
       Cleaning up the bundler cache.
-----> Discovering process types
       Procfile declares types -> web
       Default process types for Ruby -> rake, console, web

-----> Compiled slug size: 11.5 MB
       Launching... done, v4

-----> opdemand-example--ruby--sinatra deployed to Crowdbox
       http://opdemand-example--ruby--sinatra.crowdbox.es

-----> Donation page available at:
       http://crowdbox.io/app/opdemand-example--ruby--sinatra

       To learn more, use `deis help` or visit http://crowdbox.io

$ curl -s http://opdemand-example--ruby--sinatra.crowdbox.es
Powered by Deis!
```

License
-------

Copyright 2013, Crowdbox

Licensed under the Apache License, Version 2.0 (the 'License'); you may not
use this file except in compliance with the License. You may obtain a copy of
the License at http://www.apache.org/licenses/LICENSE-2.0.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations under
the License.
