# ZhiQu - Gamified Learning Platform based on Django Framework

#### Introduction
A gamified learning website implemented based on the **Django** framework, integrated with frontend **HTML, CSS, and JavaScript**.

The project offers diverse features, allowing users to register, log in, create and display tasks/to-do items, and chat with AI characters. It includes data visualization pages and adopts a reward mechanism with Gold Coins and Experience Points (XP). Gold Coins can be used to purchase equipment in the shop. It is also configured with a backend management system.

---

#### Tech Stack
Python, Django, HTML, CSS, JavaScript

---

#### Project Functions
##### Core Features

1. **User Registration & Login**
   - Users can create accounts via the registration function and use them to log in to the system.
   - After login, user information is maintained using **Django's Session framework** to facilitate subsequent operations.

2. **Task Management**
   - **Daily Tasks**: Users can create, view, and complete daily tasks to earn **Gold Coins and XP rewards**.
   - **To-Do Items**: Users can add to-do items and mark them as checked upon completion.

3. **AI NPC Chat**
   - Integrated **Inworld AI**. Users can converse with NPCs possessing distinct personalities and backstories, enhancing interactivity and fun.

4. **Equipment System**
   - Users can use Gold Coins to purchase equipment to increase their character's **Attack and Defense stats**.

5. **Data Visualization**
   - **Capability Radar Chart**: Displays the user's comprehensive capability metrics.
   - **Event Overview**: Displays user daily tasks and to-do items using a network graph.
   - **Completion Status**: Statistics on the completion of to-do items.
   - **Daily Stats**: Displays the count of daily tasks and to-do items.

6. **Backend Management System**
   - Administrators can perform **CRUD (Create, Read, Update, Delete)** operations on users, equipment, tasks, and other data via the Django Admin interface.

---

#### Project Structure

##### Key File Descriptions

- **`project01/`**: Project root directory, containing all source code and configuration files.
  - **`project01/`**: Django project configuration directory.
    - `settings.py`: Global project settings (database, middleware, static file paths, etc.).
    - `urls.py`: Main project URL configuration.
    - `__init__.py`: Python package marker file.
    - `wsgi.py`
    - `asgi.py`
  - **`manage.py`**: Django command-line utility for starting the server, database migrations, etc.
  - **`templates/`**: Directory for Django template files (HTML frontend pages).
  - **`static/`**: Directory for static assets, including CSS stylesheets, JavaScript scripts, and images.
  - **`TestModel/`**: Custom Django application directory implementing user auth and core modules.
    - `models.py`: Defines database models (e.g., `UserInfo`, `TaskInfo`).
    - `views.py`: View functions handling business logic.
    - `admin.py`: Backend admin site configuration.
    - `apps.py`
    - `tests.py`
    - `migrations/`: Database migration record files.
  - **`db.sqlite3`**: SQLite database file storing user data, tasks, equipment info, etc.
  - **`project01.iml`**: JetBrains IDE configuration file (can be ignored).

- **`Django.pdf`**: Django study notes compiled during early development (optional file).

---

#### Database Design

##### Core Tables
- **`UserInfo`**: User information table, storing basic user details, equipment, tasks, and to-do items.
- **`EquipmentInfo`**: Equipment information table, storing equipment attributes and descriptions.
- **`TaskInfo`**: Task information table, storing details of daily tasks.
- **`TodoInfo`**: To-Do information table, storing details of to-do items.
