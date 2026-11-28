"""Generates the Human Week static pages (shared header/footer). Output is plain HTML.
Retro-OS blend: windows, Paint frames, Notepad, dialogs, taskbar, pixel decoration."""
import csv, html, os
from collections import OrderedDict
from datetime import datetime

ROOT = '/home/claude/humanweek'
HOST_PDF = '/assets/docs/human-week-host-guide.pdf'
MAILTO = 'mailto:hello@humanweek.org?subject=Hey%20Human%20Week!'
NAV = [('Home', '/'), ('About', '/about/'), ('Schedule', '/schedule/'), ('Host', '/host/'), ('Attend', '/attend/')]
TICKER = ["Let's be human, first", "Robots wait outside", "Boston, MA", "Host a conversation"]
TOPICS = ['Artificial Intelligence', 'Education', 'Future Of Work', 'Health And Care', 'Strong Cities', 'Social Media', 'Attention Spans']
PX = '/assets/img/pixel/'


# ---------- components ----------
def deco(name, cls):
    size = 'cloud' if name == 'cloud' else 'star'
    return f'<img class="deco deco--{size} {cls}" src="{PX}{name}.svg" alt="" aria-hidden="true">'


def bar(file):
    return f'<div class="win__bar"><span>{file}</span><span class="win__btns" aria-hidden="true"><i>_</i><i>□</i><i>×</i></span></div>'


def win(file, body, mod='', tag='article'):
    return f'<{tag} class="win {mod}">{bar(file)}<div class="win__body">{body}</div></{tag}>'


def menu(items):
    return '<div class="menu-bar" aria-hidden="true">' + ''.join(f'<span><u>{i[0]}</u>{i[1:]}</span>' for i in items) + '</div>'


def notepad(file, body, mod=''):
    return f'<article class="win notepad {mod}">{bar(file + " - Notepad")}{menu(["File", "Edit", "Format", "View", "Help"])}<div class="win__body">{body}</div></article>'


PAINT_MENU = ["File", "Edit", "View", "Image", "Options", "Help"]


def paint(src, alt, file, mod='', pos=''):
    style = f' style="object-position:{pos}"' if pos else ''
    return (f'<figure class="win paint {mod}">{bar(file + " - Paint")}{menu(PAINT_MENU)}'
            f'<div class="paint__canvas"><img src="/assets/img/photos/{src}" alt="{alt}" loading="lazy"{style}></div>'
            f'<figcaption class="paint__status"><span>Boston, MA</span><span>humanweek.org</span></figcaption></figure>')


def paint_empty(file, hint, mod=''):
    return (f'<figure class="win paint paint--empty {mod}">{bar(file + " - Paint")}{menu(PAINT_MENU)}'
            f'<div class="paint__canvas"><p><img src="{PX}picture.svg" alt="" aria-hidden="true">Photo: {hint}</p></div>'
            f'<figcaption class="paint__status"><span>Waiting for a photo</span><span>humanweek.org</span></figcaption></figure>')


def head(title, desc):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Human Week">
<meta property="og:image" content="https://humanweek.org/assets/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Let's be Human First. Not anti-tech. Pro-human. Human Week, Boston, MA.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://humanweek.org/assets/img/og-image.png">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/css/fonts.css">
<link rel="stylesheet" href="/assets/css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to Main Content</a>
'''


def header(active):
    links = ''.join(f'<li><a href="{u}"{" aria-current=\"page\"" if n == active else ""}>{n}</a></li>' for n, u in NAV)
    items = ''.join(f'<span>{t}</span><span>•</span>' for t in TICKER)
    return f'''<header class="site-header">
  <div class="wrap">
    <a class="logo" href="/">HUMAN<br>WEEK</a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="nav" id="site-nav" aria-label="Main"><ul>{links}</ul></nav>
  </div>
  <div class="ticker ticker--dark" aria-hidden="true"><div class="ticker__track">{items}</div></div>
