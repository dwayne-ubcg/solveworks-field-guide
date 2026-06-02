from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from pathlib import Path
import textwrap

OUT = Path('/Users/macmini/openclaw/solveworks-site/proposals/solveworks-company-brain-brief.pdf')
W, H = letter
M = 0.62 * inch
NAVY = colors.HexColor('#071321')
NAVY2 = colors.HexColor('#0D2235')
INK = colors.HexColor('#0F2236')
CYAN = colors.HexColor('#0EA5E9')
CYAN2 = colors.HexColor('#38BDF8')
PALE = colors.HexColor('#F2F8FC')
WHITE = colors.white
MUTED_D = colors.HexColor('#D7E7F2')
MUTED_L = colors.HexColor('#40586D')
LINE = colors.HexColor('#C8DCE8')


def meta(c):
    c.setTitle('SolveWorks Company Brain Brief')
    c.setAuthor('SolveWorks')
    c.setSubject('Pre-call briefing on Company Brain systems and agentic workflows')
    c.setCreator('SolveWorks')


def bg(c, dark=True, section=''):
    c.setFillColor(NAVY if dark else PALE)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(colors.Color(0.05, 0.65, 0.91, alpha=0.12 if dark else 0.08))
    c.circle(W*.16, H*.9, 110, fill=1, stroke=0)
    c.setFillColor(colors.Color(0.13, 0.77, 0.43, alpha=0.055 if dark else 0.045))
    c.circle(W*.92, H*.12, 96, fill=1, stroke=0)
    c.setFont('Helvetica-Bold', 22)
    c.setFillColor(WHITE if dark else INK)
    c.drawString(M, H-M+6, 'Solve')
    c.setFillColor(CYAN2)
    c.drawString(M+50, H-M+6, 'Works')
    c.setFont('Helvetica-Bold', 8.8)
    c.setFillColor(CYAN2)
    c.drawRightString(W-M, H-M+12, section.upper())
    c.setFont('Helvetica', 8.0)
    c.setFillColor(colors.HexColor('#8AA2B7') if dark else colors.HexColor('#6A8195'))
    c.drawString(M, .34*inch, 'SOLVEWORKS.IO')
    c.drawRightString(W-M, .34*inch, 'COMPANY BRAIN SYSTEMS')


def wrap(c, text, x, y, width, font='Helvetica', size=12, leading=16, color=WHITE):
    c.setFont(font, size)
    c.setFillColor(color)
    chars = max(18, int(width/(size*.49)))
    for para in str(text).split('\n'):
        for line in textwrap.wrap(para, width=chars) or ['']:
            c.drawString(x, y, line)
            y -= leading
        y -= leading*.20
    return y


def eyebrow(c, text, x, y):
    c.setFont('Helvetica-Bold', 9.5)
    c.setFillColor(CYAN)
    c.drawString(x, y, text.upper())
    return y - 30


def title(c, text, x, y, width, dark=True, size=39):
    return wrap(c, text, x, y, width, 'Helvetica-Bold', size, size*1.06, WHITE if dark else INK)


def body(c, text, x, y, width, dark=True, size=15.4):
    return wrap(c, text, x, y, width, 'Helvetica', size, size+5, MUTED_D if dark else MUTED_L)


def takeaway(c, text, x, y, width, dark=True, size=18):
    return wrap(c, text, x, y, width, 'Helvetica-Bold', size, size+5, WHITE if dark else INK)


def card(c, x, y, w, h, head, copy='', label='', dark=True, head_size=14.8, copy_size=12.2):
    c.setFillColor(NAVY2 if dark else WHITE)
    c.setStrokeColor(colors.HexColor('#337B9A') if dark else LINE)
    c.roundRect(x, y-h, w, h, 15, fill=1, stroke=1)
    yy = y - 18
    if label:
        c.setFont('Helvetica-Bold', 7.8)
        c.setFillColor(CYAN2 if dark else CYAN)
        c.drawString(x+15, yy, label.upper())
        yy -= 15
    yy = wrap(c, head, x+15, yy, w-30, 'Helvetica-Bold', head_size, head_size+3, WHITE if dark else INK)
    if copy:
        wrap(c, copy, x+15, yy+1, w-30, 'Helvetica', copy_size, copy_size+3.8, MUTED_D if dark else MUTED_L)


def two_cards(c, items, y, dark=True, h=1.62*inch):
    for i, (head, copy, label) in enumerate(items):
        card(c, M + i*3.92*inch, y, 3.55*inch, h, head, copy, label, dark)


