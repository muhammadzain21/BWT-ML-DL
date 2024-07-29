from .FoodItem import FoodItem
from .FileManager import FileHandler
import datetime

class Inventory:
    def __init__(self,file_handler):
        self.items=[]
        self.file_handler=file_handler
        self.items=self.file_handler.load_from_file()
        self._index=0
        
    def __iter__(self):
        self._index = 0
        return self
   # Here is the Implemention of Iterator
    def __next__(self):
        if self._index < len(self.items):
            item = self.items[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
        
        
    def Add_Item(self,Food_Item):
        self.items.append(Food_Item)
        self.file_handler.save_to_file(self.items)
        
    def Edit_Item(self,barcode,name=None,category=None,quantity=None,expiredate=None):
        for item in self.items:
            if item.barcode == barcode:
                if name is not None:
                    item.barcode=name
                if category is not None:
                    item.category=category
                if quantity is not None:
                    item.quantity=quantity
                if expiredate is not None:
                    item.expiredate=expiredate
                self.file_handler.save_to_file(self.items)
            return True
        return False
    
    def Search_Item_(self,barcode=None, name=None):
       results = []
       for item in self.items:
            if barcode is not None and item.barcode == barcode:
                results.append(item)
            elif name is not None and item.name.lower() == name.lower():
                results.append(item)
       return results
   # Implementation of Searching of Task 5 you have to Give One argument from name barcode and category then it check 
   #which argument is given and then append matched item to an array result
    def Search_Item(self, barcode=None, name=None, category=None):
        results = []
        for item in self.items:
            if barcode is not None and item.barcode == barcode:
                results.append(item)
            elif name is not None and item.name.lower() == name.lower():
                results.append(item)
            elif category is not None and item.category.lower() == category.lower():
                results.append(item)
        return results
    
    def Delete_Item(self,barcode):
        for item in self.items:
            if item.barcode == barcode:
                self.items.remove(item)
                self.file_handler.save_to_file(self.items)
                return True
        return False
    def Near_Expiry_Items(self, days=7):
        near_expiry = []
        current_date = datetime.date.today()
        for item in self.items:
            if item.expiredate - current_date <= datetime.timedelta(days=days):
                near_expiry.append(item)
        return near_expiry
    def near_expiry_generator(self, days=7):
        current_date = datetime.date.today()
        for item in self.items:
            if item.expiredate - current_date <= datetime.timedelta(days=days):
                yield item
                
    def generate_report_near_expiry(self, days=7):
        near_expiry = self.Near_Expiry_Items(days)
        report = "Items Nearing Expiry:\n"
        for item in near_expiry:
            report += f"{item}\n"
        return report

    def generate_report_low_stock(self, threshold=10):
        low_stock = [item for item in self.items if item.quantity <= threshold]
        report = "Items in Low Stock:\n"
        for item in low_stock:
            report += f"{item}\n"
        return report
    # Here is the Final summary Function which Generate Summary by Firstly Create a Array for Category and then Append each 
    #Category to it and initialize the total quantity to 0 and create a items Array for the item which is of its Category
    #the it append the item to it and add its quantity for the total quantity of Category then is simply display it
    def generate_category_summary(self):
        category_summary = {}
        for item in self.items:
            if item.category not in category_summary:
                category_summary[item.category] = {
                    "total_quantity": 0,
                    "items": []
                }
            category_summary[item.category]["total_quantity"] += item.quantity
            category_summary[item.category]["items"].append(item)
        
        report = "Category-based Summary:\n"
        for category, data in category_summary.items():
            report += f"Category: {category}\n"
            report += f"Total Quantity: {data['total_quantity']}\n"
            report += "Items:\n"
            for item in data["items"]:
                report += f"  {item}\n"
                
        return report