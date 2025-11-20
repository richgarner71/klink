import pandas as pd
from datetime import datetime

# Define the resources data
resources = [
    # Category 1: Educational Resources, Databases, or LLMs
    {
        "Resource Name": "Risk Evaluation Database (RED)",
        "Type": "Database",
        "URL": "https://kinkbeyondlimits.com/risk-evaluation-database-red-bdsm-safety-kink-risk-awareness/",
        "Description": "A comprehensive risk evaluation database offered by Kink Beyond Limits to guide individuals on risks in BDSM play, covering aspects from breath play to impact play [1]",
        "Key Features": "Risk assessment tools; Coverage of multiple BDSM activities; Safety guidelines; Negotiation support; Informed consent framework",
        "Safety Focus Areas": "Breath play risks; Impact play safety; General BDSM risk awareness; Scene negotiation; Informed consent",
        "Notes": "Focuses specifically on risk-aware consensual kink (RACK) principles"
    },
    {
        "Resource Name": "Dom Sub Living",
        "Type": "Website/Educational Platform",
        "URL": "https://domsubliving.com/",
        "Description": "BDSM training platform offering D/s relationship coaching, practical guidance for Dominants and submissives, and comprehensive educational resources [2]",
        "Key Features": "Free and premium training content; BDSM checklists; Scene creation guides; Impact play tutorials; Confidence building resources; Over 10,000 students trained worldwide",
        "Safety Focus Areas": "Consent practices; Safe scene creation; Limit setting; Communication in D/s relationships; SSC (Safe, Sane, Consensual) principles",
        "Notes": "Based in North America; Offers both free and paid content"
    },
    {
        "Resource Name": "The Duchy",
        "Type": "Website/Educational Platform",
        "URL": "https://www.theduchy.com/",
        "Description": "Rope-focused educational organization offering courses, tutorials, and resources on rope bondage with emphasis on consent, negotiation, risks, and aftercare [3]",
        "Key Features": "Video tutorials organized by skill level; Scene negotiation forms; Consent worksheets; Private community Discord; Comprehensive education list covering BDSM topics; Free and membership content",
        "Safety Focus Areas": "Rope safety; Proper knot placement; Circulation awareness; Consent and negotiation; Risk management in bondage; Aftercare protocols",
        "Notes": "Excellent resource for rope bondage education; Includes downloadable negotiation forms"
    },
    {
        "Resource Name": "BDSM Wiki",
        "Type": "Database/Knowledge Base",
        "URL": "Multiple references as comprehensive online resource",
        "Description": "Comprehensive online encyclopedia providing definitions, basic information, philosophy of kink, and best practice suggestions for BDSM community [4]",
        "Key Features": "Extensive terminology definitions; Philosophy discussions; Best practice guidelines; Community-maintained content; Wikipedia-style structure",
        "Safety Focus Areas": "Terminology education; Safety acronyms (SSC, RACK, PRICK, CCCC); Consent principles; Risk awareness",
        "Notes": "Community-driven resource similar to Wikipedia format"
    },
    {
        "Resource Name": "Kink Academy",
        "Type": "Educational Platform/LLM Alternative",
        "URL": "https://www.kinkacademy.com/",
        "Description": "Leading resource for adult sexuality education with over 2,000 sex-education videos from 140+ educators worldwide, covering BDSM, polyamory, fetish, and swinging [5]",
        "Key Features": "2,000+ educational videos; 140+ sexuality educators; Weekly new content; Categorized by skill level (basic/intermediate/advanced); 24/7 accessibility; Free sample videos; Body-positive and kink-positive approach",
        "Safety Focus Areas": "Anatomy for BDSM; Safer sex practices; Risk awareness; Consent culture; Understanding boundaries; Legal concerns; Play party etiquette",
        "Notes": "Founded by Princess Kali; Subscription-based with free content available"
    },
    {
        "Resource Name": "SADE (School of Advanced Dynamic Education)",
        "Type": "Educational Platform",
        "URL": "https://sadeclasses.org/",
        "Description": "Volunteer-run, not-for-profit initiative providing inclusive, accessible, safe, and consent-focused BDSM education with vetted instructors [6]",
        "Key Features": "200+ classes offered; 22 years of service; Vetted instructors; Online classes; Charity donations; Ethical standards enforcement",
        "Safety Focus Areas": "Consent-focused education; Inclusive practices; Instructor credibility verification; Safe learning environment",
        "Notes": "Not-for-profit organization; North American based"
    },
    {
        "Resource Name": "Kink Knowledgeable Program",
        "Type": "Professional Training/Database",
        "URL": "https://kinkknowledgeable.com/",
        "Description": "Online academy training psychotherapists and professionals on BDSM to improve their competency in working with clients who practice kink [7]",
        "Key Features": "Structured professional training program; Three-part curriculum (Foundations, Therapeutic Considerations, BDSM Expertise); Targets therapists, medical, allied health, and legal professionals",
        "Safety Focus Areas": "Professional competency in kink; Non-pathologizing approaches; Therapeutic safety; Client care standards",
        "Notes": "Specifically for professionals, not general public"
    },
    {
        "Resource Name": "OhYesPlease",
        "Type": "Educational Platform",
        "URL": "https://ohyesplease.org/",
        "Description": "Online kink education platform offering playful, undogmatic courses from gender-inclusive, shame-free, body-positive, and consensually informed perspective [8]",
        "Key Features": "One-time payment for lifetime access; No downloads required; Gender-inclusive content; Courses on impact play, erotic shame, kink & trauma",
        "Safety Focus Areas": "Risk-aware practices; Consensual framework; Trauma-informed approach; Body-positive education",
        "Notes": "Emphasizes inclusivity and accessibility"
    },
    {
        "Resource Name": "Unearthed Pleasures",
        "Type": "Educational Platform",
        "URL": "https://www.unearthedpleasures.com/",
        "Description": "Platform teaching kink concepts through self-exploration, education, and folk knowledge to help individuals discover desires and create unique kink journeys [9]",
        "Key Features": "Kink Beginnings Bundle; Video content; Downloadable guides; Lifetime access; Beginner to intermediate progression",
        "Safety Focus Areas": "Self-exploration safety; Desire discovery; Partner communication; Personal boundary setting",
        "Notes": "Focus on individual journey and self-discovery"
    },
    {
        "Resource Name": "Submissive Guide",
        "Type": "Website/Educational Platform",
        "URL": "https://submissiveguide.com/",
        "Description": "Comprehensive resource led by Luna providing 15+ years of compassionate submissive learning with guides, worksheets, courses, podcast, and community [10]",
        "Key Features": "In-depth guides and articles; Self-paced courses; Podcast; Supportive community; Worksheets and journal prompts; Document library; Video vault; Weekly newsletter",
        "Safety Focus Areas": "Submissive safety; Communication skills; Personal growth; Relationship dynamics; BDSM safety protocols; Submissive skills development",
        "Notes": "Long-established resource specifically for submissives; Also has YouTube channel"
    },
    
    # Category 2: Non-Dating Kink Apps
    {
        "Resource Name": "KINX",
        "Type": "App",
        "URL": "https://kinxlist.com/",
        "Description": "Interactive checklist app allowing users to save and share preferences regarding sex-play, kink, and BDSM with play partners, functioning as a quiz to initiate conversations about boundaries [11]",
        "Key Features": "Interactive preference checklist; Save and share functionality; Summary reports; Conversation starter tool; Personal meaning integration; Jungian concepts integration",
        "Safety Focus Areas": "Boundary communication; Limit identification; Needs articulation; Consent facilitation; Pre-scene negotiation",
        "Notes": "Founded by Athos; Emphasis on personal meaning through kink"
    },
    {
        "Resource Name": "NoGrey",
        "Type": "App",
        "URL": "Referenced in Slate article - Australian-developed app",
        "Description": "Australian-developed app streamlining pre-liaison communication, allowing users to sift through 600+ kinks and create scene templates with visual interest representation [12]",
        "Key Features": "600+ kink categories; Interest and experience level specification; Visual interest mapping; Scene template creation; Limits documentation; Aftercare planning; Partner comparison tools",
        "Safety Focus Areas": "Pre-scene communication; Interest matching; Limit setting; Scene planning; Aftercare coordination",
        "Notes": "Developed by Australian kinksters; Emphasizes being supplementary to direct communication"
    },
    {
        "Resource Name": "Obedience: BDSM Habit Tracker",
        "Type": "App",
        "URL": "https://apps.apple.com/us/app/obedience-bdsm-habit-tracker/id1484629691",
        "Description": "Mobile app for couples in D/s dynamics to track habits, assign tasks, and manage rewards and punishments with secure communication features [13]",
        "Key Features": "Habit/task tracking; Rewards system; Punishment tracking; Rules and limits documentation; In-app secure chat; History and progress charts; Free and Pro versions; Cross-platform (iOS/Android); Discrete mode available",
        "Safety Focus Areas": "Dynamic consistency; Communication maintenance; Boundary documentation; Rule tracking; Safe power exchange structure",
        "Notes": "Pro version offers unlimited habits and customization; Discrete mode changes app appearance"
    },
    {
        "Resource Name": "BeMoreKinky",
        "Type": "App/Website",
        "URL": "https://www.bemorekinky.com/",
        "Description": "BDSM education and kink tool for couples focusing on facilitating intimate conversations, exploring preferences, and planning scenes [14]",
        "Key Features": "600+ activities with D/s perspectives; Swipe and match functionality; Scene planning tools; Private quizzes; Activity rating; Educational articles; Scene generator; Calendar scheduling; Switch-friendly",
        "Safety Focus Areas": "Communication facilitation; Consent practices; Scene preparation; BDSM fundamentals; Safe practices education; D/s protocols",
        "Notes": "Caters to both beginners and experienced practitioners; Comprehensive educational content"
    },
    {
        "Resource Name": "Carnal Calibration",
        "Type": "App/Tool",
        "URL": "Referenced in Reddit discussions",
        "Description": "Tool for matching interests between partners where both individuals fill out a quiz and reveals mutual 'yes' responses [15]",
        "Key Features": "Partner quiz system; Interest matching; Mutual consent revelation; Privacy for non-matches",
        "Safety Focus Areas": "Mutual consent; Interest compatibility; Private desire disclosure; Safe exploration framework",
        "Notes": "Recommended by BDSM community on Reddit; Similar to Mojo Upgrade"
    },
    {
        "Resource Name": "Mojo Upgrade",
        "Type": "App/Tool",
        "URL": "Referenced in multiple sources",
        "Description": "Couples compatibility tool where partners complete quizzes and the platform highlights activities both expressed interest in [16]",
        "Key Features": "Couples quiz system; Shared interest highlighting; Privacy protection; Activity exploration",
        "Safety Focus Areas": "Mutual interest identification; Consent verification; Safe exploration boundaries; Communication facilitation",
        "Notes": "Popular tool for couples exploring kink together"
    },
    
    # Category 3: Educational Blogs/Vlogs/Websites
    {
        "Resource Name": "Watts The Safeword",
        "Type": "Vlog/YouTube Channel",
        "URL": "https://www.youtube.com/channel/UCokRyLsHxh-NykvT4uA6n2g",
        "Description": "San Francisco-based kink and sex education YouTube channel hosted by Pup Amp and Mr. Kristofer, offering LGBTIQA+ inclusive content on alternative lifestyles since 2015 [17]",
        "Key Features": "BDSM bondage how-tos; Fetish explanations; Upbeat and entertaining videos; Multi-platform community; Sex-positive approach; Shame-free education",
        "Safety Focus Areas": "BDSM technique safety; Fetish education; LGBTIQA+ inclusive practices; Destigmatization of alternative lifestyles",
        "Notes": "Long-standing YouTube presence; Strong LGBTQ+ focus; North American based"
    },
    {
        "Resource Name": "Evie Lupine",
        "Type": "Vlog/YouTube Channel",
        "URL": "Referenced as popular kink education channel",
        "Description": "YouTube channel with 450+ videos exploring wide range of topics under alternative lifestyle umbrella since 2016 [18]",
        "Key Features": "450+ educational videos; Well-structured content; Exploratory approach; Large audience; Diverse topic coverage",
        "Safety Focus Areas": "Alternative lifestyle education; Safety practices; Consent education; Risk awareness",
        "Notes": "Highly regarded in kink community for comprehensive content"
    },
    {
        "Resource Name": "MorganThorneBDSM",
        "Type": "Vlog/YouTube Channel/Website",
        "URL": "https://www.youtube.com/channel/UCwx8uy7nxohWLwnaPocLsyg",
        "Description": "YouTube channel and website by Ms. Morgan Thorne raising awareness about kink and fetish topics with categorized videos and DIY tutorials [19]",
        "Key Features": "Categorized video library; DIY tutorials for kinksters; Workshops; Online classes; BDSM basics training; Skills instruction; Community education",
        "Safety Focus Areas": "Kink awareness; Safety in DIY projects; BDSM relationship safety; Community standards; Negotiation skills",
        "Notes": "Offers both free and paid content; North American educator"
    },
    {
        "Resource Name": "Kink Educator",
        "Type": "Vlog/YouTube Channel",
        "URL": "https://www.youtube.com/channel/UCtZR78_vnEsfoTe-7DREisw",
        "Description": "YouTube channel offering mature kink education for alternative lifestyle and kinky knowledge, created by comic book creator and kink educator [20]",
        "Key Features": "BDSM 101 playlists; Organized educational series; Alt lifestyle content; Comprehensive basic to advanced coverage",
        "Safety Focus Areas": "BDSM fundamentals; Safety basics; Education for beginners; Progressive skill building",
        "Notes": "Structured educational approach with playlists"
    },
    {
        "Resource Name": "Sexplanations",
        "Type": "Vlog/YouTube Channel",
        "URL": "Referenced as popular sex education channel",
        "Description": "YouTube channel hosted by Dr. Lindsey Doe, clinical sexologist, providing sex-positive, shame-free, comprehensive sex education including kink topics [21]",
        "Key Features": "Clinical sexologist host; Upbeat videos; Comprehensive sex education; Anatomy to consent coverage; Evidence-based information",
        "Safety Focus Areas": "Comprehensive consent education; Sexual health; Risk awareness; Shame-free approach; Clinical accuracy",
        "Notes": "Broader sex education with kink components; Professionally credentialed host"
    },
    {
        "Resource Name": "FetLife",
        "Type": "Community/Social Network",
        "URL": "https://fetlife.com/",
        "Description": "Largest social network for BDSM, Leather, and Fetish communities with over 1 million members, facilitating social interaction and event listings [22]",
        "Key Features": "Social networking; Event listings (munches, classes, play parties); Discussion groups; Educational resources; Glossary of terms; Privacy-first approach; No data selling",
        "Safety Focus Areas": "Community vetting; Event information; Network building; Resource sharing; Privacy protection; Anti-revenge porn partnership",
        "Notes": "Primary platform for finding local kink events in North America; Not primarily a dating app"
    },
    {
        "Resource Name": "The Eulenspiegel Society (TES)",
        "Type": "Community/Organization",
        "URL": "Referenced as major BDSM organization",
        "Description": "501(c)(3) non-profit BDSM/Leather/Fetish organization promoting social interaction, educational exchange, and diversity, operating The TES Center in NYC [23]",
        "Key Features": "High-quality education programs; Annual sex-positive events; Forums for discourse; Physical center in NYC; Community building; East Coast focus",
        "Safety Focus Areas": "Educational standards; Community safety; Diversity and inclusion; Ethical practices; Member support",
        "Notes": "Major East Coast organization; Physical presence in New York City"
    },
    {
        "Resource Name": "National Coalition for Sexual Freedom (NCSF)",
        "Type": "Community/Organization/Database",
        "URL": "https://www.kapprofessionals.org/",
        "Description": "501(c)(3) advocacy organization for BDSM, Leather, and Fetish communities, maintaining Kink Aware Professionals (KAP) directory [24]",
        "Key Features": "Kink Aware Professionals directory; Legislative lobbying; Community education; Registry of kink-aware therapists, doctors, lawyers; Advocacy work; Professional resources",
        "Safety Focus Areas": "Professional care standards; Non-pathologizing treatment; Legal protection; Community rights; Access to knowledgeable professionals",
        "Notes": "National U.S. organization; Critical resource for finding kink-aware professionals"
    },
    {
        "Resource Name": "Kynk 101",
        "Type": "Website/Blog",
        "URL": "https://kynk101.com/",
        "Description": "Educational website providing comprehensive articles on kink and BDSM facts including negotiation basics, online safety, and consent practices [25]",
        "Key Features": "Negotiation guides; Online safety resources; Consent education; BDSM facts; Self-reflection prompts; Practical advice",
        "Safety Focus Areas": "Negotiations in kink; Online safety; Consent basics; Risk awareness; Boundary setting",
        "Notes": "User-friendly format; Good resource for beginners"
    },
    {
        "Resource Name": "Bondesque",
        "Type": "Website/Blog",
        "URL": "https://www.bondesque.com/",
        "Description": "Educational blog covering SSC principles and 7 BDSM safety rules, providing detailed safety guidelines for various BDSM practices [26]",
        "Key Features": "SSC principle education; Detailed safety rules; Practice-specific guidelines; Safety acronym explanations; Equipment safety",
        "Safety Focus Areas": "Safe, Sane, Consensual practices; Safety rule implementation; Equipment use; Risk management; Substance use warnings",
        "Notes": "Strong emphasis on safety fundamentals"
    },
    {
        "Resource Name": "BadGirlsBible",
        "Type": "Website/Blog",
        "URL": "https://badgirlsbible.com/",
        "Description": "Comprehensive sex education website including extensive BDSM negotiation guides, kink lists, and fetish education resources [27]",
        "Key Features": "239 sexual fetishes and kinks list; BDSM negotiation guide; Scene planning resources; Communication tips; Comprehensive kink education",
        "Safety Focus Areas": "BDSM negotiation; Consent practices; Scene safety; Communication; Risk awareness",
        "Notes": "Very comprehensive kink lists; Accessible format"
    },
    {
        "Resource Name": "DanceSafe",
        "Type": "Website/Organization",
        "URL": "https://dancesafe.org/",
        "Description": "Organization providing guide on 'Navigating Mutual Consent Agreements' with lessons from BDSM negotiations applicable to broader consent education [28]",
        "Key Features": "Consent agreement guides; BDSM negotiation lessons; Substance use safety; Harm reduction approach; Educational toolbox series",
        "Safety Focus Areas": "Mutual consent agreements; Negotiation practices; Harm reduction; Substance use safety; Consent capacity",
        "Notes": "Broader harm reduction organization with excellent BDSM consent resources"
    },
    {
        "Resource Name": "Loving BDSM",
        "Type": "Podcast/Blog/Website",
        "URL": "https://lovingbdsm.net/",
        "Description": "Podcast and blog hosted by married D/s couple (John Brownstone & Kayla Lords) offering 400+ episodes on healthy power exchange relationships since 2015 [29]",
        "Key Features": "Weekly podcast (2 episodes/week); Blog posts; YouTube content; Q&A sessions; Resources for beginners; 30 Days of D/s workbook; Product reviews; Show notes archive",
        "Safety Focus Areas": "Healthy power exchange; Consent ('Play safe and gain consent. Always'); Communication; D/s relationship safety; Boundary respect",
        "Notes": "Highly rated (4.6/5 stars on Apple Podcasts); Personal experiences from active D/s couple; 400+ episodes"
    },
    {
        "Resource Name": "Kink Beyond Limits",
        "Type": "Website/Blog",
        "URL": "https://kinkbeyondlimits.com/",
        "Description": "Educational website hosting the Risk Evaluation Database (RED) and providing comprehensive BDSM safety and risk awareness education [30]",
        "Key Features": "Risk Evaluation Database; Safety guides; Negotiation resources; Risk awareness education; Comprehensive safety information",
        "Safety Focus Areas": "Risk evaluation; BDSM safety; Negotiation; Informed consent; Risk-aware practices",
        "Notes": "Home of RED database; Strong focus on risk awareness"
    },
    {
        "Resource Name": "FindAMunch.com (MALL Directory)",
        "Type": "Website/Directory",
        "URL": "https://findamunch.com/",
        "Description": "Directory listing BDSM events, munches, and educational gatherings worldwide with dedicated North America section [31]",
        "Key Features": "Event directory; Munch listings; Educational event calendar; North American focus section; Multiple lifestyle categories; Convention listings",
        "Safety Focus Areas": "Community vetting through munches; Safe social spaces; Event information; Local community connection",
        "Notes": "Critical resource for finding local in-person educational events and munches in North America"
    }
]

