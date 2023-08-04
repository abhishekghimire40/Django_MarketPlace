# Online Marketplace - DJANGO

DJANGO_MARKETPLACE is an online marketplace built with Django, allowing users to buy and sell various items. It provides an interface for managing products, categories, and conversations between buyers and sellers.

## Features

- Browse and Search: Users can easily browse through available items and search for products by title and description. They can also filter items based on specific categories, such as toys, to find relevant listings.

- Create Listings: Sellers can create new product listings by providing essential details like name, description, price, and an optional image. Listings are associated with appropriate categories for better organization.

- Inbox and Conversations: Users have an inbox that displays their conversations with other users. This feature enables direct communication between buyers and sellers, enhancing the overall buying experience.

- Dashboard Management: Sellers have access to a personalized dashboard where they can manage their listed items. They can edit, delete, or mark items as sold, ensuring accurate and up-to-date product information.

## Installation

To run the project locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/abhishekghimire40/Django_MarketPlace
```

2. Navigate to the project directory:

```bash
cd Django_MarketPlace
```

3. Create a virtual environment (recommended) and activate it:

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use "venv\Scripts\activate"
```

4. Install dependencies from requirements.txt

```bash
pip install -r requirements.txt
```

###### I have used sqlite database, if you want to use any other database then configure it in settings.py

5. Run database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser account (if needed):

```bash
python manage.py createsuperuser
```

7. Start the development server:

```bash
python manage.py runserver
```

8. Open your web browser and navigate to http://127.0.0.1:8000/ to access the application.

## Contributing

Contributions are welcome! If you find a bug or have an enhancement idea, please open an issue or submit a pull request. You can also add functionality, make project your own and add it to your github