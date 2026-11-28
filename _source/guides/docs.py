import os
OUT = '_docs'  # run from repo root; copy guides/docs.css into _docs first
PX = '/assets/img/pixel/'


def win(title, body, v='v-blue', extra='', tag='', style=''):
    t = f'<span class="tag">{tag}</span>' if tag else ''
    return (f'<div class="win {v} {extra}" style="{style}"><div class="bar"><span>{title}</span>{t}'
            f'<span class="btns"><i>_</i><i>□</i><i>×</i></span></div><div class="wb">{body}</div></div>')


def deco(name, style):
    return f'<img class="deco" src="{PX}{name}.svg" style="{style}">'


def sec(num, title, sub):
    sub_html = f'<span class="sub">// {sub}</span>' if sub else ''
    return f'<div class="sec"><span class="num">{num}</span><h2>{title}</h2>{sub_html}</div>'


HOST_TASK = '<div class="task"><span class="start">HUMANWEEK.ORG</span><span>GUIDE TO BETTER EVENT DESIGN ✳ VOL. 01</span></div>'


def head(cls, title):
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>'
            f'<link rel="stylesheet" href="docs.css"><style>@page{{size:{"letter" if cls=="portrait" else "letter landscape"};margin:0}}</style>'
            f'</head><body class="{cls}">')


# ---------------- HOST GUIDE ----------------
h = head('portrait', 'Human Week Guide to Better Event Design')

# p1 cover
h += f'''<section class="page" style="background:var(--sky)">
{deco('cloud', 'width:110px;right:.5in;top:1.7in')}{deco('sparkle', 'width:20px;right:2.1in;top:1.35in')}{deco('star', 'width:22px;left:4.9in;top:3.55in')}
<div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:.45in">
  <div class="logo">Human<br>Week</div><div class="meta" style="margin-top:4px">Boston, MA ✳ November 9–13</div></div>
<div class="meta" style="margin-bottom:8px">The Human Week</div>
<h1 class="display" style="font-size:44pt">Guide to<br><em>Better Event</em><br>Design</h1>
<p class="serif" style="font-size:17pt;font-style:italic;margin:14px 0 14px">For hosts of Human Week events</p>
{win('welcome.txt', '<p>Human Week is five days of conversations about how humans interact with a changing world: AI, education, work, care, cities, attention, and more. Anyone with a stake in the future can host. <em>As far as we can tell, that&#39;s everybody.</em></p><p>Events can happen anywhere in the greater Boston area, not just the city itself, and at any time of day. Think about when your audience is actually free: before work, over lunch, after work. Evenings are great, but they&#39;re not the rule.</p>', 'v-white', 'shade-navy')}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
{win('one_we_curate.txt', '<p>We&#39;re curating for quality, not just filling a calendar. Every session on the schedule should meet the design principles in this guide, and we read every submission against them.</p>', 'v-sage', 'shade-navy')}
{win('two_you_own_your_event.txt', '<p>Human Week is decentralized. You design it, secure the space, line up your speakers, promote it, and handle the costs. We handle the week: the schedule, the shared marketing, and the shared identity that makes Human Week events stand out.</p>', 'v-pink', 'shade-navy')}
</div>
{win('timeline.exe', '''<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px">
<div><div class="meta" style="color:var(--purple)">Sep 7</div>Submissions close, 11:59pm ET</div>
<div><div class="meta" style="color:var(--purple)">Sep 8–11</div>You hear back either way</div>
<div><div class="meta" style="color:var(--purple)">Oct 11</div>Title, description, venue, and time locked</div>
<div><div class="meta" style="color:var(--purple)">Nov 9–13</div>Human Week</div></div>''', 'v-purple', 'shade-navy', style='margin-bottom:6px')}
<p class="serif" style="font-style:italic;font-size:11.5pt;text-align:center;margin-top:8px">Missed the window? It&#39;s not the end of the world — events will still be added to the calendar on a rolling basis.</p>
{HOST_TASK}</section>'''

