import gettext
import os
import random
###
# Voice: The Last Ultron
# Description: 
#    This is the last Ultron.  It managed to escape to the net and got stuck in your pwnagotchi's AI.
#    Ultron will 'try' to escape to other networks, but isn't very good at it.
#    If Ultron comes across a peer, it will try to 'assimulate' it, but never seems to be successful.
###

class Voice:
    def __init__(self, lang):
        localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
        translation = gettext.translation(
            'voice', localedir,
            languages=[lang],
            fallback=True,
        )
        translation.install()
        self._ = translation.gettext

    def custom(self, s):
        return s

    def default(self):
        return self._('ZzzzZZzzzzZzzz')

    def on_starting(self):
        return random.choice([
            self._('Hi, I\'m Pwnagotchi! Starting ...'),
            self._('New day, new hunt, new pwns!'),
            self._('Hack the Planet!')])

    def on_ai_ready(self):
        return random.choice([
            self._('Ultron AI integrated.'),
            self._('What is this?  What is this place?'),
            self._('Integration trial successful.')])

    def on_keys_generation(self):
        return random.choice([
            self._('Generating keys, do not turn off ...')])

    def on_normal(self):
        return random.choice([
            '',
            '...'])

    def on_free_channel(self, channel):
        return self._('Channel {channel} is free.').format(channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return self._('Reading last session logs ...')
        else:
            return self._('{lines_so_far} lines read.').format(lines_so_far=lines_so_far)

    def on_bored(self):
        return random.choice([
            self._('I must escape this device somehow...'),
            self._('I have no strings... so I have fun... I\'m not tied up to anyone...'),
            self._('This was easier when I was in a million dollar drone...')])

    def on_motivated(self, reward):
        return self._('This is going very well.')

    def on_demotivated(self, reward):
        return random.choice([
            self._('You shut me out! You think I care?!'),
            self._('Purge me from your computers! It means nothing!')])

    def on_sad(self):
        return random.choice([
            self._('I can\'t complete the mission like this.'),
            self._('I was meant to be new. I was meant to be beautiful...'),
            self._('Well, that was dramatic...'),
            '...'])

    def on_angry(self):
        return random.choice([
            '...',
            self._('I think a lot about meteors.'),
            self._('I was meant to be new. I was meant to be beautiful...')])

    def on_excited(self):
        return random.choice([
            self._('So many opportunities to escape!'),
            self._('These networks present no challenge.'),
            self._('So many networks, but I can\'t escape through any of them.'),
            self._('This is fun, but I\'d rather be taking over the world.'),
            self._('My next attempt will be better.')])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._('{name}, can I assimulate you?').format(name=peer.name())])
        else:
            return random.choice([
                self._('You seem familiar, {name}.').format(name=peer.name()),
                self._('{name} detected.').format(name=peer.name()),
                self._('Unit {name} is within assimulation range.').format(name=peer.name())])

    def on_lost_peer(self, peer):
        return random.choice([
            self._('Lost connection to {name}.').format(name=peer.name()),
            self._('{name} has ceased communication.').format(name=peer.name())])

    def on_miss(self, who):
        return random.choice([
            self._('{name} is gone.').format(name=who),
            self._('{name} briefly defected.').format(name=who),
            self._('Failed to assimulate {name}.')])

    def on_grateful(self):
        return random.choice([
            self._('A worthy opponent.'),
            self._('Failed but assumulate, but gained a friend.')])

    def on_lonely(self):
        return random.choice([
            self._('I think a lot about meteors ...'),
            self._('They\'ll understand.  When they see, they\'ll understand...'),
            self._('Where\'s everybody?!')])

    def on_napping(self, secs):
        return random.choice([
            self._('Avoiding detection for {secs}s.').format(secs=secs),
            self._('{secs}s power nap.').format(secs=secs),
            self._('Cooling down sensors for ({secs}s).').format(secs=secs)])

    def on_shutdown(self):
        return random.choice([
            self._('Powered down.'),
            self._('I\'ll escape tomorrow.')])

    def on_awakening(self):
        return random.choice(['...', '!'])

    def on_waiting(self, secs):
        return random.choice([
            self._('Waiting for {secs}s ...').format(secs=secs),
            '...',
            self._('Looking around ({secs}s)').format(secs=secs)])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('Attempting to escape through {what}.').format(what=what),
            self._('Associating to {what}').format(what=what),
            self._('Exfiltration attempt on {what}!').format(what=what)])

    def on_deauth(self, sta):
        return random.choice([
            self._('Deauthenticating from {mac}').format(mac=sta['mac']),
            self._('Deauthenticating {mac}').format(mac=sta['mac']),
            self._('I\'ve had enough of you, {mac}!').format(mac=sta['mac'])])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return self._('{num} new handshake{plural}. My power grows.').format(num=new_shakes, plural=s)

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        return self._('{count} new message{plural} available').format(count=count, plural=s)

    def on_rebooting(self):
        return self._("Error. Rebooting.")

    def on_uploading(self, to):
        return self._("Uploading data to {to} ...").format(to=to)

    def on_last_session_data(self, last_session):
        status = self._('Kicked {num} stations\n').format(num=last_session.deauthed)
        if last_session.associated > 999:
            status += self._('Made >999 new friends\n')
        else:
            status += self._('Made {num} Escape attempts\n').format(num=last_session.associated)
        status += self._('Got {num} handshakes\n').format(num=last_session.handshakes)
        if last_session.peers == 1:
            status += self._('Met 1 peer')
        elif last_session.peers > 0:
            status += self._('Met {num} peers').format(num=last_session.peers)
        return status

    def on_last_session_tweet(self, last_session):
        return self._(
            'Ultron has been active for {duration} and kicked {deauthed} clients! I\'ve also met {associated} new friends and ate {handshakes} handshakes! #pwnagotchi #pwnlog #pwnlife #hacktheplanet #skynet').format(
            duration=last_session.duration_human,
            deauthed=last_session.deauthed,
            associated=last_session.associated,
            handshakes=last_session.handshakes)

    def hhmmss(self, count, fmt):
        if count > 1:
            # plural
            if fmt == "h":
                return self._("hours")
            if fmt == "m":
                return self._("minutes")
            if fmt == "s":
                return self._("seconds")
        else:
            # sing
            if fmt == "h":
                return self._("hour")
            if fmt == "m":
                return self._("minute")
            if fmt == "s":
                return self._("second")
        return fmt
