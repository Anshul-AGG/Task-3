import requests
from bs4 import BeautifulSoup
import os


def scrape_headlines():
    URL = "https://www.bbc.com/news"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    FILE_NAME = "Headlines.txt"

    try:
        print(f"Fetching data from : {URL}")
        response = requests.get(URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        main_content = soup.find("div", class_="sc-cd6075cf-0 kxYTiV")

        headlines = []

        if main_content:
            headline_tags = main_content.find_all("h2")

            print(
                f"Found {len(headline_tags)} headline elements within the specific DIV."
            )

            for tag in headline_tags:
                headline_text = tag.text.strip()

                if headline_text and headline_text not in headlines:
                    headlines.append(headline_text)

            print(f"Filtered down to {len(headlines)} unique headlines.")

        else:
            print(
                "Error: Could not find headline elements with the specified class."
            )

        with open(FILE_NAME, "w", encoding="utf-8") as f:
            for index, headline in enumerate(headlines, 1):
                line = f"{index}. {headline}\n"
                f.write(line)

        print(f"Success! Fetched {len(headlines)} unique headlines.")
        print(f"Headlines saved to: {os.path.abspath(FILE_NAME)}")

    except Exception as e:
        print(f" An unexpected error occurred: {e}")


if __name__ == "__main__":
    scrape_headlines()