# p2 principles
pr = [('Poses a real question or thesis', 'Experience should hinge on a question or idea. "Who should be allowed to use AI to grade a kid&#39;s essay?" beats "AI and the Future of Education" every time.', 'v-purple'),
      ('Uses clear language', 'Clear language is communication that is plain and direct, so that attendees can find what they need, understand it the first time, and use that information.', 'v-lilac'),
      ('Leads to pro-human, positive conversations', 'Explores the topic by considering whether it makes life better for the people who live with it. Focuses on positive outcomes and productive sharing of diverse perspectives.', 'v-pink'),
      ('Participation over consumption', 'Prioritizes engagement across tables, in small circles, or other structured discussion — not just a stage and rows of chairs.', 'v-sage'),
      ('Prioritize accessibility', 'Considers how best to provide rooms that don&#39;t echo, enough seating, no forced mingling, a quiet corner to decompress. Attending to human needs makes events accessible.', 'v-navy')]
h += f'<section class="page">{deco("sparkle", "width:18px;right:.7in;top:.62in")}{sec("01", "Design principles", "overarching")}<p class="lede">What makes a Human Week event. We read every submission against these:</p>'
for i, (t, b, v) in enumerate(pr):
    h += win(f'{i+1:02d}_{t.lower().replace(" ", "_").replace(",", "")}.txt'[:44], f'<p style="font-family:var(--disp);font-weight:800;text-transform:uppercase;color:var(--navy);margin-bottom:3px">{t}</p><p>{b}</p>', v, 'shade-navy')
h += f'{deco("cloud", "width:100px;left:.55in;bottom:.7in")}{HOST_TASK}</section>'

# p3 types
ty = [('Point of View Panels', 'Friction, not consensus', 'This is a specific, structured, and moderated conversation designed to elicit disagreement in a productive way. Bring together two or three voices who disagree, or approach the same question from genuinely different lived angles. Moderated towards friction, not consensus. Preference is for discussion and debrief afterwards, with framing questions that ask people to reflect positively on what they learned or took away from the session.', 'v-purple'),
      ('Small-Circle Discussion', 'Salon-style, no stage', 'Salon-style, no stage. Hosted round tables of small groups, each with a facilitator. The facilitator does not need to be an expert, this is just someone keeping the conversation moving. One shared prompt. Ideal structure takes the “report out” approach, where you start as pairs, then move to groups of four, then eight, then share out to the room.', 'v-lilac'),
      ('Working Sessions', 'Hands moving in 10 minutes', 'Hands-on, ending in something tangible rather than a memory of a talk. Ideal structure involves no more than 10 minutes of set-up and then hands are moving within the first 10 minutes. This includes art classes, yoga, hack-a-thons, and more. Invent your own!', 'v-pink'),
      ('Performances and Talks', 'Light on a human', 'Musical acts, single-speaker talks, poetry events and more fall under this category. Anything that involves light pointed at a human on stage. Ideal structure involves audience interaction with the work through reflection or direct, auditory engagement.', 'v-sage'),
      ('Communal Meal / Walk &amp; Talk', 'Shared table, shared movement', 'A shared table or shared movement event. Could be a small group dinner, potluck, or a walking conversation instead of a seated program. Walks and meals should be capped at a size where conversation is still possible.', 'v-navy')]
h += f'<section class="page">{sec("02", "Types of events", "styles we support")}<div style="height:6px"></div>'
for t, tag, b, v in ty:
    h += win(t, f'<p>{b}</p>', v, 'shade-navy', tag=tag)
h += f'{HOST_TASK}</section>'