def numbered(c, n, head, copy, x, y, dark=True, w=3.25*inch):
    c.setFillColor(CYAN)
    c.roundRect(x, y-.31*inch, .38*inch, .38*inch, 8, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont('Helvetica-Bold', 11)
    c.drawCentredString(x+.19*inch, y-.19*inch, str(n))
    yy = wrap(c, head, x+.52*inch, y, w-.52*inch, 'Helvetica-Bold', 13.4, 16.5, WHITE if dark else INK)
    wrap(c, copy, x+.52*inch, yy+1, w-.52*inch, 'Helvetica', 10.6, 14.2, MUTED_D if dark else MUTED_L)


c = canvas.Canvas(str(OUT), pagesize=letter)
meta(c)

# 1 Cover
bg(c, True, 'Pre-call briefing')
y = H - 1.78*inch
y = title(c, 'The head start your agent gets the day SolveWorks builds it.', M, y, 7.1*inch, True, 43)
y = body(c, 'Most businesses do not need another chatbot. They need an agent that understands the work: the sources, rules, approvals, tools, and corrections that make execution safe.', M, y-8, 6.95*inch, True, 16.2)
card(c, M, 2.60*inch, 7.30*inch, 1.32*inch, 'We build the Company Brain around the agent.', 'Context layer. Workflow rules. Permission model. Skillset Packs. QA checks. Execution surfaces.', 'What sets SolveWorks apart', True, 15.4, 11.8)
c.showPage()

# 2 Problem
bg(c, False, 'Why agents stall')
y = H - 1.22*inch
y = eyebrow(c, 'The hard lesson', M, y)
y = title(c, 'The model is rarely the whole problem.', M, y, 7*inch, False, 36)
y = body(c, 'Every real agent build since December has confirmed one thing: a better prompt does not fix a broken operating layer.', M, y-4, 6.95*inch, False, 16.2)
two_cards(c, [('Cold starts','The agent wakes up without the right call notes, SOPs, dashboard definitions, CRM history, or priorities.',''), ('No source of truth','It cannot know whether the spreadsheet, dashboard, transcript, old SOP, or correction should win.','')], 5.05*inch, False, 1.52*inch)
two_cards(c, [('Unsafe permissions','Nobody has defined what the agent can read, draft, send, change, or escalate.',''), ('Lost corrections','Humans correct the same mistake again because feedback never becomes a reusable rule.','')], 3.15*inch, False, 1.52*inch)
takeaway(c, 'SolveWorks fixes the operating layer first, then gives the agent room to execute.', M, 1.25*inch, 6.95*inch, False, 17.5)
c.showPage()

# 3 Difference
bg(c, True, 'The SolveWorks difference')
y = H - 1.22*inch
y = eyebrow(c, 'Not a chatbot install', M, y)
y = title(c, 'We build agents like operators, not demos.', M, y, 7*inch, True, 36)
y = body(c, 'A useful business agent needs more than model access. It needs trusted context, scoped tools, approval gates, feedback loops, logs, QA, and a way to improve after every correction.', M, y-4, 6.95*inch, True, 15.2)
items=[('Company Brain','Map the business context the agent needs before it acts.'),('Skillset Packs','Package how the company does recurring work.'),('Execution Surfaces','Turn work into briefs, dashboards, drafts, watchdogs, and queues.'),('Safety + Receipts','Start safe, log what happened, and expand only after verification.')]
y=4.85*inch
for h,b in items:
    card(c, M, y, 7.30*inch, .70*inch, h, b, '', True, 14.2, 11.4)
    y -= .84*inch
c.showPage()

# 4 Company Brain intro
bg(c, False, 'Company Brain layer')
y = H - 1.22*inch
y = eyebrow(c, 'The foundation', M, y)
y = title(c, 'The agent starts smarter because the brain is designed.', M, y, 7*inch, False, 36)
y = body(c, 'We do not dump the whole company into a prompt. We design the layers that let an agent retrieve the right context and respect the business rules.', M, y-4, 6.95*inch, False, 15.4)
card(c, M, 4.62*inch, 7.30*inch, 1.35*inch, 'The Company Brain is the operating layer between scattered business knowledge and useful agent execution.', 'It defines what the agent should know, which source to trust, what it is allowed to do, and how corrections improve the next run.', '', False, 16, 12)
takeaway(c, 'This is the difference between an agent that impresses in a demo and one that earns a place in daily operations.', M, 2.35*inch, 6.95*inch, False, 18)
c.showPage()

# 5 Six layers A
bg(c, True, 'Company Brain layer')
y = H - 1.25*inch
y = eyebrow(c, 'Six layers, part one', M, y)
y = title(c, 'First: capture the work and retrieve the right context.', M, y, 7*inch, True, 34)
y = body(c, 'The agent should not start cold, and it should not be flooded with everything. It needs the right facts for the job in front of it.', M, y-4, 6.95*inch, True, 15.2)
three=[('Capture','Calls, SOPs, docs, dashboards, CRM notes, decisions, corrections.','01'),('Retrieval','Only the facts needed for the job, not a noisy memory dump.','02'),('Source Truth','Rules for which system wins when data conflicts.','03')]
yc=4.72*inch
for i,(h,b,l) in enumerate(three):
    card(c, M+i*2.50*inch, yc, 2.25*inch, 1.58*inch, h, b, l, True, 13.8, 11.7)
c.showPage()

# 6 Six layers B
bg(c, False, 'Company Brain layer')
y = H - 1.25*inch
y = eyebrow(c, 'Six layers, part two', M, y)
y = title(c, 'Then: set boundaries, learn from corrections, and execute.', M, y, 7*inch, False, 34)
y = body(c, 'This is where the agent becomes safer and more useful. Permissions are explicit, feedback becomes reusable, and outputs move into the tools the business actually uses.', M, y-4, 6.95*inch, False, 15.2)
three=[('Permissions','What the agent can read, draft, send, change, or escalate.','04'),('Feedback Loops','Corrections become future rules, not lost chat threads.','05'),('Execution','Briefs, dashboards, follow-ups, watchdogs, tasks, and approvals.','06')]
yc=4.72*inch
for i,(h,b,l) in enumerate(three):
    card(c, M+i*2.50*inch, yc, 2.25*inch, 1.58*inch, h, b, l, False, 13.8, 11.7)
c.showPage()

# 7 Skillset Packs
bg(c, True, 'Skillset Packs')
y = H - 1.22*inch
y = eyebrow(c, 'How agents learn the work', M, y)
y = title(c, 'We package the way your company actually does the job.', M, y, 7*inch, True, 35)
y = body(c, 'The strongest agents do not rely on vague instructions. They run on reusable operating knowledge: decisions, checks, commands, and examples.', M, y-4, 6.95*inch, True, 15.2)
two_cards(c, [('Rules','How to decide, what to avoid, when to escalate, and which source is trusted.','Included'), ('Runbooks','The step-by-step operating pattern for repeatable workflows.','Included')], 4.90*inch, True, 1.56*inch)
two_cards(c, [('QA checks','Tests, review gates, leakage scans, and receipts before work is trusted.','Included'), ('Tool commands','Safe ways the agent reads, drafts, checks, reports, and operates systems.','Included')], 3.03*inch, True, 1.56*inch)
takeaway(c, 'Our builds are designed to compound: each workflow makes the next one faster to stand up and easier to improve.', M, 1.22*inch, 6.95*inch, True, 17)
c.showPage()

# 8 Where start
bg(c, False, 'Where to start')
y=H-1.22*inch
y=eyebrow(c, 'The first useful win', M, y)
y=title(c, 'Start where the team keeps re-explaining the work.', M, y, 7*inch, False, 35)
y=body(c, 'The goal is not “AI everywhere.” The goal is one workflow where context, judgment, and follow-through keep slowing the business down every week.', M, y-4, 6.95*inch, False, 15.2)
card(c, M, 4.70*inch, 7.30*inch, 1.32*inch, 'The best first workflow has three traits.', 'It repeats often. It depends on context. It benefits from a human approval step before action.', '', False, 16, 12)
takeaway(c, 'The starting point is practical: read-only or draft-only first, then approval-gated action once the workflow is proven.', M, 2.38*inch, 6.95*inch, False, 18)
c.showPage()

# 9 Workflow examples
bg(c, True, 'Workflow examples')
y=H-1.25*inch
y=eyebrow(c, 'Common first pilots', M, y)
y=title(c, 'Useful agents usually start with ordinary recurring work.', M, y, 7*inch, True, 34)
two_cards(c, [('Sales follow-up','Call summary, buyer pain, next steps, CRM note, approved follow-up draft.',''), ('Owner briefing','Calendar, inbox, dashboard exceptions, priorities, risks, and decisions.','')], 5.10*inch, True, 1.45*inch)
two_cards(c, [('Dashboard analyst','Freshness checks, KPI explanations, anomalies, and recommended actions.',''), ('Ops watchdog','Recurring checks, stale tasks, order/inventory exceptions, and escalations.','')], 3.28*inch, True, 1.45*inch)
c.showPage()

# 10 Discovery A
bg(c, False, 'Discovery call')
y=H-1.25*inch
y=eyebrow(c, 'Before proposing', M, y)
y=title(c, 'A strong agent is scoped before it is built.', M, y, 7*inch, False, 35)
y=body(c, 'The call is not a generic demo. We map the workflow, sources, decisions, permissions, and risk boundaries so the proposal is specific.', M, y-4, 6.95*inch, False, 15.2)
numbered(c, 1, 'What work repeats every week?', 'Find the workflow with the fastest practical return.', M, 4.55*inch, False, 3.25*inch)
numbered(c, 2, 'Which systems does it depend on?', 'Identify the calls, docs, dashboards, CRM, inboxes, and tools.', M+3.90*inch, 4.55*inch, False, 3.25*inch)
numbered(c, 3, 'Which source should win?', 'Define source truth before the agent trusts bad data.', M, 3.02*inch, False, 3.25*inch)
c.showPage()

# 11 Discovery B
bg(c, True, 'Discovery call')
y=H-1.25*inch
y=eyebrow(c, 'Before proposing', M, y)
y=title(c, 'We also define what the agent should not do.', M, y, 7*inch, True, 35)
y=body(c, 'Good scoping protects the business. We decide what stays human-approved, what repeated mistakes become rules, and what first output would be useful immediately.', M, y-4, 6.95*inch, True, 15.2)
numbered(c, 4, 'What must stay human-approved?', 'Set the permission ladder and escalation rules.', M, 4.55*inch, True, 3.25*inch)
numbered(c, 5, 'What mistakes repeat?', 'Turn recurring corrections into rules and QA checks.', M+3.90*inch, 4.55*inch, True, 3.25*inch)
numbered(c, 6, 'What output would be useful tomorrow?', 'Pick the first brief, draft, dashboard, task list, or watchdog.', M, 3.02*inch, True, 3.25*inch)
c.showPage()

# 12 Head start
bg(c, False, 'The head start')
y=H-1.22*inch
y=eyebrow(c, 'What a SolveWorks build gives the agent', M, y)
y=title(c, 'Your agent does not start from a blank chat box.', M, y, 7*inch, False, 35)
y=body(c, 'The first build is not just access to a model. It is a working operating package around the agent so it knows the job, tools, boundaries, and definition of done.', M, y-4, 6.95*inch, False, 15.2)
two_cards(c, [('Brain map','Sources, decisions, and context the workflow depends on.',''), ('Skillset Pack','Rules, prompts, runbooks, examples, checks, and escalation paths.','')], 4.88*inch, False, 1.35*inch)
two_cards(c, [('Tool bench','Safe ways to read, draft, report, summarize, check, and queue work.',''), ('QA receipts','Tests, launch checks, logs, and proof before permissions expand.','')], 3.18*inch, False, 1.35*inch)
takeaway(c, 'This is the head start: the agent begins with operating knowledge, not guesswork.', M, 1.30*inch, 6.95*inch, False, 18)
c.showPage()

# 13 Bio
bg(c, True, 'About SolveWorks')
y=H-1.22*inch
y=eyebrow(c, 'Brief bio', M, y)
y=title(c, 'SolveWorks builds practical AI agents for real business workflows.', M, y, 7*inch, True, 34)
y=body(c, 'We help owner-led companies turn scattered knowledge, repeated decisions, and manual follow-through into agent-assisted operating systems.', M, y-4, 6.95*inch, True, 15.2)
two_cards(c, [('What we do','Build purpose-built agents, dashboards, briefs, watchdogs, and workflow tools.',''), ('How we work','Start with one useful workflow, map the sources and approvals, then launch safely.','')], 4.92*inch, True, 1.55*inch)
two_cards(c, [('What makes it different','The agent gets a Company Brain, Skillset Pack, tool bench, permission ladder, and feedback loop.',''), ('Who it is for','Business owners and operators who want AI help with follow-up, reporting, research, dashboards, admin, and recurring operations.','')], 3.03*inch, True, 1.55*inch)
c.showPage()

# 14 Close
bg(c, False, 'After the call')
y=H-1.22*inch
y=eyebrow(c, 'What happens next', M, y)
y=title(c, 'When there is a fit, we send a specific proposal.', M, y, 7*inch, False, 35)
y=body(c, 'The proposal is built around the workflow we mapped together. It defines what the agent reads, what it produces, what needs approval, and how we verify that it works.', M, y-4, 6.95*inch, False, 15.2)
two_cards(c, [('Operating model','Sources, source-truth rules, permission ladder, escalation path.',''), ('Working artifacts','Agent workflows, briefs or dashboards, runbooks, QA checks, receipts.','')], 4.88*inch, False, 1.35*inch)
two_cards(c, [('Launch posture','Safe first: read-only or draft-only before approved action.',''), ('Compounding value','Each correction improves the brain instead of disappearing in chat.','')], 3.18*inch, False, 1.35*inch)
takeaway(c, 'A useful agent is the model plus the business context, trust rules, permissions, skillsets, tools, QA, and feedback loops around it.', M, 1.30*inch, 6.95*inch, False, 17.2)
c.showPage()

c.save()
print(OUT)
