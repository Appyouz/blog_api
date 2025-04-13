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

1.  **[ ] Set up your Django Project:**
    * [x] Create a new Django project (using `django-admin startproject your_project_name`).
    * [x] Create a new Django app for your blog (using `python manage.py startapp blog`).
    * [x] Add the 'blog' app to your `INSTALLED_APPS` in your project's `settings.py` file.

2.  **[ ] Define the Article Model:**
    * [ ] Open the `models.py` file in your 'blog' app.
    * [ ] Create a Django model named `Article` with the following fields (at a minimum):
        * `title` (CharField)
        * `content` (TextField)
        * `publication_date` (DateTimeField)
    * [ ] Run `python manage.py makemigrations blog` to create the database migration.
    * [ ] Run `python manage.py migrate` to apply the migration to your database.

**Phase 1.5: User Authentication Setup**

3.  **[ ] Set up Django REST Framework Token Authentication:**
    * [ ] Install Django REST Framework if you haven't already (`pip install djangorestframework`).
    * [ ] Add `'rest_framework'` and `'rest_framework.authtoken'` to your `INSTALLED_APPS` in `settings.py`.
    * [ ] Run `python manage.py makemigrations rest_framework` and `python manage.py migrate` to create the necessary database tables for tokens.
    * [ ] In your project's `settings.py` file, configure the default authentication classes for Django REST Framework:
        ```python
        REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': [
                'rest_framework.authentication.TokenAuthentication',
                'rest_framework.authentication.SessionAuthentication', # Optional, for browser-based API access
            ],
            'DEFAULT_PERMISSION_CLASSES': [
                'rest_framework.permissions.IsAuthenticatedOrReadOnly', # Default permission
            ]
        }
        ```
        * `TokenAuthentication`: For authenticating requests using tokens.
        * `SessionAuthentication`: Optional, allows you to authenticate using Django's session if you have a web frontend.
        * `IsAuthenticatedOrReadOnly`: Allows unauthenticated users to perform read-only requests (GET, HEAD, OPTIONS) but requires authentication for write operations (POST, PUT, DELETE).

4.  **[ ] Create a User for your Blog API:**
    * [ ] You can create a superuser using Django's `python manage.py createsuperuser` command. This user can then be used to generate tokens.
    * [ ] Alternatively, you can create regular users through Django's admin interface (after running `python manage.py createsuperuser` and accessing `/admin/`).

5.  **[ ] Obtain an Authentication Token:**
    * [ ] For Token Authentication, you'll typically generate tokens for your users. One way to do this is by using Django's admin interface. When you create or edit a user, there will be a "Tokens" section where you can create a new token for that user.
    * [ ] Programmatically generating tokens can also be done (we can add this later if needed).

**Phase 2: Implement the "Return a list of articles" Endpoint**

6.  **[ ] Create a Serializer for the Article Model:**
    * [ ] Create a new file named `serializers.py` in your 'blog' app.
    * [ ] In `serializers.py`, create a Django REST Framework serializer for your `Article` model.

7.  **[ ] Create a View for Listing Articles:**
    * [ ] Open the `views.py` file in your 'blog' app.
    * [ ] Import the necessary modules from Django REST Framework and your `models` and `serializers`.
    * [ ] Create a view (likely using a `ListAPIView` or a function-based view with `@api_view`) that:
        * Retrieves all `Article` objects from the database.
        * Serializes the `Article` objects using your `ArticleSerializer`.
        * Returns the serialized data in the response.

8.  **[ ] Define the URL for Listing Articles:**
    * [ ] Create a new file named `urls.py` in your 'blog' app.
    * [ ] Import `path` from `django.urls` and your view.
    * [ ] Define a URL pattern (e.g., `/api/articles/`) that maps to your list articles view.
    * [ ] Include your app's `urls.py` in your project's main `urls.py` file.

**Phase 3: Implement the "Return a single article" Endpoint**

9.  **[ ] Create a View for Retrieving a Single Article:**
    * [ ] In `views.py`, create a view (likely using a `RetrieveAPIView` or a function-based view) that:
        * Accepts an `id` as a parameter.
        * Retrieves the `Article` object with the matching ID from the database.
        * Handles the case where the article doesn't exist (return a 404 error).
        * Serializes the `Article` object.
        * Returns the serialized data.

10. **[ ] Define the URL for Retrieving a Single Article:**
    * [ ] In `urls.py`, define a URL pattern (e.g., `/api/articles/<int:pk>/`) that maps to your single article view, capturing the article ID.

**Phase 4: Implement the "Create a new article" Endpoint**

11. **[ ] Create a View for Creating a New Article:**
    * [ ] In `views.py`, create a view (likely using a `CreateAPIView` or a function-based view with `@api_view(['POST'])`) that:
        * **Apply Authentication:** Add the `permission_classes = [permissions.IsAuthenticated]` attribute to your view to ensure only authenticated users can access it. Import `rest_framework.permissions` as `permissions`.
        * Accepts data in the request body.
        * Deserializes the data using your `ArticleSerializer`.
        * Validates the data.
        * Saves a new `Article` object to the database if the data is valid.
        * Returns the serialized data of the newly created article (usually with a 201 Created status).

**Phase 5: Implement the "Delete a single article" Endpoint**

12. **[ ] Create a View for Deleting an Article:**
    * [ ] In `views.py`, create a view (likely using a `DestroyAPIView` or a function-based view with `@api_view(['DELETE'])`) that:
        * **Apply Authentication:** Add `permission_classes = [permissions.IsAuthenticated]` to your view.
        * Accepts an `id` as a parameter.
        * Retrieves the `Article` object with the matching ID.
        * Handles the case where the article doesn't exist (return a 404 error).
        * Deletes the `Article` object from the database.
        * Returns an appropriate response (usually a 204 No Content status).

13. **[ ] Define the URL for Deleting an Article:**
    * [ ] In `urls.py`, define a URL pattern (e.g., `/api/articles/<int:pk>/`) that maps to your delete article view (using the same URL as retrieving, but for the DELETE method).

**Phase 6: Implement the "Update a single article" Endpoint**

14. **[ ] Create a View for Updating an Article:**
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

15. **[ ] Define the URL for Updating an Article:**
    * [ ] In `urls.py`, define a URL pattern (e.g., `/api/articles/<int:pk>/`) that maps to your update article view (again, using the same URL as retrieving and deleting, but for the PUT or PATCH methods).

**Phase 7: Adding Filters (Optional)**

16. **[ ] Implement Filtering for the List Articles Endpoint:**
    * [ ] In your list articles view in `views.py`, you can use Django REST Framework's filtering capabilities (e.g., `filter_backends` and `DjangoFilterBackend`) or implement custom filtering logic to allow filtering by `publication_date` or `tags` (if you add a `tags` field to your model).

**Important Notes (Updated):**

* **Authentication for API:** For an API, especially when dealing with actions like create, update, and delete, **Token Authentication** is generally preferred over Django's form-based authentication (like `UserCreationForm`, `AuthenticationForm`, `login`, `logout`). This is because APIs are often stateless and need a way to authenticate each request independently. Tokens serve this purpose well.
* **Take Breaks, Test Frequently, Commit Code, Focus on One Step, Celebrate Wins:** (Same as before)