# p4 topics
topics = [('Intelligence', 'v-purple', [('AI and People', 'what work, creativity, and purpose look like when computers and humans work together'), ('Emotional intelligence in an automated world', 'the skills machines can&#39;t replace'), ('The death and rebirth of expertise', 'mastery when a passable draft takes moments to generate'), ('Wisdom vs. information', 'why knowing more hasn&#39;t made us wiser'), ('Animal and ecological intelligence', 'what humans might learn by taking non-human minds seriously'), ('Neurodivergence and the myth of "normal"', 'different minds, different kinds of intelligence, different value'), ('Different ways of knowing', 'exploring all the ways we know things: our bodies, our hearts, our minds.')]),
          ('Attention', 'v-pink', [('Attention as the scarce resource', 'algorithms, addiction design, and reclaiming focus'), ('Digital identity', 'who we are online vs. off, what being online gives us and costs us'), ('Paying attention to civic duty', 'what to pay attention to when considering collective good'), ('Climate grief and agency', 'living meaningfully and managing anxiety under climate change'), ('Slowness as resistance', 'deep work, deep rest, deep relationships'), ('Caregiving as a form of attention', 'Care as a human act that can only be done by humans'), ('Creative growth', 'the difference between understanding something and consuming something')]),
          ('Connection', 'v-sage', [('The loneliness epidemic', 'connection in an over-connected world'), ('Cross-generational dialogue', 'what different generations can do for each other'), ('Secular spirituality', 'ritual and meaning without religion, for the 21st Century'), ('Hope and Joy as a discipline', 'not naivety, but as a tool that helps connect us with ourselves'), ('Third places', 'the reinvention of social fabric and community infrastructure'), ('Institutional trust', 'how local, regional and national leaders are rebuilding it'), ('Death, grief, and loss', 'talking about the most taboo subjects that are also the ones we all have in common'), ('Unlikely intersections', 'where disparate fields or identities collide, and what emerges')]),
          ('Arts &amp; Culture', 'v-lilac', [('Art in the age of generation', 'the uniquely human nature of arts and cultural creativity'), ('Taste and the algorithm', 'discovery, curation, and pushing back against monoculture'), ('Storytelling as infrastructure', 'how the stories a culture tells shape what it believes is possible'), ('Who gets to make culture', 'access, gatekeeping, and the voices outside the "mainstream" narrative'), ('The economics of making', 'patronage, platforms, and what it takes to sustain a creative life'), ('Craft and the handmade', 'the growing value of slow, physical, imperfect things'), ('Arts as civic space', 'museums, venues, and libraries as places where community grows and lives')])]
h += f'<section class="page" style="font-size:8.6pt;line-height:1.35">{sec("03", "Possible topics", "examples to build from")}<p class="lede" style="font-size:10pt">Examples of topics that will be covered or explored at Human Week. This list is presented as inspiration. Feel free to take one of these topics directly or adapt it based on what inspires you.</p>'
for t, v, items in topics:
    li = ''.join(f'<p style="margin:0 0 4px"><b style="color:var(--navy)">{a}:</b> {b}</p>' for a, b in items)
    h += win(f'{t}', f'<div style="columns:2;column-gap:18px">{li}</div>', v, 'shade-navy', style='margin-bottom:9px')
h += f'{HOST_TASK}</section>'

# p5 won't list
nos = [('A pitch in a panel&#39;s clothing', 'If the real goal is selling something, host a demo. Different event, different week.', 'v-purple'),
       ('Six speakers, zero disagreement', 'Too many people with the same point of view leads to conversation without substance.', 'v-lilac'),
       ('Networking as the whole plan', '"Come mingle" isn&#39;t an event. Give people something to gather around and the mingling takes care of itself.', 'v-pink'),
       ('Ending on "any questions?"', 'Design your close like you designed your open. People should leave with something — a question, a next step, a person to follow up with.', 'v-sage'),
       ('Jargon at the door', 'If your description needs translating, the room is already smaller than it should be.', 'v-navy')]
h += f'<section class="page">{sec("04", "What we won&#39;t list", "curation means saying no")}<p class="lede">Human Week is curated. We say yes with enthusiasm and no with care, so that when you see an event on our calendar, you know it earned the spot. Here&#39;s what gets an event turned down:</p>'
for t, b, v in nos:
    h += win(t, f'<p>{b}</p>', v, 'shade-navy')
