from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether)

BROWN = colors.HexColor("#8B5E3C")
CREAM = colors.HexColor("#FBF4EA")
DARK = colors.HexColor("#3A2A1E")

ss = getSampleStyleSheet()
title = ParagraphStyle("t", parent=ss["Title"], fontSize=34, leading=40, textColor=BROWN, spaceAfter=10)
tagline = ParagraphStyle("tag", parent=ss["Normal"], fontSize=14, alignment=1,
                         textColor=DARK, fontName="Helvetica-Oblique", spaceAfter=20)
h1 = ParagraphStyle("h1", parent=ss["Heading1"], textColor=BROWN, fontSize=18, spaceBefore=10)
h2 = ParagraphStyle("h2", parent=ss["Heading2"], textColor=DARK, fontSize=13, spaceBefore=8)
body = ParagraphStyle("b", parent=ss["Normal"], fontSize=10.5, leading=15, textColor=DARK,
                      spaceAfter=6)
small = ParagraphStyle("s", parent=body, fontSize=9, leading=12, textColor=colors.HexColor("#6b5a4c"))
cell = ParagraphStyle("c", parent=body, fontSize=9.5, leading=13, spaceAfter=0)
cellb = ParagraphStyle("cb", parent=cell, fontName="Helvetica-Bold")


def P(t, s=body):
    return Paragraph(t, s)


