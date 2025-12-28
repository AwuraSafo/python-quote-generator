import random

def load_quotes(filename):
    with open(filename, "r") as file:
        quotes = file.readlines()
    return quotes

def show_random_quote(quotes):
    quote = random.choice(quotes)
    print(quote.strip())

def main():
    quotes = load_quotes("quotes.txt")
    show_random_quote(quotes)

if __name__ == "__main__":
    main()