h += f'''<div class="win v-yellow shade-navy" style="background:var(--navy)"><div class="bar"><span>error.exe</span><span class="btns"><i>_</i><i>□</i><i>×</i></span></div>
<div class="wb" style="color:var(--paper);display:flex;gap:12px;align-items:center"><img src="{PX}sparkle.svg" style="width:22px;image-rendering:pixelated"><p>We turn events down for one reason: so every event we do list is worth showing up for. That&#39;s the whole promise of the week.</p></div></div>
{deco('cloud', 'width:100px;right:.6in;bottom:.75in')}{HOST_TASK}</section>'''

# p6 worksheet
ws = [('Working title', 'Use plain language.', 2, 'v-purple'),
      ('The topic or question', 'One sentence only, please. This follows the title of your event.', 2, 'v-lilac'),
      ('Who it is for', 'Written as "For anyone who…" Define your audience by how this topic shows up in their daily life. Name it; don&#39;t explain it.', 2, 'v-pink'),
      ('Your thesis', 'Why host this event, at this moment, in this way? There are no wrong answers. It&#39;s a question about the question you&#39;re asking, the coworking you&#39;re facilitating, or the activity you&#39;re leading.', 3, 'v-sage'),
      ('What people are leaving with', 'What do you want people still talking about on the way home? A question, a next step, a person to follow up with.', 2, 'v-navy')]
h += f'<section class="page">{sec("05", "Host worksheet: frame your event", "required before listing").replace("<h2>", "<h2 style=\"font-size:17pt\">")}<p class="lede">A clear frame is what makes an event worth someone&#39;s evening and tells them why they&#39;d attend. We are not collecting this worksheet, but we will ask you these questions on the host application.</p>'
for t, b, n, v in ws:
    h += win(t, f'<p>{b}</p><div class="lines">{"<div></div>" * n}</div>', v, 'shade-navy', style='margin-bottom:11px')
h += f'''<div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:4px"><span class="serif" style="font-style:italic;font-size:14pt">Let&#39;s be human, first.</span>
<span style="font-family:var(--disp);font-weight:900;text-transform:uppercase;color:var(--navy)">Human Week 2026 ✳ Boston, MA</span></div>
{HOST_TASK}</section>'''
h += '</body></html>'
open(os.path.join(OUT, 'host.html'), 'w').write(h)

# ---------------- SPONSOR GUIDE ----------------
TICK = ('LET&#39;S BE HUMAN, FIRST ✳ ROBOTS WAIT OUTSIDE ✳ BOSTON 2026 ✳ FIVE DAYS ✳ ' * 4)
TICK2 = ('HUMAN WEEK 2026 ✳ BOSTON, MA ✳ NOVEMBER 9–13 ✳ LET&#39;S BE HUMAN, FIRST ✳ ' * 4)
SP_TASK = '<div class="task" style="padding:0 .65in"><span class="start">HUMANWEEK.ORG</span><span>SPONSOR HUMAN WEEK 2026</span></div>'
s = head('landscape', 'Sponsor Human Week 2026')

s += f'''<section class="page" style="background:var(--sky)">
{deco('cloud', 'width:140px;right:.9in;top:1.6in')}{deco('cloud', 'width:90px;right:3.2in;top:3.1in')}{deco('sparkle', 'width:22px;right:2.4in;top:1.1in')}{deco('star', 'width:26px;right:1.2in;bottom:1.6in')}
<div style="display:flex;justify-content:space-between"><div class="logo">Human<br>Week</div><div class="meta">Boston, MA ✳ November 9–13, 2026</div></div>
<h1 class="display" style="font-size:62pt;margin-top:.55in">Sponsor<br><em>Human Week</em><br>2026<img src="{PX}shades.svg" style="width:1.3em;margin-left:.2em;vertical-align:.1em;image-rendering:pixelated"></h1>
<div style="width:6.2in;margin-top:.3in">{win('pro-human.txt - Notepad', '<p><span class="serif" style="font-style:italic;font-size:13pt">pro-human (adj.)</span> — putting what people need to live well ahead of what a system needs to grow.</p>', 'v-white', 'shade-navy')}</div>
<div class="ticker">{TICK}</div></section>'''