</header>
<main id="main">
'''


def topic_ticker(more=True):
    items = TOPICS + (['And More'] if more else [])
    return '<div class="ticker ticker--sage" aria-hidden="true"><div class="ticker__track">' + ''.join(f'<span>{t}</span><span>•</span>' for t in items) + '</div></div>\n'


def newsletter():
    form = '''<h2 class="form-title">Join our Newsletter!</h2>
        <p class="form-lead">Join our mailing list to receive updates and announcements about Human Week 2027!</p>
        <div class="beehiiv-embed"><script async src="https://subscribe-forms.beehiiv.com/v3/loader.js" data-beehiiv-form="6ddcc59b-b811-4455-94c0-ef54edf48399"></script></div>
        <p class="form-note">Prefer the web? Sign up at <a href="https://humanweek.beehiiv.com">humanweek.beehiiv.com</a>.</p>'''
    return f'''<section class="band-night" id="newsletter">
  {deco('star', 'night-star-1')}{deco('star', 'night-star-2')}{deco('sparkle', 'night-star-3')}{deco('star', 'night-star-4')}
  <div class="wrap">
    {win('join_newsletter.exe', form, 'dialog')}
  </div>
</section>
'''


def footer():
    return f'''</main>
<footer>
  <div class="footer-sky">
    {deco('cloud', 'footer-cloud-1')}{deco('cloud', 'footer-cloud-2')}{deco('star', 'footer-star-1')}{deco('star', 'footer-star-2')}
    <div class="wrap">
      <p class="see-you">SEE YOU AT</p>
      <p class="pixel-title">Human Week</p>
    </div>
  </div>
  <nav class="taskbar" aria-label="Footer">
    <a class="start" href="/"><img src="/assets/img/favicon.svg" alt="" aria-hidden="true">Human Week</a>
    <a href="/about/">About</a>
    <a href="/attend/">Attend</a>
    <a href="https://www.instagram.com/bostonhumanweek">Instagram</a>
    <a href="https://www.linkedin.com/company/boston-human-week/">LinkedIn</a>
    <a href="{MAILTO}">Contact</a>
    <span class="clock">© 2026 by Boston Human Week. All Rights Reserved.</span>
  </nav>
