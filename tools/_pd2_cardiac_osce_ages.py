"""Typical age for each Cardiac OSCE chart row (Jaxon, 2026-10-19: "put the most
common ages with each disease/disorder").

AGES[name] = (from_slides, cite, textbook)
  from_slides  what a deck says about age, in plain words ("" if no deck says)
  cite         the slide(s) it came from ("" if none)
  textbook     a standard-reference age, used ONLY where the decks give none
               or give no number; the page labels it "Textbook, not on the
               slides" so it is never mistaken for course content
"""

AGES = {
    "Primary hypertension": (
        "Climbs with every decade: 23% of adults aged 18&ndash;39, 53% at 40&ndash;59, 72% at 60 and older.",
        "CMS L20 slide 8", ""),
    "Hypertensive emergency": (
        "", "",
        "Middle-aged and older adults with long-standing, poorly controlled hypertension."),
    "Vasovagal syncope": (
        "Young adults, most often young women: reflex syncope causes 85% of fainting before age 40 "
        "(and still half of it in the elderly).",
        "CMS L21 slide 14", ""),
    "Orthostatic hypotension": (
        "Older adults: advanced age is one of its listed causes, alongside low volume and medications.",
        "CMS L21 slide 12", ""),
    "Chronic heart failure": (
        "Mostly over 65: 60% of patients with heart failure are older than 65, and 10&ndash;15% of people "
        "over 80 have it.",
        "CMS L25 slide 6", ""),
    "Stable angina": (
        "Men 45 and older, women 55 and older (the age risk factor); the gap between the sexes closes by "
        "about 80.",
        "CMS L24 slide 22", ""),
    "Acute coronary syndrome": (
        "Men 45 and older, women 55 and older; 65 or older adds a point on the TIMI score.",
        "CMS L24 slides 22, 71", ""),
    "Aortic stenosis": (
        "Over 65: present in 25% of people over 65 and 35% over 70. Over 70 the usual cause is "
        "degenerative; under 70 it is a bicuspid valve.",
        "CMS L23 slides 12&ndash;13", ""),
    "Mitral regurgitation": (
        "", "",
        "Much more common with age; moderate or severe regurgitation affects about 1 in 10 people "
        "over 75."),
    "Mitral valve prolapse": (
        "Healthy women aged 15&ndash;30.",
        "CMS L23 slide 54", ""),
    "Chronic venous insufficiency and varicose veins": (
        "Rises with age (advancing age is its first listed risk factor); women more often than men.",
        "CMS L26 slide 8", ""),
    "Deep vein thrombosis": (
        "Over 60 (a listed risk factor), or any age with a provoking cause such as surgery or bed rest.",
        "CMS L26 slides 50, 64", ""),
    "Peripheral artery disease": (
        "Over 60 with no other risk factors; 50 and older with smoking, diabetes, hypertension or high "
        "cholesterol.",
        "CMS L27 slide 11", ""),
    "Aortic dissection": (
        "60s and 70s, men more than women; younger with Marfan syndrome.",
        "CMS L27 slide 115", ""),
    "Hypertrophic cardiomyopathy": (
        "Any age, but it is the leading cause of sudden death in preadolescents and adolescents, usually "
        "during extreme exertion.",
        "CMS L28 slides 58, 66", ""),
    "Atrial fibrillation": (
        "Older adults (&ldquo;elderly&rdquo; is on its risk list).",
        "CMS L29 slide 48",
        "Rare before 55; about 1 in 10 people over 80."),
    "Premature ventricular contractions": (
        "", "",
        "Any age; they become more frequent with age and with heart disease."),
    "Ventricular tachycardia": (
        "", "",
        "Mostly older adults with structural heart disease, above all a prior heart attack."),
    "Acute pericarditis": (
        "", "",
        "Most often men aged 20 to 50."),
    "Cardiac tamponade": (
        "Any age; it follows its cause. In older adults, suspect cancer first.",
        "CMS L31 slide 36", ""),
}
