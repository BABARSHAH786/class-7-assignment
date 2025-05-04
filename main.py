import streamlit as st
import os

class Sweet:
    def __init__(self, name, category, price, quantity, image_path=None):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.image_path = image_path

    def display_details(self):
        details = f"**{self.name}** ({self.category}) - Price: ${self.price:.2f}, Quantity: {self.quantity}"
        if self.image_path and os.path.exists(self.image_path):
            details += f'\n![{self.name}]({self.image_path})'
        return details

    def update_quantity(self, change):
        self.quantity += change
        if self.quantity < 0:
            self.quantity = 0
            st.warning(f"Quantity for {self.name} cannot be negative.")

class BabarSweet(Sweet):
    def __init__(self, name, price, quantity, image_name):
        image_path = f"images/{image_name}"
        super().__init__(name, "Pakistani Sweet", price, quantity, image_path)

class SweetShop:
    def __init__(self):
        self.inventory = {}

    def add_sweet(self, sweet):
        if sweet.name in self.inventory:
            st.warning(f"{sweet.name} already exists in the inventory. Consider updating quantity.")
        else:
            self.inventory[sweet.name] = sweet
            st.success(f"Added {sweet.name} to inventory.")

    def remove_sweet(self, sweet_name):
        if sweet_name in self.inventory:
            del self.inventory[sweet_name]
            st.warning(f"Removed {sweet_name} from inventory.")
        else:
            st.error(f"{sweet_name} not found in inventory.")

    def get_sweet(self, sweet_name):
        return self.inventory.get(sweet_name)

    def display_inventory(self):
        st.header("BABAR Sweet Shop🍨 ")
        if self.inventory:
            for name, sweet in self.inventory.items():
                st.markdown(sweet.display_details())
        else:
            st.info("Inventory is empty.")

    def sell_sweet(self, sweet_name, quantity):
        sweet = self.get_sweet(sweet_name)
        if sweet:
            sweet.update_quantity(-quantity)
        else:
            st.error(f"{sweet_name} not found in inventory.")

def main():
    st.title("BABAR Sweet Shop🍨")
    sweet_shop = SweetShop()

    # Sample Sweet Inventory
    if not sweet_shop.inventory:
        sweet_shop.add_sweet(BabarSweet("Gulab Jamun (6pcs)", 3.50, 30, "gulab_jamun.jpg"))
        sweet_shop.add_sweet(BabarSweet("Jalebi (250g)", 2.00, 50, "jalebi.jpg"))
        sweet_shop.add_sweet(BabarSweet("Barfi (500g)", 5.00, 25, "barfi.jpg"))
        # Add more  sweets here

    with st.sidebar:
        st.header("⚙️ Actions")
        action = st.selectbox("Choose an action:", ["View Inventory", "Add New Sweet", "Sell Sweet"])

        if action == "Add New Sweet":
            st.subheader("➕ Add New Sweet")
            name = st.text_input("Name:")
            price = st.number_input("Price:", min_value=0.01)
            quantity = st.number_input("Quantity:", min_value=0, step=1)
            image_name = st.text_input("Image Filename (e.g., gulab_jamun.jpg):")
            if st.button("Add Sweet"):
                sweet_shop.add_sweet(BabarSweet(name, price, quantity, image_name))

        elif action == "Sell Sweet":
            st.subheader("💸 Sell Sweet")
            sweet_name = st.selectbox("Select Sweet:", list(sweet_shop.inventory.keys()))
            sell_quantity = st.number_input("Quantity to Sell:", min_value=1, step=1)
            if st.button("Sell"):
                sweet_shop.sell_sweet(sweet_name, sell_quantity)

    if st.sidebar.button("🔄 Refresh Inventory"):
        st.experimental_rerun()

    sweet_shop.display_inventory()

if __name__ == "__main__":
    main()