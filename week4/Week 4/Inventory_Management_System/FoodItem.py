class FoodItem:
    def __init__(self,name,category,quantity,barcode,expiredate):
        self.name=name
        self.category=category
        self.quantity=quantity
        self.barcode=barcode
        self.expiredate=expiredate
    def __repr__(self):
        return f"FoodItem(name={self.name}, category={self.category}, quantity={self.quantity}, barcode={self.barcode}, expiry_date={self.expiredate})"
        