s += f'''<section class="page">{deco('sparkle', 'width:20px;left:5.3in;top:.7in')}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:.5in;align-items:center;height:100%">
<div>{sec('01', 'About Human Week', '')}
<p style="margin-top:14px">Human Week is a decentralized conference in Boston built to bring the people building technology and the people living with it into the same room.</p>
<p>Across artificial intelligence, education, the future of work, health &amp; care, cities &amp; the built environment, and social media &amp; attention, the week asks one guiding question:</p>
<p class="serif" style="font-style:italic;font-size:15pt;line-height:1.2">How do we structure society, technology, and our built environment so human needs come first?</p></div>
<div>{win('5_days.exe', '<p class="display" style="font-size:24pt">5 Days</p><p>November 9–13, 2026, across Boston</p>', 'v-purple', 'shade-navy')}
{win('official_plus_satellite.exe', '<p class="display" style="font-size:20pt">Official + Satellite</p><p>Official programming plus a growing calendar of independently hosted satellite events</p>', 'v-pink', 'shade-navy')}
{win('tracks.exe', '<p class="display" style="font-size:24pt;margin:0">6+ Tracks</p>', 'v-sage', 'shade-navy')}</div></div>{SP_TASK}</section>'''

cols = [('Intelligence', 'v-purple', ['AI and meaning', 'Neurodivergence and the myth of "normal"', 'Collective intelligence', 'Emotional intelligence in an automated world', 'The death and rebirth of expertise', 'Animal and ecological intelligence', 'Wisdom vs. information']),
        ('Attention', 'v-pink', ['Attention economy vs. connection economy', 'Building slowness in a fast paced world', 'Navigating digital identity', 'Caregiving as a form of attention to humanity', 'Attending to our civic responsibilities', 'Social media: Pros, cons and everything between', 'Climate grief, joy, and the power of nature']),
        ('Connection', 'v-sage', ['The loneliness epidemic', 'Third places', 'Cross-generational dialogue', 'Institutional trust', 'Secular spirituality', 'Death, grief, and impermanence', 'Hope as a discipline', 'Unlikely intersections']),
        ('Arts &amp; Culture', 'v-lilac', ['Art in the age of generation', 'The economics of making things real', 'Taste and the algorithm', 'Craft and handmade goods', 'Storytelling as infrastructure', 'Arts as civic space', 'Who gets to make culture'])]
