import csv
import datetime
from .FoodItem import FoodItem

class FileHandler:
    def __init__(self, filename='F:/Bitwise ML DL Intership/BWT-ML-DL-Track/week 4/inventory.csv'):
        self.filename = filename

    def load_from_file(self):
        items = []
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # skip empty rows
                        name, category, quantity, barcode, expiry_date = row
                        expiry_date = datetime.datetime.strptime(expiry_date, '%Y-%m-%d').date()
                        items.append(FoodItem(name, category, int(quantity), barcode, expiry_date))
        except FileNotFoundError:
            print(f"{self.filename} not found. Starting with an empty inventory.")
        except Exception as e:
            print(f"Error loading from file: {e}")
        return items

    def save_to_file(self, items):
        try:
           
            with open("F:/Bitwise ML DL Intership/BWT-ML-DL-Track/week 4/Output.csv", mode='w', newline='') as file:
                writer = csv.writer(file)
                for item in items:
                    print(item)
                    writer.writerow([item.name, item.category, item.quantity, item.barcode, item.expiredate])
        except Exception as e:
            print(f"Error saving to file: {e}")
