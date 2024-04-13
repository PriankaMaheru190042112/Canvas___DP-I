
# Canvas
## Overview
Canvas is a web application designed for hosting and participating in virtual exhibitions. It allows organizations to create events, upload images, and set event schedules. Admins can approve event creation requests from organizations, while users can browse events, filter them by category, and purchase items from exhibitions.


## Features

1. Organization: Create events by uploading images and setting event schedule.

2. Admin :Approves event creation requests submitted by organizations to ensure quality exhibitions.

3. User:
- Browse Events: Users can view events displayed on their feed.
- Filter Events: Filter events by category to find exhibitions of interest.
- Purchase Items: Users can buy items from exhibitions directly through the platform.




## Technologies

Frontend: HTML, CSS, JS

Backend:  Django framework 
## Installation

1. Navigate to the project directory:
```bash
cd code/canvas
```
2. Create superuser:
```
python manage.py createsuperuser
```

3. Apply database migration:
```
python manage.py migrate
```

4. Start the Django development server:
```
python manage.py runserver
```
Execute these and  navigate to http://localhost:8000 to access the application.
