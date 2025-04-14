# Personal Blog API - (Python + Django)

# Structure
 Blog's UI <---> Blog API <---> Database

# Features:
- Return a list of articles. You can add filters such as publishing date, or tags.
- Return a single article, specified by the ID of the article.
- Create a new article to be published.
- Delete a single article, specified by the ID.
- Update a single article, again, you’d specify the article using its ID.

# Todo List

**Phase 1: Project Setup & Basic Article Model**

1.  **[x] Set up your Django Project:**
    * [x] Created a new Django project (using `django-admin startproject your_project_name`).
    * [x] Created a new Django app for your blog (using `python manage.py startapp blog`).
    * [x] Added the 'blog' app to your `INSTALLED_APPS` in your project's `settings.py` file.

2.  **[x] Define the Article Model:**
    * [x] Opened the `models.py` file in your 'blog' app.
    * [x] Created a Django model named `Article` with the following fields (at a minimum):
        * `title` (CharField)
        * `content` (TextField)
        * `publication_date` (DateTimeField)
    * [x] Ran `python manage.py makemigrations blog` to create the database migration.
    * [x] Ran `python manage.py migrate` to apply the migration to your database.

**Phase 1.5: User Authentication Setup**

3.  **[x] Set up Django REST Framework Token Authentication:**
    * [x] Installed Django REST Framework if you haven't already (`pip install djangorestframework`).
    * [x] Added `'rest_framework'` and `'rest_framework.authtoken'` to your `INSTALLED_APPS` in `settings.py`.
    * [x] Ran `python manage.py makemigrations rest_framework` and `python manage.py migrate` to create the necessary database tables for tokens.
    * [x] Configured the default authentication classes in your project's `settings.py` file (added `REST_FRAMEWORK` settings).

4.  **[x] Create a User for your Blog API:**
    * [x] Created a superuser using Django's `python manage.py createsuperuser` command.

5.  **[x] Obtain an Authentication Token:**
    * [x] Started your Django development server (`python manage.py runserver`).
    * [x] Accessed the Django admin interface (`http://127.0.0.1:8000/admin/`).
    * [x] Logged in with your superuser credentials.
    * [x] Found your user in the "Users" section.
    * [x] Went to the "Tokens" section.
    * [x] Added a new token for your user.
    * [x] Saved the token and noted it down.

6.  **[ ] Programmatically Generating Tokens (For Later):**
    * [x] Set up API endpoints for user registration and/or login to automatically generate and return authentication tokens.

**Phase 2: Implement the "Return a list of articles" Endpoint**

7.  **[ ] Create a Serializer for the Article Model:**
    * [x] Create a new file named `serializers.py` in your 'blog' app.
    * [x] In `serializers.py`, create a Django REST Framework serializer for your `Article` model.

8.  **[ ] Create a View for Listing Articles:**
    * [x] Open the `views.py` file in your 'blog' app.
    * [x] Import the necessary modules from Django REST Framework and your `models` and `serializers`.
    * [x] Create a view (likely using a `ListAPIView` or a function-based view with `@api_view`) that:
        * Retrieves all `Article` objects from the database.
        * Serializes the `Article` objects using your `ArticleSerializer`.
        * Returns the serialized data in the response.

9.  **[ ] Define the URL for Listing Articles:**
    * [x] Create a new file named `urls.py` in your 'blog' app.
    * [x] Import `path` from `django.urls` and your view.
    * [x] Define a URL pattern (e.g., `/api/articles/`) that maps to your list articles view.
    * [x] Include your app's `urls.py` in your project's main `urls.py` file.

**Phase 3: Implement the "Return a single article" Endpoint**

10. **[ ] Create a View for Retrieving a Single Article:**
    * [x] In `views.py`, create a view (likely using a `RetrieveAPIView` or a function-based view) that:
        * Accepts an `id` as a parameter.
        * Retrieves the `Article` object with the matching ID from the database.
        * Handles the case where the article doesn't exist (return a 404 error).
        * Serializes the `Article` object.
        * Returns the serialized data.

11. **[ ] Define the URL for Retrieving a Single Article:**
    * [x] In `urls.py`, define a URL pattern (e.g., `/api/articles/<int:pk>/`) that maps to your single article view, capturing the article ID.

**Phase 4: Implement the "Create a new article" Endpoint**

12. **[ ] Create a View for Creating a New Article:**
    * [x] In `views.py`, create a view (likely using a `CreateAPIView` or a function-based view with `@api_view(['POST'])`) that:
        * **Apply Authentication:** Add the `permission_classes = [permissions.IsAuthenticated]` attribute to your view to ensure only authenticated users can access it. Import `rest_framework.permissions` as `permissions`.
        * Accepts data in the request body.
        * Deserializes the data using your `ArticleSerializer`.
        * Validates the data.
        * Saves a new `Article` object to the database if the data is valid.
        * Returns the serialized data of the newly created article (usually with a 201 Created status).

**Phase 5: Implement the "Delete a single article" Endpoint**

13. **[ ] Create a View for Deleting an Article:**
    * [ ] In `views.py`, create a view (likely using a `DestroyAPIView` or a function-based view with `@api_view(['DELETE'])`) that:
        * **Apply Authentication:** Add `permission_classes = [permissions.IsAuthenticated]` to your view.
        * Accepts an `id` as a parameter.
        * Retrieves the `Article` object with the matching ID.
        * Handles the case where the article doesn't exist (return a 404 error).
        * Deletes the `Article` object from the database.
        * Returns an appropriate response (usually a 204 No Content status).

14. **[ ] Define the URL for Deleting an Article:**
    * [ ] In `urls.py`, define a URL pattern (e.g., `/api/articles/<int:pk>/`) that maps to your delete article view (using the same URL as retrieving, but for the DELETE method).

**Phase 6: Implement the "Update a single article" Endpoint**

15. **[ ] Create a View for Updating an Article:**
    * [ ] In `views.py`, create a view (likely using an `UpdateAPIView` or a function-based view with `@api_view(['PUT', 'PATCH'])`) that:
        * **Apply Authentication:** Add `permission_classes = [permissions.IsAuthenticated]` to your view.
        * Accepts an `id` as a parameter.
        * Retrieves the `Article` object with the matching ID.
        * Handles the case where the article doesn't exist.
        * Accepts updated data in the request body.
        * Deserializes the data and updates the existing `Article` object.
        * Validates the updated data.
        * Saves the updated `Article` to the database.
        * Returns the serialized data of the updated article.

16. **[ ] Define the URL for Updating an Article:**
    * [ ] In `urls.py`, define a URL pattern (e.g., `/api/articles/<int:pk>/`) that maps to your update article view (again, using the same URL as retrieving and deleting, but for the PUT or PATCH methods).

**Phase 7: Adding Filters (Optional)**

17. **[ ] Implement Filtering for the List Articles Endpoint:**
    * [ ] In your list articles view in `views.py`, you can use Django REST Framework's filtering capabilities (e.g., `filter_backends` and `DjangoFilterBackend`) or implement custom filtering logic to allow filtering by `publication_date` or `tags` (if you add a `tags` field to your model).

**Important Notes:**

* **Authentication for API:** For an API, especially when dealing with actions like create, update, and delete, **Token Authentication** is generally preferred.
* **Take Breaks, Test Frequently, Commit Code, Focus on One Step, Celebrate Wins:** (Same as before)

