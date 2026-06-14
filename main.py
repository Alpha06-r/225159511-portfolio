import flet as ft


def main(page: ft.Page):
    page.title = "Rehabeam Portfolio"
    page.theme_mode = ft.ThemeMode.DARK
    page.assets_dir = "assets"
    page.scroll = ft.ScrollMode.AUTO

    # Colors
    BLUE = "#1565C0"
    GOLD = "#D4AF37"
    WHITE = "#FFFFFF"

    # Header
    header = ft.Container(
        content=ft.Column(
            [
                ft.Image(
                    src="ImageFit.jpg",
                    width=180,
                ),

                ft.Text(
                    "REHABEAM PEHOVELO HITILAVALI",
                    size=34,
                    weight=ft.FontWeight.BOLD,
                    color=GOLD,
                    text_align=ft.TextAlign.CENTER,
                ),

                ft.Text(
                    "Computer Programming I Portfolio",
                    size=20,
                    color=WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),

                ft.Text(
                    "UI/UX Designer • Front-End Contributor • Problem Solver",
                    size=16,
                    color=WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),

                ft.Row(
                    [
                        ft.ElevatedButton(
                            "GitHub Profile",
                            url="https://github.com/Alpha06-r",
                        ),

                        ft.ElevatedButton(
                            "Project Repository",
                            url="https://github.com/Alpha06-r/UNAM-I3691CP-WaterLeak-Ongwediva",
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=BLUE,
        padding=25,
    )

    # About
    about = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "ABOUT ME",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=GOLD,
                ),

                ft.Text(
                    """
My name is Rehabeam Pehovelo Hitilavali.

I am a Computer Programming I student with a strong interest in
software development, UI/UX design, and problem solving.

This portfolio showcases my contributions to the Fix-Flow project,
my learning journey, and the skills I developed throughout the semester.
                    """,
                    color=WHITE,
                    size=16,
                ),
            ]
        ),
        padding=20,
    )

    # Project
    project = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "FIX-FLOW PROJECT",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=GOLD,
                ),

                ft.Text(
                    """
Fix-Flow is an Ongwediva Water Leak and Infrastructure Reporting System.

The system allows residents to report water leaks and infrastructure
problems quickly and efficiently.

The goal of the project is to improve communication and speed up
responses to infrastructure issues.
                    """,
                    color=WHITE,
                    size=16,
                ),
            ]
        ),
        padding=20,
    )

    # Contributions
    contributions = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "MY CONTRIBUTIONS",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=GOLD,
                ),

                ft.Text(
                    """
• Assisted with UI/UX Design

• Improved application layouts

• Contributed to front-end implementation

• Assisted with usability testing

• Improved user experience and navigation

• Participated in project discussions and planning
                    """,
                    color=WHITE,
                    size=16,
                ),
            ]
        ),
        padding=20,
    )

    # Skills
    skills = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "SKILLS DEVELOPED",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=GOLD,
                ),

                ft.Text("Python Programming", color=WHITE),
                ft.ProgressBar(value=0.90),

                ft.Text("UI / UX Design", color=WHITE),
                ft.ProgressBar(value=0.95),

                ft.Text("Problem Solving", color=WHITE),
                ft.ProgressBar(value=0.90),

                ft.Text("Team Collaboration", color=WHITE),
                ft.ProgressBar(value=0.85),
            ]
        ),
        padding=20,
    )

    # Screenshots
    screenshots = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "PROJECT SCREENSHOTS",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=GOLD,
                ),

                ft.Text("Login Screen", color=WHITE),
                ft.Image(src="login.png", width=700),

                ft.Text("Dashboard", color=WHITE),
                ft.Image(src="dashboard.png", width=700),

                ft.Text("Admin Panel", color=WHITE),
                ft.Image(src="admin.png", width=700),

                ft.Text("Map View", color=WHITE),
                ft.Image(src="map.png", width=700),

                ft.Text("Report Leak Screen", color=WHITE),
                ft.Image(src="report_leak.png", width=700),
            ]
        ),
        padding=20,
    )

    # Certificates
    certificates = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "MATLAB CERTIFICATES",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=GOLD,
                ),

                ft.Image(src="cert1.png", width=700),
                ft.Image(src="cert2.png", width=700),
                ft.Image(src="cert3.png", width=700),
                ft.Image(src="cert4.png", width=700),
                ft.Image(src="cert5.png", width=700),
                ft.Image(src="cert6.png", width=700),
                ft.Image(src="cert7.png", width=700),
                ft.Image(src="cert8.png", width=700),
            ]
        ),
        padding=20,
    )

    # Reflection
    reflection = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "REFLECTION",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=GOLD,
                ),

                ft.Text(
                    """
The Fix-Flow project provided valuable practical experience in software
development and teamwork.

Through my contribution to UI/UX design and front-end development,
I learned the importance of usability, collaboration, and software testing.

This project strengthened my confidence in programming, communication,
problem solving, and working as part of a development team.
                    """,
                    color=WHITE,
                    size=16,
                ),
            ]
        ),
        padding=20,
    )

    # Video Section
    video = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "CONTRIBUTION VIDEO",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=GOLD,
                ),

                ft.Text(
                    "Contribution.mp4 has been included in the assets folder.",
                    color=WHITE,
                    size=16,
                ),
            ]
        ),
        padding=20,
    )

    # Footer
    footer = ft.Container(
        content=ft.Text(
            "© 2025 Rehabeam Pehovelo Hitilavali",
            color=WHITE,
            text_align=ft.TextAlign.CENTER,
        ),
        bgcolor=BLUE,
        padding=20,
    )

    page.add(
        ft.Column(
            [
                header,
                about,
                project,
                contributions,
                skills,
                screenshots,
                certificates,
                reflection,
                video,
                footer,
            ]
        )
    )


ft.app(target=main)