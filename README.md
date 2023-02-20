# Django Library

## Description
This project is a library management system built using Django, where users can browse books, borrow and return books, and librarians can manage books and book loans.

## Installation

1. Clone the repository: `git clone https://github.com/mlk-chess/django-library.git`
2. Navigate to the project directory: `cd django-library`
3. Create a virtual environment: `python3 -m venv env`
4. Activate the virtual environment: `source env/bin/activate`
5. Install the required packages: `pip install -r requirements.txt`
6. Run the database migrations: `python manage.py migrate`
7. Create a superuser: `python manage.py createsuperuser`
8. Start the development server: `python manage.py runserver`

Alternatively, you can use Docker to run the project:

1. Install Docker and Docker Compose
2. Clone the repository: `git clone https://github.com/mlk-chess/django-library.git`
3. Navigate to the project directory: `cd django-library`
4. Build and start the Docker containers: `docker-compose up --build`

## Usage

After completing the installation steps, you can access the library management system at `http://localhost:8000/`. 

The home page displays a list of all books in the library. From here, you can browse books by clicking on their titles, and see more details such as the book's author, publication date, and availability.

To borrow a book, you must first log in with a user account. If you don't have an account, you can create one by clicking the "Sign up" link in the top navigation bar. After logging in, you can borrow a book by clicking the "Borrow" button on the book's detail page.

To return a book, go to the "My Loans" page by clicking the link in the top navigation bar. From here, you can see a list of all the books you've borrowed, and click the "Return" button to return any book that you currently have borrowed.

Librarians can manage the books and book loans through the Django admin interface, which can be accessed by logging in as a superuser at `http://localhost:8000/admin/`.

## Contributing

This project is open to contributions. To contribute, please fork the repository, create a new branch, make your changes, and then create a pull request. All contributions are welcome!

## Screenshots

### Home Page
![Home Page](screenshots/home.png)

### Book Detail Page
![Book Detail Page](screenshots/book_detail.png)

### Borrow Book
![Borrow Book](screenshots/borrow_book.png)

### My Loans Page
![My Loans Page](screenshots/my_loans.png)

### Admin Interface
![Admin Interface](screenshots/admin.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
