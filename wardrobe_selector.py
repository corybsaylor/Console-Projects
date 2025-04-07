import random

class Wardrobe:
    def __init__(self):
        self.wardrobe = {
            'tops': [],
            'bottoms': [],
            'shoes': [],
            'accessories': []
        }
        self.article = 'top'
        self.style = 'casual'
        self.item = 'black tee'
        self.articles = ['tops', 'bottoms', 'shoes', 'accessories']
        self.styles = ['casual', 'formal', 'business', 'party', 'random']

    def add_clothing_item(self):
        article = self.prompt_user_article()
        item = self.prompt_user_item()
        self.wardrobe[article].append(item)

    def remove_clothing_item(self):
        article = self.prompt_user_article()
        item = self.prompt_user_item()
        if item in self.wardrobe[article]:
            self.wardrobe[article].remove(item)
        else:
            print("Item not found in wardrobe.")

    def list_clothing_items(self, article=None):
        if article:
            if article in self.wardrobe:
                print(self.wardrobe[article])
            else:
                print("Invalid article.")
        else:
            print(self.wardrobe)

    def generate_outfit(self, style=None):
        try:
            top = random.choice(self.wardrobe['tops'])
            bottoms = random.choice(self.wardrobe['bottoms'])
            shoes = random.choice(self.wardrobe['shoes'])
            accessory = random.choice(self.wardrobe['accessories'])
            print(f"Top: {top}, Bottoms: {bottoms}, Shoes: {shoes}, Accessory: {accessory}")
        except IndexError:
            print("Your wardrobe is missing items in some categories!")

    def prompt_user_style(self):
        while True:
            style = input("Enter a style (casual, formal, business, party, or random): ").strip().lower()
            if style in self.styles:
                return style
            print("Invalid input. Please try again.")

    def prompt_user_article(self):
        while True:
            article = input("Enter a type of clothing category (tops, bottoms, shoes, or accessories): ").strip().lower()
            if article in self.articles:
                return article
            print("Invalid input. Please try again.")

    def prompt_user_item(self):
        return input("Enter the clothing item: ").strip()

    def display_outfit(self, style=None):
        self.generate_outfit(style)

if __name__ == '__main__':
    wardrobe = Wardrobe()
    print("Welcome to your wardrobe selector")
    while True:
        try:
            run = int(input("To exit Wardrobe Selector enter 0, To add clothing to your wardrobe enter 1, to remove enter 2, to view enter 3, and to generate an outfit enter 4: "))
            if run == 1:
                wardrobe.add_clothing_item()
            elif run == 2:
                wardrobe.remove_clothing_item()
            elif run == 3:
                article=input("Enter 1 to chose article type or 2 in order to skip: ")
                if article=='1':
                    wardrobe.list_clothing_items(wardrobe.prompt_user_article())
                else:
                    wardrobe.list_clothing_items()
            elif run == 4:
                wardrobe.generate_outfit()
            elif run == 0:
                print("Goodbye!")
                quit()
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