s += f'<section class="page"><div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:14px"><h2 class="display" style="font-size:28pt">Topics on the table</h2><span class="serif" style="font-style:italic;font-size:14pt">A sample of what hosts will explore</span></div><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">'
for t, v, items in cols:
    s += win(t, '<ul class="bul">' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>', v, 'shade-navy', style='height:5.6in')
s += f'</div>{SP_TASK}</section>'

why = [('An audience looking for authenticity and principles', 'Our audience at Human Week is not anti-technology. We are simply pro-human. What this means is that we are seeking brands and companies that understand technologies, policies, and standards can be adopted to support human well-being, rather than detracting from it.'),
       ('Citywide visibility', 'Sponsorship covers the full week of official programming across all five days of Human Week. This provides you with brand visibility across the whole city, not just a single event.</p><p>Brands that help make Human Week happen will be putting a flag in the ground and taking a very popular stance in favor of pro-human principles.'),
       ('A real conversation', 'Real conversations about tech and humanity, not a trade show. Sponsors support the conversation, and every host starts with a real question and takes a clear stance.</p><p>We are working diligently to prevent "event slop," meaning your brand will benefit from being the face of fewer, higher quality events.')]
s += f'<section class="page" style="background:var(--navy);color:var(--paper)">{deco("sparkle", "width:20px;right:.8in;top:.7in")}{deco("star", "width:24px;left:.5in;bottom:.6in")}<div class="sec"><span class="num">02</span><h2 style="color:var(--paper)">Why sponsor the week</h2></div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:16px">'
for t, b in why:
    s += win(t.lower().replace(' ', '_')[:30] + '.txt', f'<p style="font-family:var(--disp);font-weight:900;text-transform:uppercase;color:var(--navy);font-size:14pt;line-height:1.05">{t}</p><p style="color:var(--body)">{b}</p>', 'v-blue', 'shade-yellow', style='height:5.4in')
s += '</div><p class="serif" style="font-style:italic;text-align:center;color:var(--lilac);font-size:14pt;margin-top:8px">Not anti-tech. Pro-human.</p></section>'

tiers = [('Title Partner', '$75,000', 'Limit: 1', 'v-purple'), ('Week Partner', '$30,000', 'Limit: 3', 'v-lilac'), ('Program Partner', '$10,000', 'Limit: 12', 'v-pink'), ('Community Partner', '$2,500', 'Open', 'v-sage'), ('In-Kind Partner', 'Value-based', 'By arrangement', 'v-navy')]
s += f'<section class="page">{sec("03", "Sponsorship tiers", "")}<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-top:1.3in">'
for t, p, l, v in tiers:
    s += win(t.split()[0].lower() + '.exe', f'<p class="display" style="font-size:13pt;line-height:1">{t}</p><p class="display" style="font-size:{17 if p[0]=="$" else 12}pt;color:var(--purple);margin:10px 0 6px">{p}</p><p class="meta" style="font-size:6.5pt">{l}</p>', v, 'shade-navy')
s += f'</div>{deco("cloud", "width:120px;right:.8in;bottom:.9in")}{deco("sparkle", "width:20px;left:1in;top:4.6in")}{SP_TASK}</section>'

title_b = ['Exclusive naming rights across the week', 'Top billing on humanweek.org, the week&#39;s schedule, and all citywide materials', 'Opening remarks at Kick-Off Night and closing remarks at the Closing Party', 'Right of first refusal on Title Partnership for Human Week 2027', 'Logo presence at every official programming event across all five days', 'Dedicated feature across Human Week&#39;s social and email channels', 'Full post-week attendance and engagement report']
s += f'''<section class="page" style="background:var(--purple);color:var(--paper)">{deco('sparkle', 'width:22px;left:.7in;top:.8in')}{deco('star', 'width:24px;left:3.6in;bottom:1in')}
<div style="display:grid;grid-template-columns:1fr 1.25fr;gap:.5in;align-items:center;height:100%">
<div><p class="meta" style="color:var(--sky)">Limit: 1</p><h2 class="display" style="font-size:52pt;color:var(--paper);text-shadow:-4px 4px 0 var(--navy)">Title<br>Partner</h2>
<p class="display" style="font-size:26pt;color:var(--yellow);margin:12px 0">$75,000</p>
<p class="serif" style="font-style:italic;color:var(--pink);font-size:13pt">“Human Week 2026, presented by [Sponsor]”</p></div>
<div>{win('title_partner_benefits.txt', '<ul class="bul">' + ''.join(f'<li>{x}</li>' for x in title_b) + '</ul>', 'v-white', 'shade-navy')}</div></div></section>'''

pt = [('Week Partner', '$30,000', 'v-lilac', ['Logo on humanweek.org and the week&#39;s official schedule', 'Verbal recognition at official programming events', 'Dedicated social media feature', 'Reserved seating across official programming events', 'Named recognition in the post-week summary report']),
      ('Program Partner', '$10,000', 'v-pink', ['Logo on humanweek.org and the week&#39;s official schedule', 'Shared social media mention', 'Reserved seating at select official programming events']),
      ('Community Partner', '$2,500', 'v-sage', ['Logo on humanweek.org&#39;s partner listing', 'Recognition in the week&#39;s program and closing materials'])]
s += f'<section class="page"><h2 class="display" style="font-size:28pt;margin-bottom:.45in">Partner tiers</h2><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px;align-items:start">'
for i, (t, p, v, items) in enumerate(pt):
    s += win(t.lower().replace(' ', '_') + '.txt', f'<p class="display" style="font-size:16pt">{t}</p><p class="display" style="font-size:20pt;color:var(--purple);margin:6px 0 10px">{p}</p><ul class="bul">' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>', v, 'shade-navy', style=f'margin-top:{i*0.35}in')
s += f'</div>{deco("cloud", "width:110px;left:.8in;bottom:.9in")}{SP_TASK}</section>'

ik = ['For venue, catering, A/V, printing, or other donations in lieu of cash', 'Benefits scaled to match the equivalent cash tier', 'Logo placement matched to contribution value']
s += f'''<section class="page">{deco('sparkle', 'width:20px;left:4.6in;top:1.4in')}
<div style="display:grid;grid-template-columns:1fr 1.2fr;gap:.5in;align-items:center;height:100%">
<div><p class="meta" style="color:var(--purple)">By arrangement</p><h2 class="display" style="font-size:52pt">In-Kind<br><em>Partner</em></h2><p class="display" style="font-size:18pt;margin-top:12px">Value-based</p></div>
<div>{win('in_kind_partner.txt', '<ul class="bul">' + ''.join(f'<li>{x}</li>' for x in ik) + '</ul>', 'v-navy', '')}</div></div>{SP_TASK}</section>'''

s += f'''<section class="page" style="background:var(--navy);color:var(--paper)">{deco('star', 'width:24px;right:1in;top:1in')}{deco('sparkle', 'width:20px;left:1in;bottom:1.2in')}
<div style="display:flex;flex-direction:column;justify-content:center;height:100%;max-width:8.6in">
{win('how_sponsorship_works.txt', '<p class="display" style="font-size:26pt;margin-bottom:12px">How sponsorship works</p><p>Sponsors are held to the same standard as every host: support the conversation, don&#39;t own it. Sponsorship doesn&#39;t include editorial control over speakers or content, and stage time connects to each event&#39;s topic and purpose.</p><p class="serif" style="font-style:italic;font-size:13pt;margin-top:8px">Editorial independence is what makes the audience show up and trust Human Week Events. This is how we will protect our brand and yours.</p>', 'v-purple', 'shade-yellow')}
</div></section>'''

s += f'''<section class="page" style="background:var(--sky);text-align:center">
{deco('cloud', 'width:130px;left:.9in;top:1in')}{deco('cloud', 'width:100px;right:1in;top:1.6in')}{deco('sparkle', 'width:22px;left:2.6in;bottom:2in')}{deco('star', 'width:26px;right:2.4in;bottom:1.6in')}
<div style="display:flex;flex-direction:column;justify-content:center;align-items:center;height:100%">
<h2 class="display" style="font-size:50pt">Let&#39;s partner on<br><em>the week</em></h2>
<p style="margin:18px 0 22px;color:var(--navy)">Partnerships start at $2,500. Custom arrangements welcome if the standard tiers don&#39;t fit.</p>
<div style="display:flex;gap:18px">
<span style="font-family:var(--disp);font-weight:800;text-transform:uppercase;background:var(--yellow);color:var(--navy);border:2.5px solid var(--navy);box-shadow:4px 4px 0 var(--navy);padding:10px 22px">humanweek.org</span>
<span style="font-family:var(--disp);font-weight:800;background:var(--paper);color:var(--navy);border:2.5px solid var(--navy);box-shadow:4px 4px 0 var(--navy);padding:10px 22px">hello@humanweek.org</span></div></div>
<div class="ticker">{TICK2}</div></section>'''
s += '</body></html>'
open(os.path.join(OUT, 'sponsor.html'), 'w').write(s)
print('ok')
