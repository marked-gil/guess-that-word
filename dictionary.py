"""
This module contains the words and their definitions that are used in the game.
"""

# List of easy words
easy_words = [
    {
        "id": "e1",
        "word": "anger",
        "definition": "A strong feeling of displeasure and usually of "
        "antagonism",
    },
    {
        "id": "e2",
        "word": "answer",
        "definition": "Something spoken or written in reply to a question",
    },
    {
        "id": "e3",
        "word": "dream",
        "definition": "A series of thoughts, images, or emotions occurring "
        "during sleep",
    },
    {
        "id": "e4",
        "word": "famous",
        "definition": "Widely known",
    },
    {
        "id": "e5",
        "word": "holiday",
        "definition": "A day on which one is exempt from work",
    },
    {
        "id": "e6",
        "word": "office",
        "definition": "A position of responsibility or some degree of "
        "executive authority",
    },
    {
        "id": "e7",
        "word": "wedding",
        "definition": "A marriage ceremony usually with its accompanying "
        "festivities",
    },
    {
        "id": "e8",
        "word": "student",
        "definition": "An attentive and systematic observer",
    },
    {
        "id": "e9",
        "word": "shallow",
        "definition": "Having little depth",
    },
    {
        "id": "e10",
        "word": "village",
        "definition": "A settlement usually larger than a hamlet and smaller "
        "than a town",
    },
    {
        "id": "e11",
        "word": "freedom",
        "definition": "The absence of necessity, coercion, or constraint in "
        "choice or action",
    },
    {
        "id": "e12",
        "word": "expensive",
        "definition": "Involving high cost or sacrifice",
    },
    {
        "id": "e13",
        "word": "honest",
        "definition": "Free from fraud or deception",
    },
    {
        "id": "e14",
        "word": "friendly",
        "definition": "Showing kindly interest and goodwill",
    },
    {
        "id": "e15",
        "word": "problem",
        "definition": "A question raised for inquiry, consideration, or "
        "solution",
    },
    {
        "id": "e16",
        "word": "magazine",
        "definition": "A print periodical containing miscellaneous pieces",
    },
    {
        "id": "e17",
        "word": "special",
        "definition": "Readily distinguishable from others of the same "
        "category",
    },
    {
        "id": "e18",
        "word": "tomorrow",
        "definition": "On or for the day after today",
    },
    {
        "id": "e19",
        "word": "repeat",
        "definition": "To make, do, or perform again",
    },
    {
        "id": "e20",
        "word": "silence",
        "definition": "Absence of sound or noise",
    },
    {
        "id": "e21",
        "word": "strange",
        "definition": "Different from what is usual, ordinary, or expected",
    },
    {
        "id": "e22",
        "word": "promise",
        "definition": "A declaration that one will do or refrain from doing "
        "something specified",
    },
    {
        "id": "e23",
        "word": "garden",
        "definition": "A plot of ground where herbs, fruits, flowers, or "
        "vegetables are cultivated",
    },
    {
        "id": "e24",
        "word": "destroy",
        "definition": "To ruin the structure, organic existence, or condition "
        "of",
    },
    {
        "id": "e25",
        "word": "basket",
        "definition": "A receptacle made of interwoven material",
    },
    {
        "id": "e26",
        "word": "attack",
        "definition": "To set upon or work against forcefully",
    },
    {
        "id": "e27",
        "word": "nomad",
        "definition": "An individual who roams about",
    },
    {
        "id": "e28",
        "word": "warehouse",
        "definition": "A structure or room for the storage of merchandise or "
        "commodities",
    },
    {
        "id": "e29",
        "word": "danger",
        "definition": "Exposure or liability to injury, pain, harm, or loss",
    },
    {
        "id": "e30",
        "word": "escape",
        "definition": "To get away",
    },
    {
        "id": "e31",
        "word": "strong",
        "definition": "Having or marked by great physical power",
    },
    {
        "id": "e32",
        "word": "breathe",
        "definition": "To draw air into and expel it from the lungs",
    },
    {
        "id": "e33",
        "word": "opportunity",
        "definition": "A good chance for advancement or progress",
    },
    {
        "id": "e34",
        "word": "dirty",
        "definition": "Not clean or pure",
    },
    {
        "id": "e35",
        "word": "common",
        "definition": "Belonging to or shared by two or more individuals or "
        "things or by all",
    },
    {
        "id": "e36",
        "word": "extreme",
        "definition": "Going to great or exaggerated lengths",
    },
    {
        "id": "e37",
        "word": "fever",
        "definition": "A rise of body temperature above the normal",
    },
    {
        "id": "e38",
        "word": "healthy",
        "definition": "Not displaying clinical signs of disease or infection",
    },
    {
        "id": "e39",
        "word": "opposite",
        "definition": "Contrary to one another or to a thing specified",
    },
    {
        "id": "e40",
        "word": "threat",
        "definition": "An expression of intention to inflict evil, injury, or "
        "damage",
    },
    {
        "id": "e41",
        "word": "simple",
        "definition": "Of humble origin or modest position",
    },
    {
        "id": "e42",
        "word": "school",
        "definition": "An organization that provides instruction",
    },
    {
        "id": "e43",
        "word": "prevent",
        "definition": "To keep from happening or existing",
    },
    {
        "id": "e44",
        "word": "perfect",
        "definition": "Being entirely without fault or defect",
    },
    {
        "id": "e45",
        "word": "hungry",
        "definition": "Feeling an uneasy or painful sensation from lack of "
        "food",
    },
    {
        "id": "e46",
        "word": "accurate",
        "definition": "Free from error especially as the result of care",
    },
    {
        "id": "e47",
        "word": "barrier",
        "definition": "Something material that blocks or is intended to block "
        "passage",
    },
    {
        "id": "e48",
        "word": "complaint",
        "definition": "Expression of grief, pain, or dissatisfaction",
    },
    {
        "id": "e49",
        "word": "decline",
        "definition": "To tend toward an inferior state or weaker condition",
    },
    {
        "id": "e50",
        "word": "expand",
        "definition": "To increase the extent, number, volume, or scope of",
    },
]


