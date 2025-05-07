# Dalilah_Backend

This project represents the backend system for the Dalilah application, a platform where users can explore cities, browse local places by category, save their favorite spots, and share their experiences through reviews.

---

## Entity Relationship Diagram (ERD)

The following diagram illustrates the relationships between the main models (User, City, Category, Place, Review):

<img width="100%" src="assets/dalilah_ERD.png" />

---

# RESTful Routing

RESTful routing stands for **Representational State Transfer** and uses our resources (entities in our database) as the focal point of how to organize our code. It emphasizes treating data as the single source of truth, ensuring that our client requests interact properly with server endpoints through CRUD operations:

- (C) Create
- (R) Read
- (U) Update
- (D) Delete

The following tables outline the main routes used for interacting with the Dalilah API resources.

---

## User Authentication
<table border="1">
<tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
<tr><td>POST</td><td>/users/signup/</td><td>signup</td><td>Register a new user</td></tr>
<tr><td>POST</td><td>/users/login/</td><td>login</td><td>User login and return tokens</td></tr>
<tr><td>GET</td><td>/users/token/refresh/</td><td>refresh</td><td>Refresh the JWT token</td></tr>
</table>

---

## Cities
<table border="1">
<tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
<tr><td>GET</td><td>/cities/</td><td>index</td><td>List all cities</td></tr>
<tr><td>GET</td><td>/cities/:city_id/</td><td>show</td><td>Show details of a specific city</td></tr>
</table>

---

## Categories
<table border="1">
<tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
<tr><td>GET</td><td>/categories/</td><td>index</td><td>List all categories</td></tr>
<tr><td>GET</td><td>/categories/:category_id/</td><td>show</td><td>Show details of a specific category</td></tr>
</table>

---

## Places
<table border="1">
<tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
<tr><td>GET</td><td>/places/</td><td>index</td><td>List all places</td></tr>
<tr><td>POST</td><td>/places/</td><td>create</td><td>Add a new place (select city and category)</td></tr>
<tr><td>GET</td><td>/places/:place_id/</td><td>show</td><td>Show a specific place details</td></tr>
<tr><td>PUT/PATCH</td><td>/places/:place_id/</td><td>update</td><td>Update an existing place</td></tr>
<tr><td>DELETE</td><td>/places/:place_id/</td><td>destroy</td><td>Delete a place</td></tr>
</table>

---

## Reviews
<table border="1">
<tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
<tr><td>POST</td><td>/reviews/</td><td>create</td><td>Create a review for a place</td></tr>
<tr><td>GET</td><td>/reviews/</td><td>index</td><td>List all reviews (for explore section)</td></tr>
</table>

---

# User Stories

## Visitor

- As a Visitor, I want to explore random reviews from other users, so that I can get inspired to visit interesting places without needing to log in.

- As a Visitor, I want to sign up and create an account, so that I can add places, write reviews, and save favorite spots.

- As a Visitor, I want to log in using my credentials, so that I can access my saved places and interact more with the application.

---

## Registered User

- As a Registered User, I want to browse all available cities, so that I can select one and explore its places.

- As a Registered User, I want to select a category within a city (such as cafes, restaurants), so that I can filter places based on my interest.

- As a Registered User, I want to view a list of places within a selected city and category, so that I can find locations that interest me.

- As a Registered User, I want to click on a place and view its detailed information, so that I can learn more about the place.

- As a Registered User, I want to add a new place by filling out a form, so that I can share great locations I know with others.

- As a Registered User, I want to select the city and category from dropdown menus when adding a place, so that the data stays organized and consistent.

- As a Registered User, I want to write a review for a specific place, so that I can share my personal experience and help guide others.

- As a Registered User, I want to explore all user reviews, so that I can discover recommended and popular places easily.



---

## Tech Stack

- **Backend Framework:** Django REST Framework  
- **Database:** PostgreSQL  
- **Authentication:** JWT (JSON Web Tokens)  
- **Deployment:** Docker  
- **Additional Tools:** Django CORS Headers (for Cross-Origin requests)

---

## Frontend Repository Link

[Dalilah Frontend Repository](<ضع رابط مستودع الـFrontend هنا>)

---

## Link to Deployed Site

[Dalilah Application Live Link](<ضع رابط الموقع المباشر هنا>)

---

## Installation Instructions (Docker)

To run the backend locally using Docker, follow these instructions:

### 1. Clone the repository:
```bash
git clone <backend-repo-url>
cd dalilah_backend


IceBox Features

- [ ] **Image Uploads:** Allow users to upload images for places.
- [ ] **Google Maps Integration:** Display interactive maps showing the location of each place.
- [ ] **User Profiles:** Provide public user profiles that display their reviews and places they've added.
- [ ] **Real-Time Notifications:** Notify users instantly when new places or reviews are added.
- [ ] **Social Media Sharing:** Enable users to share places and reviews directly to social media platforms.
