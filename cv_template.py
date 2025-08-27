from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# Output file
output_path = "DeniHyseniCV_Template.pdf"

# Page setup
width, height = A4
sidebar_width = 2.2 * inch

c = canvas.Canvas(output_path, pagesize=A4)

# Sidebar background
c.setFillColorRGB(0.93, 0.93, 0.93)  # light gray
c.rect(0, 0, sidebar_width, height, fill=1, stroke=0)

# Header (Name in top center)
c.setFont("Helvetica-Bold", 20)
c.setFillColorRGB(0, 0, 0)
c.drawCentredString((width + sidebar_width) / 2, height - 50, "Deni Hyseni")

# -------------------------
# SIDEBAR CONTENT
# -------------------------
c.setFont("Helvetica-Bold", 12)
c.setFillColorRGB(0, 0.3, 0.6)
c.drawString(20, height - 100, "Contact")

c.setFont("Helvetica", 10)
c.setFillColorRGB(0, 0, 0)
sidebar_y = height - 120

contact_info = [
    ("Email:", "deni.hyseni@gmail.com"),
    ("Phone:", "+383 49 238 823"),
    ("Location:", "Prishtina, Kosovo"),
    ("GitHub:", "github.com/denihyseni/python-journey"),
    ("LinkedIn:", "linkedin.com/in/deni-hyseni-734712273/")
]

for label, value in contact_info:
    c.drawString(20, sidebar_y, f"{label} {value}")
    sidebar_y -= 16

# Technical Skills
c.setFont("Helvetica-Bold", 12)
c.setFillColorRGB(0, 0.3, 0.6)
c.drawString(20, sidebar_y - 10, "Technical Skills")

c.setFont("Helvetica", 10)
c.setFillColorRGB(0, 0, 0)
skills = ["Java", "SQL", "PHP", "JavaScript", "HTML, CSS", "Windows OS", "MacOS", "Networking"]
sidebar_y -= 30
for skill in skills:
    c.drawString(20, sidebar_y, f"• {skill}")
    sidebar_y -= 14

# -------------------------
# MAIN CONTENT
# -------------------------
main_x = sidebar_width + 40
y = height - 100

def section(title, body):
    global y
    # Section title
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(0, 0.3, 0.6)
    c.drawString(main_x, y, title)
    y -= 16
    # Section body
    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica", 10)
    text = c.beginText(main_x, y)
    text.setLeading(14)
    text.textLines(body)
    c.drawText(text)
    y -= 14 * (body.count("\n") + 2)

# Sections
section("Summary", """Passionate about technology and programming, interested in developing skills in a professional environment. 
Background in Java and foundational knowledge in PHP, SQL, and JavaScript. 
Eager to learn, grow, and contribute to impactful projects. Check out my personal work on GitHub.""")

section("Education", """“Don Bosko” Technical High School – Diploma in Computer Science and Software Engineering 
“Kolegji Universum” University – First-year student in Computer Science and Software Engineering""")

section("Projects & Portfolio", """GitHub Portfolio: github.com/denihyseni/python-journey 
Explore projects such as Java applications, SQL database exercises, and Python learning experiments.""")

section("Abilities", """• Problem-solving and analytical thinking 
• Quick learner with adaptability 
• Effective communication and teamwork 
• Strong ambition to achieve deep knowledge in programming""")

section("Hobbies", """• Developing small programming projects 
• Reading technical literature to enhance programming knowledge 
• Sports activities and fitness""")

section("Aspiration", """I aim to apply my knowledge in a professional environment, contribute to impactful projects, 
and continue expanding my expertise in programming and technology.""")

# References
c.setFont("Helvetica", 10)
c.setFillColorRGB(0, 0, 0)
c.drawString(main_x, y, "References available upon request.")

# Save PDF
c.save()

print(f"CV created: {output_path}")
