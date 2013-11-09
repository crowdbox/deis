# Crowdbox

Crowdbox is a hosting platform in the style of Heroku. The difference being that each app is funded
by donations in the style of Wikipedia.

The Crowdbox codebase is a fork of [Deis](http://deis.io/).

Here is an extract from [a blog post](http://tombh.co.uk/crowd-box-implementing-crowdfunded-paas/) I wrote outlining some of Crowdbox's main features:

The first and most significant feature is the fact that you can only deploy from a public Github repo. My reasoning is that this will promote a greater trust in the code that you are donating your money to. Imagine a Kickstarter-style page that had a description of the application, what its hosting costs are (eg; $100/month), its current received donation rate (eg; $120/month) and a link to the actual code that is running that application. You could click through, or clone the repo and scrutinise every single line of code yourself to make sure it isn't doing anything naughty, like secretly using spare CPU cycles to mine bitcoins!

Any spare money would always remain within Crowdbox's control, if unspent it would eventually be shared amongst all the other hosted apps on the system. In fact, Crowdbox users would never be allowed access to any of the money they've been donated. This way you can ensure that the money you donate is being used exactly for what you intended — hosting.

An interesting result of requiring Github code is that you could automatically deploy any public repo. For instance you could deploy Heroku's Node.js Hello World app, simply by replacing the 'github.com' domain with 'crowdbox.es'. Crowdbox would uniquely namespace the app to 'eiplab-heroku-node-helloworld.crowdbox.es' for your CNAMEing convenience and deploy. Magic.

But that raises two questions: 1) who becomes the admin (to do stuff like scale the number of dynos)? And 2) how can you deploy an app without donating any money? Crowdbox will federate its user authentication to Github's Oauth API, therefore the owner of the repo will be the default owner of the hosted app. If you want to become the owner, all you need do is fork the app and repeat the process with your new repo. I would like Crowdbox to have a free tier for low-traffic sites. I imagine there would be system whereby say, 5% of all donations are filtered into a central pool that funds a free tier and perhaps the general costs of maintaining the Crowdbox platform itself.

One problem I foresee is making databases transparent. I think it would be pretty off-putting if Crowdbox gave unrestricted read access to databases. Saying that, I would like to provide public access to all of an app's logs. The trouble is that databases will inevitably contain sensitive user data, albeit encrypted, but still it shoudn't be public. Not to mention that many databases allow you to store and run procs and functions — maybe you could write a bitcoin miner in Postgres procs!?

So that's the basic idea. I've already built a lot of it and I'm hoping to get a prototype working in the next few months. To start with it will have a 'push button' credit system to simulate payments, where anybody can push a button to donate credit to an app. I'll cover the hosting costs for a while, as long as they don't get too high!
