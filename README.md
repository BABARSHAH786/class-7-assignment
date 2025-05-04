# 🇵🇰 Pakistani Sweet Shop Hub

This is a Streamlit web application designed for owners of Pakistani sweet shops to manage their inventory, complete with images of the delicious treats. It utilizes Object-Oriented Programming (OOP) principles for a structured and maintainable codebase.

## Features:

* **View Inventory with Images:** Displays all the Pakistani sweet items currently in stock with their details (name, category, price, quantity) and a visual representation (image) of the sweet.
* **Add New Sweet:** Allows the user to add new Pakistani sweet items to the inventory, including the filename of the sweet's image.
* **Sell Sweet:** Enables the user to record sales, updating the quantity of the selected sweet in the inventory.

## How to Run:

1.  **Prerequisites:**
    * Python 3.6 or higher installed on your system.
    * Streamlit library installed. You can install it using pip:
        ```bash
        pip install streamlit
        ```
    * **Images:** Create a folder named `images` in the same directory as your `app.py` file. Place image files of your Pakistani sweets (e.g., `gulab_jamun.jpg`, `jalebi.jpg`, `barfi.jpg`) inside this `images` folder. Ensure the filenames you enter in the application match the actual image filenames.

2.  **Save the code:** Save the Python code provided in the `app.py` file in the main project directory.

3.  **Navigate to the directory:** Open your terminal or command prompt and navigate to the main project directory (`sweet_shop_app/`).

4.  **Run the application:** Execute the following command:
    ```bash
    streamlit run app.py
    ```

    This command will start the Streamlit development server and automatically open the application in your default web browser.

## OOP Principles Applied:

* **Encapsulation:** The `Sweet` and `PakistaniSweet` classes encapsulate the data and behavior of each sweet item, including the image path.
* **Abstraction:** Users interact with simple actions without needing to know the underlying image handling.
* **Inheritance:** `PakistaniSweet` inherits from the base `Sweet` class and adds specific handling for image paths relevant to Pakistani sweets.
* **Polymorphism:** The `display_details()` method is extended to include image display.

## Further Enhancements (Potential Future Features):

* Order Management for Pakistani sweets.
* Categorization of sweets (e.g., Mithai, Halwa, etc.).
* Inventory alerts for low stock.
* Data persistence for the inventory.
* Detailed product pages with larger images and descriptions."# class-7-assignment" 