</footer>
<script src="/assets/js/site.js"></script>
</body>
</html>
'''


DEF = '<p class="definition"><b>pro-human</b> (adj.) — putting what people need to <span class="ink">live well</span> ahead of what a system needs to <span class="ink">grow</span>.</p>'


def write(path, s):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w').write(s)


def intro(inner):
    return f'<section class="intro">{deco("cloud", "intro-cloud")}{deco("star", "intro-star")}<div class="wrap">{inner}</div></section>\n'


# ---------------- HOME ----------------
hero_copy = '''<p class="lead">Not anti-tech. Pro-human.</p>
      <p>Human Week 2026 was a decentralized conference designed to facilitate discussion among people, companies, and leaders who want the future to feel more human.</p>
      <p>We brought Boston five days of events about artificial intelligence, attention, the connection economy, and more.</p>
      <div class="btn-row"><a class="btn btn--lg" href="/schedule/">See the schedule</a><a class="btn btn--gray" href="/host/">Host a conversation</a></div>'''

about_body = '''<h2 class="h2">Boston Human Week 2026</h2>
      <p>Human Week 2026 was a decentralized conference designed to facilitate discussion among people, companies, and leaders who want the future to feel more human.</p>
      <p>The guiding question is this: how do we structure society, technology, and our built environment to create a future where human needs are prioritized?</p>
      <p>Human Week brought the people building technology and the people living with it into the same room.</p>
      <p>Across the landscapes of artificial intelligence, climate change, social media, education, and more: if you’re a human, your authentic voice is welcomed and needed. And if you are a robot, well…please wait outside.</p>
      <div class="actions"><a class="btn" href="/schedule/">See the schedule</a></div>'''

mission_body = '''<h2 class="h2">Better events. Better conversations.</h2>
      <p>We have been to so many bad events that we now refer to them as "event slop." With Human Week, our mission is to fill a week with conversations that change your perspective(s), introduce you to someone new, and most importantly, are worth your (and our) precious time.</p>
      <p>We ask everyone who hosts during Human Week to start with a genuine question, to design for accessibility, and to put human needs first. That's it. What follows (we hope) is a week of rooms where people say what they believe, hear something they hadn't considered, and leave with new relationships, ideas, and excitement.</p>
      <p><em>Anyone with a stake in the future is welcome to host a Human Week conversation. As far as we can tell, that's everybody.</em></p>
      <div class="actions"><a class="btn btn--yellow" href="/host/">Host an event</a></div>'''

vision_body = '''<h2 class="h2">A simple standard</h2>
      <p>Does a new technology or policy make life better for the people who have to live with it? Our vision for Human Week is to <em>inspire conversations that question what choices advance this standard.</em></p>
      <p>Human Week conversations should take a hopeful approach: there is no doom and gloom here. We believe that all things are possible when we set our minds to an outcome. We also believe that no technology is inherently bad, and that the structures, incentives, and regulations that surround them will shape whether humans flourish in the 21st century.</p>
      <div class="actions"><a class="btn" href="/about/">More about us</a></div>'''


def tile(file, src=None, alt=''):
    if src:
        return f'<figure class="tile"><div class="tile__img"><img src="/assets/img/photos/{src}" alt="{alt}" loading="lazy"></div><figcaption>{file}</figcaption></figure>'
    return f'<figure class="tile"><div class="tile__img"><img class="icon" src="{PX}picture.svg" alt=""></div><figcaption>{file}</figcaption></figure>'


gallery = ('<div class="address"><b>Address</b><span>C:\\Human Week\\2026\\Photos</span></div>'
           '<div class="win__body"><div class="tiles">'
           + tile('happy_human_hour.jpg', 'happy_human_hour.jpg', 'People talking in small groups at Happy Human Hour')
           + tile('host_dinner.jpg', 'host_dinner.jpg', 'A group of attendees posing together at a host dinner')
           + tile('closing_celebration.jpg', 'closing_celebration.jpg', 'A packed room at the Human Week closing celebration, one person holding a The Slop Must Stop sticker')
           + tile('calling_all_connectors.jpg', 'calling_all_connectors.jpg', 'Attendees waving at the camera at Calling All Connectors')
           + tile('optimists_meetup.jpg', 'optimists_meetup.jpg', 'Attendees cheering together at the Optimists Meetup')
           + tile('host_dinner_2.jpg', 'host_dinner_2.jpg', 'People listening around a long table at a host dinner')
           + '</div></div>')

home = head('Human Week: Not anti-tech. Pro-human.', 'Human Week is a decentralized conference for people, companies, and leaders who want the future to feel more human.') + header('Home') + f'''
<section class="hero">
  {deco('cloud', 'hero-cloud-1')}{deco('cloud', 'hero-cloud-2')}{deco('star', 'hero-star-1')}{deco('star', 'hero-star-2')}{deco('sparkle', 'hero-star-3')}
  <div class="wrap">
    <div>
      <h1 class="hero__title"><span>Let's be</span><span class="human">Human</span><span>First<img class="hero__shades" src="{PX}shades.svg" alt="" aria-hidden="true"></span></h1>
    </div>
    {win('human_first.exe', hero_copy)}
  </div>
</section>

<section class="section">
  <div class="wrap">{paint('host_dinner.jpg', 'A group of Human Week attendees posing together at a host dinner in a restaurant', 'host_dinner.jpg', 'paint--wide', '50% 60%')}</div>
</section>

<section class="section section--tight">
  <div class="wrap grid-2">
    {win('about.txt', about_body, 'win--sage')}
    <div class="stack">
      {notepad('pro-human.txt', '<p class="notepad__title">Pro-Human</p>' + DEF)}
      {paint('host_dinner_2.jpg', 'People listening around a long table at a Human Week host dinner', 'host_dinner_2.jpg')}
    </div>
  </div>
</section>

<section class="section section--pink">
  <div class="wrap grid-2 grid-2--center">
    {paint('happy_human_hour.jpg', 'People talking in small groups at Happy Human Hour', 'happy_human_hour.jpg')}
    {win('mission.exe', mission_body, 'win--purple')}
  </div>
</section>

<section class="section">
  <div class="wrap grid-2 grid-2--center">
    {win('vision.doc', vision_body, 'win--navy')}
    {paint('conversation.jpg', 'Two attendees talking and laughing in a gallery hung with colorful paintings', 'conversation.jpg')}
  </div>