# List of hard words
hard_words = [
    {
        "id": "h1",
        "word": "expatriate",
        "definition": "To leave one's native country to live elsewhere",
    },
    {
        "id": "h2",
        "word": "obsolete",
        "definition": "No longer in use or no longer useful",
    },
    {
        "id": "h3",
        "word": "intuition",
        "definition": "An innate sense of what is true or what will happen",
    },
    {
        "id": "h4",
        "word": "bailiwick",
        "definition": "The sphere in which one has superior knowledge or "
        "authority",
    },
    {
        "id": "h5",
        "word": "community",
        "definition": "A unified body of individuals",
    },
    {
        "id": "h6",
        "word": "swindle",
        "definition": "To obtain money or property by fraud or deceit",
    },
    {
        "id": "h7",
        "word": "acquiesce",
        "definition": "To accept, comply, or submit tacitly or passively",
    },
    {
        "id": "h8",
        "word": "ambiguous",
        "definition": "Capable of being understood in two or more possible "
        "senses or ways",
    },
    {
        "id": "h9",
        "word": "deference",
        "definition": "Respect and esteem due a superior or an elder",
    },
    {
        "id": "h10",
        "word": "clandestine",
        "definition": "Marked by, held in, or conducted with secrecy",
    },
    {
        "id": "h11",
        "word": "docile",
        "definition": "Easily taught",
    },
    {
        "id": "h12",
        "word": "divergent",
        "definition": "Moving or extending in different directions from a "
        "common point",
    },
    {
        "id": "h13",
        "word": "enigma",
        "definition": "Something hard to understand or explain",
    },
    {
        "id": "h14",
        "word": "interactive",
        "definition": "Involving the actions or input of a user",
    },
    {
        "id": "h15",
        "word": "epitaph",
        "definition": "An inscription on or at a tomb or a grave in memory of "
        "the one buried there",
    },
    {
        "id": "h16",
        "word": "magnanimous",
        "definition": "Showing or suggesting a lofty and courageous spirit",
    },
    {
        "id": "h17",
        "word": "invincible",
        "definition": "Incapable of being conquered, overcome, or subdued",
    },
    {
        "id": "h18",
        "word": "reflection",
        "definition": "The production of an image by or as if by a mirror",
    },
    {
        "id": "h19",
        "word": "authentic",
        "definition": "Made or done the same way as an original",
    },
    {
        "id": "h20",
        "word": "eminent",
        "definition": "Standing out so as to be readily perceived or noted",
    },
    {
        "id": "h21",
        "word": "identical",
        "definition": "Having such close resemblance as to be essentially the "
        "same",
    },
    {
        "id": "h22",
        "word": "augment",
        "definition": "To make greater, more numerous, larger, or more "
        "intense",
    },
    {
        "id": "h23",
        "word": "outskirt",
        "definition": "A part remote from the center",
    },
    {
        "id": "h24",
        "word": "sufficient",
        "definition": "Enough to meet the needs of a situation or a proposed "
        "end",
    },
    {
        "id": "h25",
        "word": "extort",
        "definition": "To obtain from a person by force, intimidation, or "
        "undue or illegal power",
    },
    {
        "id": "h26",
        "word": "wayward",
        "definition": "Following one's own capricious, wanton, or depraved "
        "inclinations",
    },
    {
        "id": "h27",
        "word": "converge",
        "definition": "To come together and unite in a common interest or "
        "focus",
    },
    {
        "id": "h28",
        "word": "admiration",
        "definition": "A feeling of respect and approval",
    },
    {
        "id": "h29",
        "word": "agreement",
        "definition": "Harmony of opinion, action, or character",
    },
    {
        "id": "h30",
        "word": "appropriate",
        "definition": "Especially suitable or compatible",
    },
    {
        "id": "h31",
        "word": "calamity",
        "definition": "A disastrous event marked by great loss and lasting "
        "distress and suffering",
    },
    {
        "id": "h32",
        "word": "comfortable",
        "definition": "Affording or enjoying contentment and security",
    },
    {
        "id": "h33",
        "word": "substance",
        "definition": "A fundamental or characteristic part or quality",
    },
    {
        "id": "h34",
        "word": "accomplish",
        "definition": "To bring to completion",
    },
    {
        "id": "h35",
        "word": "canny",
        "definition": "clever, shrewd",
    },
    {
        "id": "h36",
        "word": "aspirant",
        "definition": "seeking to attain a desired position or status",
    },
    {
        "id": "h37",
        "word": "abhor",
        "definition": "To regard with extreme repugnance",
    },
    {
        "id": "h38",
        "word": "amiable",
        "definition": "Friendly, sociable, and congenial",
    },
    {
        "id": "h39",
        "word": "brusque",
        "definition": "Blunt in manner or speech often to the point of "
        "ungracious harshness",
    },
    {
        "id": "h40",
        "word": "coherent",
        "definition": "Having clarity or intelligibility",
    },
    {
        "id": "h41",
        "word": "fabricate",
        "definition": "To make up for the purpose of deception",
    },
    {
        "id": "h42",
        "word": "haughty",
        "definition": "Blatantly and disdainfully proud",
    },
    {
        "id": "h43",
        "word": "indolent",
        "definition": "Showing an inclination to laziness",
    },
    {
        "id": "h44",
        "word": "insatiable",
        "definition": "Incapable of being satisfied",
    },
    {
        "id": "h45",
        "word": "intrepid",
        "definition": "Characterized by resolute fearlessness, "
        "fortitude, and endurance",
    },
    {
        "id": "h46",
        "word": "gluttony",
        "definition": "Excess in eating or drinking",
    },
    {
        "id": "h47",
        "word": "eloquent",
        "definition": "Marked by forceful and fluent expression",
    },
    {
        "id": "h48",
        "word": "connive",
        "definition": "To be indulgent or in secret sympathy",
    },
    {
        "id": "h49",
        "word": "candor",
        "definition": "Unreserved, honest, or sincere expression",
    },
    {
        "id": "h50",
        "word": "callous",
        "definition": "Feeling no emotion",
    },
]
