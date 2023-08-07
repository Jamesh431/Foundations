import wikipedia

search = input("What would you like to search on wikipedia?: ")

print(wikipedia.summary(search))
# Plain text summary of the page.

print(wikipedia.page(search).section)
# Get the plain text content of a section from self.sections. Returns None if section_title isn’t found, otherwise returns a whitespace stripped string. This is a convenience method that wraps self.content.

print(wikipedia.page(search).url)
# gives link to the wikipedia page

# print(wikipedia.WikipediaPage(search).sections)
# does not work, me and john tried making it work and we concluded it might just be broken as it only prints "[]"

print(wikipedia.page(search).content)
# Plain text content of the page, excluding images, tables, and other data.

print(wikipedia.WikipediaPage(search).references)
# List of URLs of external links on a page. May include external links within page that aren’t technically cited anywhere.


###################################### HOW JOHN DID IT BELOW

# John Ipson - Wikipedia Module Assignment - Chapter 11
# main.py - File 1/2

import wikipedia
from functions import wiki_results, wiki_page_summary

while True:

    user_query = input("Please enter a search term: ")

    results = wiki_results(user_query)

    user_selection = int(
        input(f"\nWhich item number would you like to know more about? ")
    )
    outcome = wiki_page_summary(results, user_selection)

    while True:

        if outcome == "m":
            print("\n")
            outcome = wiki_page_summary(results, user_selection, True)

        elif outcome == "v":
            print("\n")
            results = wiki_results(user_query)
            user_selection = int(
                input(f"\nWhich item number would you like to know more about? ")
            )
            outcome = wiki_page_summary(results, user_selection)
            continue

        elif outcome == "s":
            break


# John Ipson - Wikipedia Module Assignment - Chapter 11
# functions.py File 2/2

import wikipedia


def wiki_results(search_term, wanted_results_num=5):
    # takes user input and defaults to 5 results returned as a numbered list.
    search_results = wikipedia.search(search_term, results=wanted_results_num)
    result_count = 1
    for i in search_results:
        print(f"{result_count}) {i}")
        result_count += 1
    return search_results


def wiki_page_summary(search_results, user_selection, more_info=False):
    # imports list and item unumber that user chooses from wiki_results and then returns a summary page or page with more info if requested.

    while True:

        if more_info == False:
            # returns wikipedia page summary for selection, limited to 5 sentences
            print("\n")
            print(
                wikipedia.summary(
                    search_results[user_selection - 1],
                    sentences=5,
                    auto_suggest=False,
                    redirect=False,
                )
            )
            print("\n")
            another_search = input(
                "\nWould you like (m)ore information, to (v)iew another page, (s)earch for something else, or (q)uit? "
            )

        else:
            # returns non limited page summary if more information is requested by user. Ommits the 'm' option as this is the more information page.
            print("\n")
            print(
                wikipedia.summary(
                    search_results[user_selection - 1],
                    auto_suggest=False,
                    redirect=False,
                )
            )
            print("\n")
            another_search = input(
                "\nWould you like to (v)iew another page, (s)earch for something else, or (q)uit? "
            )

        # After More info output or not, return correct value for menu options.
        if another_search.lower() == "m":
            return "m"

        elif another_search.lower() == "v":
            return "v"

        elif another_search.lower() == "s":
            return "s"

        elif another_search.lower() == "q":
            print("Goodbye!")
            quit()
        else:
            print("Invalid Selection. Please try a valid response.")