</section>
''' + topic_ticker() + f'''
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2 class="h2">Human Week 2026 in photos</h2>
    </div>
    <div class="win explorer win--yellow">{bar('Photos')}{gallery}</div>
  </div>
</section>
''' + newsletter() + footer()
write('index.html', home)

# ---------------- ABOUT ----------------
people = [('Ang Richard', 'ang-richard.jpg', "Ang Richard is an educator, creator, and researcher whose practice revolves around one common theme: bringing together and elevating community in ways that ensure people are seen, heard, and valued. Researching AI as a career shock for her Ph.D., Ang finds herself caught in the rapid evolution of technology and its impact on real careers. That’s why she wanted to be part of Human Week — advancing workplaces must be grounded in the stories of those whose work and lived experience lift missions and drive all of us forward."),
          ('JAKE Small', 'jake-small.jpg', "JAKE is a storyteller, educator, and community builder who believes deeply in the power of bringing people together around ideas that matter. He’s driven by a pretty simple question: how do we make sure the right ideas (and the people holding them) get the platforms they need to change the world? That’s what drew him to Human Week; the chance to build something that feels curious, a little unexpected, and genuinely human."),
          ('Sarah Agopian-Khalifé', 'sarah-agopian-khalife.jpg', "Sarah Agopian-Khalifé is an experience designer, community builder, and facilitator. She believes that when we bring people together, we better make it worth their time and energy. There’s a lot of event slop out there, especially in decentralized conferences, and those rooms are also usually only reserved for certain types of people. That’s why she wanted to build Human Week — to show what’s possible in this format when we make space for more perspectives, prioritize quality over quantity, and lead with a human-first lens instead of it being an afterthought."),
          ('Zach Reizes', 'zach-reizes.jpg', "Zach Reizes is a curator, strategist, and community builder who is fascinated by the messy nuance of being alive. Zach has spent years asking what happens when we build events around how people think, connect, and recharge. He is an advocate for building a better society that meets human needs first. That's why he wanted to help create Human Week - because the conversations shaping our future deserve rooms designed with humans in mind.")]
topics = [('Artificial Intelligence', "There's a collective reckoning happening in real time over where, how, and why people want to encounter Artificial Intelligence in their daily lives. It's time to take this conversation from the LinkedIn comments section to the real world."),
          ('Future of Work', "Remote, hybrid, automated, four-day, fractional…the shape of 21st-century work is being rewritten in real time. How do we prepare kids for a changing world? And what do we want our work to mean?"),
          ('Education', "Educators are working through AI use, phone policies, and a rewritten definition of cheating, and they have the clearest view of what's working and what isn't. How can we better connect with and learn from one another?"),
          ('Social Media &amp; Attention', "How do I escape this doomscroll pattern? And what can we build to maximize connection and intentional sharing of ideas, stories, and relationships? Researchers, parents, and more all have real thoughts on this question."),
          ('Health, Care &amp; Connection', "What systems and structures make doing the most human thing possible? And why is it so hard to make new friends? Let's explore what technologies and ideas give people more time with each other instead of less."),
          ('And much more...', "Dreaming of a conversation that doesn't fit neatly into the above topics? That's fine. Plenty of our hosts brought events and activations of their own. Human Week is what you make of it!")]
folders = ['folder-yellow', 'folder-purple', 'folder-blue']
about = head('About | Human Week', 'Human Week 2026 is a decentralized conference built to facilitate discussion between the people, companies, and leaders who want the future to be more Human.') + header('About') + intro(f'''<div class="grid-2 grid-2--center">
    <div>
      {DEF}
      <h1 class="display">Join us for a <em>pro-human</em> conversation</h1>
    </div>
    {win('welcome.txt', '<p>Human Week 2026 was a decentralized conference built to facilitate discussion between the people, companies, and leaders who want the future to be more Human.</p><p>Across the landscapes of artificial intelligence, climate change, social media, education and more, if you’re a human, your authentic voice is welcomed and needed. And if you are a robot, well…please wait outside.</p>')}
  </div>''') + topic_ticker(False) + f'''
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2 class="h2">Conversations worth your time to have</h2>
      <p class="lead measure">The guiding question is: how do we structure society, technology, and our built environment to create a future where human needs are prioritized first?</p>
    </div>
    <div class="topics">
      {''.join(f'<div class="topic"><img src="{PX}{folders[i % 3]}.svg" alt="" aria-hidden="true"><h3 class="h3">{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(topics))}
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">{paint('closing_celebration.jpg', 'A packed room at the Human Week closing celebration', 'closing_celebration.jpg', 'paint--wide', '50% 45%')}</div>
</section>

<section class="section section--pink">
  <div class="wrap grid-2">
    {win('who_can_attend.txt', '''<h2 class="h2">Everyone. Genuinely.</h2>
      <p>Human Week is for anyone who is wondering what all of this — the algorithms, the automation, the always-on feeling — is doing to us. This is not an anti-technology space: it's a pro-Human one.</p>
      <p>Human Week takes a hopeful approach – there is no doom and gloom here. We believe that all things are possible when we set our minds to an outcome. We also believe that no technology is inherently bad, and that the structures, incentives, and regulations that surround them will shape whether or not humans flourish in the 21st century.</p>
      <p>Human Week is built for two crowds in the same room: the founders, operators, and builders who regularly attend tech events, and "everybody else" who live and engage with the new technologies and systems we are all experiencing in real time.</p>''', 'win--purple')}
    <div class="stack">
      {win('organizers.txt', f'''<p>Boston Human Week is brought to you by an ad hoc group of volunteer organizers from across the greater Boston area. As people who work at the intersection of technology and community, we are taking a pro-human position on the way we talk about AI, societal structures, and more.</p>
        <p>Questions, compliments, press inquiries, and other requests can be directed to <a href="{MAILTO}">hello@humanweek.org</a></p>
        <div class="actions"><a class="btn" href="/schedule/">See all events</a></div>''', 'win--navy')}
      {paint('organizers.jpg', 'The four Human Week organizers together: Ang Richard, Zach Reizes, JAKE Small and Sarah Agopian-Khalifé', 'organizers.jpg', '', '50% 40%')}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2 class="h2 section-head">The humans behind Human Week</h2>
    <div class="people">
      {''.join(win(img.replace('-', '_'), f'<img src="/assets/img/{img}" alt="{n}" width="104" height="104"><div><h3>{n}</h3><p>{b}</p></div>', 'person ' + ['win--sage', 'win--yellow', 'win--yellow', 'win--sage'][i]) for i, (n, img, b) in enumerate(people))}
    </div>
  </div>
</section>
''' + footer()
write('about/index.html', about)

# ---------------- SCHEDULE ----------------
rows = [r for r in csv.DictReader(open('/home/claude/humanweek-export/data/schedule-2026.csv')) if 'umbrella' not in r['event']]
days = OrderedDict()
for r in rows:
    days.setdefault(r['date'], []).append(r)
blocks = ''
for d, evs in days.items():
    dt = datetime.strptime(d, '%Y-%m-%d')
    items = ''
    for e in evs:
        hosts = [h.strip() for h in e['hosts'].split(';') if h.strip() and h.strip() != 'Human Week'] or ['Human Week']
        where = ', '.join(x for x in [e['venue'], e['city']] if x)
        meta = ' · '.join(x for x in [where, 'Hosted by ' + ', '.join(hosts)] if x)
        items += f'<div class="event"><time>{e["start_et"]} – {e["end_et"]}</time><div><h3><a href="{e["luma_url"]}">{html.escape(e["event"])}</a></h3><p>{html.escape(meta)}</p></div></div>'
    label = dt.strftime("%A")
    blocks += win(label, items, 'day', tag='section')
sched = head('Schedule | Human Week', 'The full schedule of Boston Human Week 2026.') + header('Schedule') + intro('''<h1 class="display">Human Week Schedule</h1>
    ''' + notepad('thank_you.txt', '''<p>Boston Human Week took place from Nov. 9th – 13th, 2026. Thank you for joining us! You can view our schedule of past events below, and be sure to <a href="#newsletter">join our newsletter</a> for updates about where we’re headed next.</p>''', 'recap-note')) + f'''
<section class="section">
  <div class="wrap">{paint('optimists_meetup.jpg', 'Attendees cheering together at the Optimists Meetup', 'optimists_meetup.jpg', 'paint--wide', '50% 48%')}</div>
</section>
<section class="section section--tight">
  <div class="wrap"><div class="schedule">{blocks}</div></div>
</section>
''' + newsletter() + footer()
write('schedule/index.html', sched)

# ---------------- HOST ----------------
gtypes = [('Point of View Panels', "This is a specific, structured, and moderated conversation designed to elicit disagreement productively. It brings together two or three voices who disagree or approach the same question from genuinely different lived angles, and is moderated towards friction rather than consensus. We suggest about twenty minutes of discussion and debrief afterwards, with framing questions that ask people to reflect positively on what they learned or took away from the session."),
          ('Working Sessions', "Hands-on, ending in something tangible rather than a memory of a talk. Ideal structure involves no more than 10 minutes of set-up and then hands are moving within the first 10 minutes. This includes art classes, yoga, hack-a-thons, and more. Invent your own!"),
          ('Group Discussions', "Salon-style, no stage. Hosted round tables of 5-8, each with a facilitator. The facilitator does not need to be an expert, this is just someone keeping the conversation moving. One shared prompt. Ideal structure takes the “report out” approach, where you start as pairs, then move to groups of four, then eight, then share out to the room."),
          ('Communal Meals or Walks', "A shared table or shared movement event. Could be a small group dinner, potluck, or a walking conversation instead of a seated program. Walks and meals should be capped at a size where conversation is still possible."),
          ('Performances &amp; Talks', "Musical acts, single-speaker talks, poetry events, and more fall under this category. Anything that involves light pointed at a human on stage. Ideal structure involves audience interaction with the work through reflection or direct, auditory engagement.")]
tabbtns = ''.join(f'<button role="tab" id="tab-{i}" aria-controls="panel-{i}" aria-selected="{"true" if i == 0 else "false"}">{t}</button>' for i, (t, _) in enumerate(gtypes))
panels = ''.join(f'<div role="tabpanel" id="panel-{i}" aria-labelledby="tab-{i}"{"" if i == 0 else " hidden"}><h3 class="h3">{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(gtypes))
host_form = '''<form name="host-interest" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="/thanks/">
        <input type="hidden" name="form-name" value="host-interest">
        <p class="hidden"><label>Leave this empty: <input name="bot-field"></label></p>
        <div class="fields">
          <div class="field"><label for="h-first">First name *</label><input id="h-first" name="first_name" required autocomplete="given-name"></div>
          <div class="field"><label for="h-last">Last name *</label><input id="h-last" name="last_name" required autocomplete="family-name"></div>
          <div class="field full"><label for="h-email">Email *</label><input id="h-email" name="email" type="email" required autocomplete="email"></div>
          <div class="field full"><label for="h-org">Company or Organization name *</label><input id="h-org" name="company" required autocomplete="organization"></div>
          <div class="field full"><label for="h-topic">Event topic *</label><input id="h-topic" name="event_topic" required></div>
        </div>
        <div class="form-actions"><button class="btn btn--yellow" type="submit">Submit</button></div>
      </form>'''
host = head('Host | Human Week', 'Host a Human Week conversation. In an era of automation and layoffs, be known for the opposite.') + header('Host') + intro(f'''<div class="grid-2 grid-2--center">
    <div>
      <p class="lead">In an era of automation and layoffs, be known for the opposite.</p>
      <h1 class="display">Calling all <em>human first</em> companies</h1>
    </div>
    {win('calling_all_companies.txt', '<p>Every year, the headlines about technology are the same: layoffs, automation, and another job that AI can do a little cheaper. Inside that story, the companies getting the human side right rarely get mentioned at all.</p><p>For five days, we brought together organizations of every kind — tech, healthcare, finance, education, and beyond — who are leading with people-first principles.</p><p>Hosts joined one of our flagship conversations or ran their own program. The only requirement was a shared desire to see humans flourish in an age where authenticity is increasingly hard to come by.</p>')}
  </div>''') + f'''
<section class="section">
  <div class="wrap grid-2">
    {win('who_can_host.txt', '''<h2 class="h2">Anyone. Mostly.</h2>
      <p>Our mission at Human Week is to fill a week with conversations that are worth your time to have: conversations that change your perspective, introduce you to someone new, and lead to inspiring, pro-human collaborations. So long as this calls to you, you are part of Human Week.</p>
      <p>We ask everyone who hosts during Human Week to start with a real question, take a clear stance, and put human needs first. That's it. What followed was a week of rooms where people said what they think, heard something they hadn't considered, and left with new relationships, ideas and excitement.</p>
      <p><em>Anyone with a stake in the future is welcome to host a Human Week conversation. As far as we can tell, that's everybody.</em></p>''', 'win--purple')}
    {notepad('house_rules.txt', f'''<ol class="rules">
        <li>Name the topic and why it matters</li>
        <li>Cut the industry jargon</li>
        <li>Design for participation</li>
        <li>Treat comfort as an access issue</li>
        <li>Provide a thesis (aka "your why")</li>
      </ol>
      <p>Find more details in our design playbook, below.</p>
      <div class="actions"><a class="btn btn--yellow" href="{HOST_PDF}">Download our event design guide</a></div>''')}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">{paint('calling_all_connectors.jpg', 'A host and their room waving at the camera at Calling All Connectors', 'calling_all_connectors.jpg', 'paint--wide', '50% 45%')}</div>
</section>

<section class="section section--sky">
  {deco('cloud', 'intro-cloud')}
  <div class="wrap grid-2">
    <div>
      <h2 class="h2">Gathering types we support</h2>
      <p>Part of the Human Week philosophy is that quality events lead to quality outcomes. We support gathering models that include all and encourage productive connection and conversation.</p>
    </div>
    {win('gathering_types.cfg', f'<div role="tablist" aria-label="Gathering types">{tabbtns}</div>{panels}', 'tabs win--yellow')}
  </div>
</section>

<section class="section">
  <div class="wrap grid-2 grid-2--center">
    {win('submit_your_event.exe', '''<h2 class="h2">Want to host next time?</h2>
      <p>Event submissions for Human Week 2026 are closed. Thank you to every host who brought an awesome, pro-human event to Boston! If you'd like to host in the future, drop your info here and join our newsletter for updates on Human Week 2027.</p>
      <div class="actions"><a class="btn btn--lg btn--yellow" href="/#newsletter">Join the newsletter</a></div>''', 'win--pink')}
    {win('host_interest.exe', host_form, 'dialog dialog--wide')}
  </div>
</section>
''' + footer()
write('host/index.html', host)

# ---------------- ATTEND ----------------
attend = head('Attend | Human Week', 'Human Week, all over Boston, MA.') + header('Attend') + intro(f'''<div class="grid-2 grid-2--center">
    {win('for_attendees.txt', '''<h1 class="h2">For attendees</h1>
      <ul class="facts">
        <li><b>Where:</b> All over Boston, MA</li>
        <li><b>Who:</b> You and several hundred new friends</li>
        <li><b>Why:</b> Because we can do great things when we prioritize human needs first.</li>
      </ul>
      <p>Human Week 2026 is a wrap! Thank you to everyone who showed up. Join our newsletter below for updates on Human Week 2027.</p>''', 'win--purple')}
    {paint('conversation.jpg', 'Two attendees meeting each other at a Human Week event', 'conversation.jpg')}
  </div>''') + '''
''' + newsletter() + footer()
write('attend/index.html', attend)

# ---------------- THANKS (form success) ----------------
thanks = head('Thank you | Human Week', 'Thanks for reaching out to Human Week.') + header('') + intro(f'''<div class="measure center">
    {win('message_sent.exe', '<h1 class="display">Thank you!</h1><p class="lead">Thanks so much for reaching out. We\'ll be in touch soon!</p><div class="actions"><a class="btn" href="/">Back to Human Week</a></div>', 'dialog')}
  </div>''') + '<div class="section"></div>' + footer()
write('thanks/index.html', thanks)
print('pages written')
