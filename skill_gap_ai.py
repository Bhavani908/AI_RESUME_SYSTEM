# ================= ROLE SKILLS DATABASE =================
role_skills = {
    "software developer": [
        "oops", "data structures", "algorithms", "api", "database",
        "git", "problem solving", "system design", "debugging"
    ],
    "data analyst": [
        "sql", "excel", "python", "pandas", "data visualization",
        "statistics", "power bi", "tableau"
    ],
    "web developer": [
        "html", "css", "javascript", "react", "node js",
        "responsive design", "rest api"
    ],
    "software tester": [
        "testing", "selenium", "automation testing", "jira",
        "test cases", "bug reporting"
    ],
    "customer support executive": [
        "communication", "customer handling", "problem solving",
        "crm tools", "email etiquette"
    ],
    "business analyst": [
        "requirements gathering", "documentation", "stakeholder management",
        "excel", "data analysis"
    ]
}

# ================= LEARNING RESOURCE DATABASE =================
resources_db = {
    # Software Dev
    "oops": "https://www.geeksforgeeks.org/object-oriented-programming-oops-concept-in-java/",
    "data structures": "https://www.geeksforgeeks.org/data-structures/",
    "algorithms": "https://www.geeksforgeeks.org/fundamentals-of-algorithms/",
    "api": "https://www.freecodecamp.org/news/what-is-an-api/",
    "database": "https://www.w3schools.com/sql/",
    "git": "https://www.atlassian.com/git/tutorials",
    "problem solving": "https://leetcode.com/problemset/all/",
    "system design": "https://www.geeksforgeeks.org/system-design-tutorial/",
    "debugging": "https://www.guru99.com/debugging-techniques.html",

    # Data Analyst
    "sql": "https://www.w3schools.com/sql/",
    "excel": "https://excel-practice-online.com/",
    "python": "https://www.learnpython.org/",
    "pandas": "https://www.geeksforgeeks.org/python-pandas-tutorial/",
    "data visualization": "https://www.tableau.com/learn/training",
    "statistics": "https://www.khanacademy.org/math/statistics-probability",
    "power bi": "https://learn.microsoft.com/en-us/training/powerplatform/power-bi",
    "tableau": "https://www.tableau.com/learn/training",

    # Web Dev
    "html": "https://www.w3schools.com/html/",
    "css": "https://www.w3schools.com/css/",
    "javascript": "https://www.javascript.info/",
    "react": "https://react.dev/learn",
    "node js": "https://nodejs.dev/learn",
    "responsive design": "https://www.freecodecamp.org/news/responsive-web-design-basics/",
    "rest api": "https://restfulapi.net/",

    # Testing
    "testing": "https://www.guru99.com/software-testing.html",
    "selenium": "https://www.selenium.dev/documentation/",
    "automation testing": "https://www.guru99.com/automation-testing.html",
    "jira": "https://www.atlassian.com/software/jira/guides",
    "test cases": "https://www.guru99.com/test-case.html",
    "bug reporting": "https://www.guru99.com/bug-life-cycle.html",

    # Customer Support
    "communication": "https://www.toastmasters.org/",
    "customer handling": "https://www.coursera.org/courses?query=customer%20service",
    "problem solving": "https://www.mindtools.com/pages/main/newMN_TMC.htm",
    "crm tools": "https://www.salesforce.com/in/crm/what-is-crm/",
    "email etiquette": "https://www.indeed.com/career-advice/career-development/email-etiquette",

    # Business Analyst
    "requirements gathering": "https://www.tutorialspoint.com/software_engineering/software_requirements.htm",
    "documentation": "https://www.lucidchart.com/blog/how-to-write-software-documentation",
    "stakeholder management": "https://www.smartsheet.com/content/stakeholder-management",
    "data analysis": "https://www.coursera.org/specializations/data-analysis"
}

# ================= LOGIC =================
def detect_skill_gap(role, resume_text):
    skills = role_skills.get(role.lower(), [])
    resume_text = resume_text.lower()
    return [skill for skill in skills if skill not in resume_text]

def recommend_resources(skill_gaps):
    return {skill: resources_db.get(skill, "Search on Google") for skill in skill_gaps}
