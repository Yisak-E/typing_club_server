class Normalizer:
    def __init__(self, raw):
        self.raw = raw
        pass

    def normalize_news(self):
        # split into paragraphs based on double newlines
        paragraphs = [p.strip() for p in self.raw.split("\n\n") if p.strip()]

        headline = ""
        date = ""
        boby = []

        filtered_paragraphs = []
        for p in paragraphs:

            if p in ["**FOR IMMEDIATE RELEASE**", "###", "**###**"]:
                continue

            if p.startswith("***") and p.endswith("***") and any(char.isdigit() for char in p):
                p = p.strip("*")

                filtered_paragraphs.append(p)

        paragraphs = filtered_paragraphs

        if len(paragraphs) >= 3:
            if any(char.isdigit() for char in paragraphs[0]):
                date = paragraphs[0]
                headline = paragraphs[1]
                boby = paragraphs[2:]
            else:
                headline = paragraphs[0]
                date = paragraphs[1]
                boby = paragraphs[2:]
        elif len(paragraphs) == 2:
            if any(char.isdigit() for char in paragraphs[1]):
                date = paragraphs[1]
                headline = paragraphs[0]
            else:
                headline = paragraphs[0]
                body = paragraphs[1:]

        elif len(paragraphs) == 1:
            headline = paragraphs[0]


        return {
            "headline": headline,
            "date": date,
            "boby": boby
        }
