# admaren-interview

_______________________________________Question_____________________________________

Develop a text saving and retrieval web app using Django. The app should be able to save short text
snippets with a title, timestamp and created user. The snippet should also contain a relation to a Tag
model (simple model with only title field). Tag title should be unique. Do not create tags for every snippet,
check whether the tag with the same title exists or not before creating a new one. If the same tag exists
link to that tag. Implement JWT authentication for getting user.
Expected output format: GitHub repository URL.
Authentication API:
1. Login API
2. Refresh API
CRUD APIs:
1. Overview API (total count, listing)
Total number of snippet and list all available snippets with a hyperlink to respective detail APIs.
2. Create API
API to collect the snippet information and save the data to DB.
3. Detail API
API should display the snippet title, content, and timestamp information.
4. Update API
API to update individual items. Update API should return item detail response.

5. Delete API
API to delete selected items and return the list of items as response.
6. Tag list API
API to list tags
7. Tag Detail API
API to return snippets linked to the selected tag.

______________________________________Text Saving and Retrieval Web App______________________________


This web app allows users to save and retrieve short text snippets. It is developed using Django, a Python web framework. The app provides the following features:

______________________________________Functionality___________________________________________________

______________________________________Authentication:_________________________________________________

Login API: Allows users to log in and obtain an access token for authentication.
Refresh API: Provides a way to refresh the access token.

______________________________________CRUD Operations:______________________________________________

Overview API: Retrieves the total count of snippets and lists all available snippets with links to their respective detail APIs.
Create API: Enables users to save a new text snippet with a title, timestamp, and created user information. The snippet can be associated with one or more tags.
Detail API: Displays detailed information about a specific snippet, including the title, content, and timestamp.
Update API: Allows users to update individual snippet items. Returns the updated item details.
Delete API: Deletes selected snippet items and returns the updated list of items as a response.
Tag list API: Lists all available tags.
Tag Detail API: Returns the snippets linked to a selected tag.

________________________________________Project Setup______________________________________________

To set up the project locally, follow these steps:

1.Clone the repository:
 git clone 
2.Navigate to the project directory:
  cd admaren interview 
3.Activate the virtual environment:
   venv\Scripts\activate
4.Install the project dependencies:
    pip install -r requirements.txt
5.Set up the database:
    python manage.py makemigrations
    python manage.py migrate
6.Run the development server:
    python manage.py runserver