# Create DataFrame
df = pd.DataFrame(resources)

# Save to Excel with formatting
with pd.ExcelWriter('/home/ubuntu/kink_resources_catalog.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Kink Resources', index=False)
    
    # Get workbook and worksheet objects
    workbook = writer.book
    worksheet = writer.sheets['Kink Resources']
    
    # Define formats
    header_format = workbook.add_format({
        'bold': True,
        'bg_color': '#4F81BD',
        'font_color': 'white',
        'border': 1,
        'text_wrap': True,
        'valign': 'vcenter'
    })
    
    cell_format = workbook.add_format({
        'text_wrap': True,
        'valign': 'top',
        'border': 1
    })
    
    url_format = workbook.add_format({
        'text_wrap': True,
        'valign': 'top',
        'border': 1,
        'font_color': 'blue',
        'underline': True
    })
    
    # Set column widths
    worksheet.set_column('A:A', 30)  # Resource Name
    worksheet.set_column('B:B', 20)  # Type
    worksheet.set_column('C:C', 40)  # URL
    worksheet.set_column('D:D', 60)  # Description
    worksheet.set_column('E:E', 50)  # Key Features
    worksheet.set_column('F:F', 50)  # Safety Focus Areas
    worksheet.set_column('G:G', 40)  # Notes
    
    # Apply header format
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)
    
    # Apply cell formats
    for row_num in range(1, len(df) + 1):
        for col_num in range(len(df.columns)):
            if col_num == 2:  # URL column
                worksheet.write(row_num, col_num, df.iloc[row_num-1, col_num], url_format)
            else:
                worksheet.write(row_num, col_num, df.iloc[row_num-1, col_num], cell_format)
    
    # Freeze top row
    worksheet.freeze_panes(1, 0)

print(f"✓ Successfully created kink_resources_catalog.xlsx with {len(resources)} resources")
print(f"\nBreakdown by category:")
print(f"  - Educational Resources/Databases/LLMs: 10")
print(f"  - Non-Dating Kink Apps: 6")
print(f"  - Educational Blogs/Vlogs/Websites: 15")
print(f"  - Total: 31 resources")
print(f"\nFile location: /home/ubuntu/kink_resources_catalog.xlsx")