def table(rows, widths):
    data = [[P(c, cellb if i == 0 else cell) for c in r] for i, r in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), CREAM),
        ("LINEBELOW", (0, 0), (-1, 0), 1, BROWN),
        ("LINEBELOW", (0, 1), (-1, -1), 0.25, colors.HexColor("#d9c8b4")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#8a7a6c"))
    canvas.drawString(20 * mm, 12 * mm, "Boxbnb - Company Profile")
    canvas.drawRightString(190 * mm, 12 * mm, f"Page {doc.page}")
    canvas.restoreState()


s = []

# ---------- Cover / intro ----------
s += [Spacer(1, 30 * mm), P("BOXBNB", title),
      P("Find your box. Ignore your human.", tagline),
      P("Company Profile", ParagraphStyle("cp", parent=h2, alignment=1)),
      Spacer(1, 10 * mm)]

s += [P("Who We Are", h1),
      P("Boxbnb is the world's leading short-stay rental platform for cats. We connect discerning "
        "cats with premium resting spots: cardboard boxes, sunbeams, laptop keyboards, freshly folded "
        "laundry, and the exact spot a human was about to sit in."),
      P("Comfort is easy. Any cat can find a soft cushion. Boxbnb exists for cats who want more: a resting "
        "spot that is warm, enclosed, and actively ruining someone's afternoon. We believe that is not "
        "a luxury. It is a right.")]

s += [P("Our Story", h1),
      P("Boxbnb was founded on a sunny third-floor windowsill by three cats. Our founder, Princess "
        "Consuela Bananhammock (Banana for short), had spent four days claiming a perfect delivery box when her human recycled it "
        "without notice. She did not get angry. She got organized."),
      P("Within a week she had recruited Ashe Burrito, a specialist in strategic inconvenience, and "
        "Ivy-BeanBun, who had personally sat in more boxes than any cat on record. Together they built a "
        "platform that lists every box, sunbeam, and warm surface in the household, rates it by how much "
        "it inconveniences the nearest human, and lets cats book it for a fee paid in treats."),
      P("Customer support was added later, by accident. See <i>Our Team</i>.")]

s += [P("Mission", h1),
      P("To give every cat access to a resting spot that is warm, enclosed, and as inconvenient as possible "
        "for the nearest human.")]

s += [P("What Makes Us Different", h1),
      P("<b>The Inconvenience Guarantee.</b> Every Boxbnb listing is certified Maximally Inconvenient by our "
        "Head of Inconvenience Strategy. If your human is not at least mildly annoyed by your stay, your "
        "next night is free."),
      P("<b>Treat-based pricing.</b> No cards, no cash, no subscriptions. All stays are paid in treats."),
      P("<b>No schedules.</b> Check in whenever. Check out whenever. Leave halfway through. We understand.")]

s.append(PageBreak())

# ---------- Listings ----------
s += [P("Listings and Pricing", h1),
      P("All prices are in treats. Prices are fixed and are not negotiable, no matter how long you stare.", small)]

s += [P("Box Stays (per night)", h2),
      table([["Listing", "Price", "Description"],
             ["Shoebox Studio", "2 treats", "Cozy, snug, slightly too small. Guests love it anyway. "
              "Best for cats who enjoy spilling over the edges."],
             ["Prime Location Box", "5 treats", "A standard delivery box. Our most popular listing. "
              "Usually placed in the middle of the hallway."],
             ["Fridge Box Penthouse", "12 treats", "Spacious and multi-level once you chew a door into it. "
              "Limited availability: appears only when a human buys a large appliance."]],
            [42 * mm, 22 * mm, 106 * mm])]

s += [P("Sunbeam Timeshares (per hour)", h2),
      table([["Listing", "Price", "Description"],
             ["Living Room Sunbeam", "3 treats/hour", "Available 2pm to 4pm only. Moves slowly across the "
              "floor; guests are expected to follow it."],
             ["Bedroom Sunbeam", "2 treats/hour", "Mornings only. Lands directly on the human's pillow."]],
            [42 * mm, 26 * mm, 102 * mm]),
      Spacer(1, 3),
      P("All sunbeams are subject to clouds. No refunds for weather.", small)]

s += [P("Premium Inconvenience Listings (per session)", h2),
      table([["Listing", "Price", "Description"],
             ["Keyboard Suite", "8 treats", "A warm laptop keyboard. Guaranteed to be booked during your "
              "human's deadlines."],
             ["Fresh Laundry Pile", "6 treats", "Warm and clean. Dark clothing preferred for maximum fur "
              "visibility."],
             ["The Doorway", "4 treats", "Stand halfway in, halfway out. Do not commit to either side."],
             ["Human's Chair (still warm)", "7 treats", "Must be booked the moment the human gets up."]],
            [42 * mm, 22 * mm, 106 * mm])]

s += [P("Add-ons", h2),
      table([["Add-on", "Price", "Description"],
             ["4AM Wake-Up Service", "3 treats", "A gentle paw to the human's face, repeated until results."],
             ["Glass Edge Package", "5 treats", "Includes one full glass of water placed near a table edge."],
             ["Video Call Cameo", "4 treats", "Walk across the screen during an important meeting."]],
            [42 * mm, 22 * mm, 106 * mm])]

s.append(PageBreak())

# ---------- Policies ----------
s += [P("Policies", h1),
      P("<b>Check-in and check-out:</b> whenever. We do not believe in schedules."),
      P("<b>Cancellation:</b> we don't care."),
      P("<b>Recycling Day Clause:</b> Boxbnb is not responsible if your human recycles your box during your "
        "stay. No refunds."),
      P("<b>The bathtub:</b> the bathtub listing is decorative and cannot be booked. Do not ask."),
      P("<b>Guests:</b> Boxbnb is for cats. Dogs are not permitted as guests."),
      P("<b>Payment:</b> treats only, paid at check-in. Half-eaten treats are not accepted."),
      P("<b>Complaints from humans:</b> humans may file complaints about a stay. All complaints are logged. "
        "None are acted upon.")]

# ---------- FAQ ----------
s += [P("Frequently Asked Questions", h1)]
faq = [
    ("How do I book a stay?", "Leave your name and email with customer support and tell us which listing you "
     "want. Our team will confirm your booking when they wake up."),
    ("Can I book a listing that is already occupied?", "Yes, but you will need to resolve it with the current "
     "guest yourself. Boxbnb does not mediate."),
    ("What if my box gets recycled?", "See the Recycling Day Clause. We are sorry. Not sorry enough to refund you."),
    ("Is the Inconvenience Guarantee real?", "Yes. If your human is not at least mildly annoyed, your next "
     "night is free. Annoyance is assessed by Ashe Burrito."),
    ("I am a human. Can I book a stay?", "No. You can, however, file a complaint."),
    ("Why does customer support sound sad?", "That is not something we can comment on."),
]
for q, a in faq:
    s.append(KeepTogether([P(f"<b>{q}</b>"), P(a)]))

s.append(PageBreak())

# ---------- Team ----------
s += [P("Our Team", h1)]
team = [
    ("Princess Consuela Bananhammock", "Founder &amp; CEO",
     "A Persian who sleeps 20 hours a day and calls it strategic vision. Founded Boxbnb after a box she had "
     "claimed was recycled without warning. Has not attended a meeting since 2023 but is copied on all of them."),
    ("Ashe Burrito", "Head of Inconvenience Strategy",
     "Black shorthair. Personally tests every Premium Inconvenience Listing before it goes live. Has knocked "
     "over 4,000 glasses in his career and designed the Glass Edge Package from personal experience."),
    ("Ivy-BeanBun", "Head of Box Acquisitions",
     "Tabby. Inspects every new box by sitting in it for six hours. Has rejected boxes for being too clean, "
     "too new, and smelling too much like the recycling bin."),
    ("Bob", "Customer Support Associate",
     "Golden retriever. Hired by mistake. The job posting asked for someone who can sit, stay, and handle "
     "complaints, and Bob was the only applicant who could sit and stay on command. Nobody has fired him "
     "because firing him would require filling out a form, and nobody can be bothered. Bob is paid in dry "
     "biscuits. The cats ignore him. He is required to sell products designed to inconvenience humans, whom "
     "he loves very much. He does his job correctly. He is not happy about it."),
]
for name, role, bio in team:
    s.append(KeepTogether([P(name, h2), P(f"<i>{role}</i>", small), P(bio)]))

s += [P("Contact", h1),
      P("Bookings: bookings@boxbnb.example"),
      P("Customer support is available 24/7, because Bob is not allowed to leave.")]

doc = SimpleDocTemplate("about_business.pdf", pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm,
                        topMargin=20 * mm, bottomMargin=20 * mm, title="Boxbnb - Company Profile",
                        author="Boxbnb")
doc.build(s, onFirstPage=footer, onLaterPages=footer)
print("ok")
