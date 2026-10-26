# Farmers Market

A Django web application for managing a local farmers market: the **producers** (farms, dairies, bakeries, fisheries) who sell there, the **products** they offer, and the **market days** they attend.

Built as the Regular Exam project for the SoftUni **Django Basics** course.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Environment Variables & Credentials](#environment-variables--credentials)
- [Project Structure](#project-structure)
- [Data Model](#data-model)
- [Pages & URLs](#pages--urls)
- [Custom 404 Page](#custom-404-page)
- [Optional Demo Data](#optional-demo-data)

---

## Features

- **Producers**: full CRUD. You can list, search by name, view details (including the producer's products), create, update and delete (with a confirmation step).
- **Products**: full CRUD. Each product belongs to a producer and has a category, unit, price, stock quantity, an optional expiry date and an image.
- **Market Days**: schedule market days with a location, a market type and opening hours, and choose which producers attend (many-to-many).
- **Home dashboard**: live counts of products, producers and market days, plus the latest products and upcoming market days.
- **Search**: search producers and products by name, and market days by location.
- **Image uploads** for producers and products.
- **Responsive UI** built with Bootstrap 5, Font Awesome and a custom stylesheet.
- **Shared layout**: a base template plus reusable partials (header, navigation, footer, form card).

## Tech Stack

| Layer      | Technology                                   |
|------------|----------------------------------------------|
| Language   | Python 3.12                                  |
| Framework  | Django 6.1                                   |
| Database   | SQLite (default, no setup needed)            |
| Forms      | django-crispy-forms + crispy-bootstrap5      |
| Countries  | django-countries                             |
| Images     | Pillow                                       |
| Front-end  | Bootstrap 5.3, Font Awesome 6 (CDN)          |

## Getting Started

### Prerequisites

- Python **3.12+**
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/DBV70/FarmersMarket.git
cd FarmersMarket

# 2. Create and activate a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations (creates db.sqlite3)
python manage.py migrate

# 5. Start the development server
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

The application starts with an **empty database**. Every object can be created through the UI:

1. **Producers → Add Producer**: create at least one producer.
2. **Products → Add Product**: create products and assign them to a producer.
3. **Market Days → Add Market Day**: schedule a market day and select the attending producers.

## Environment Variables & Credentials

**No environment variables or credentials are required** to run the project locally.

- The project uses Django's default development settings (`DEBUG = True`, SQLite database, development `SECRET_KEY` in `FarmersMarket/settings.py`).
- No login is needed. Authentication and user management are intentionally out of scope for this project.
- The Django admin panel is **not** needed to use the application.

## Project Structure

```
FarmersMarket/
├── manage.py
├── requirements.txt
├── FarmersMarket/            # Project package (settings, root URLs, WSGI/ASGI)
│   ├── settings.py
│   ├── urls.py
│   ├── common/               # Home page, shared forms (search), management commands
│   ├── producers/            # Producer model, forms, CRUD views
│   ├── products/             # Product model, forms, CRUD views
│   └── markets/              # MarketDay model, forms, views
├── templates/
│   ├── shared/               # base.html + partials: header, nav, footer, form-card
│   ├── common/               # home page
│   ├── producers/            # list, detail, add, update, confirm delete
│   ├── products/             # list, detail, add, update, confirm delete
│   └── markets/              # list, detail, add, update, confirm delete
├── static/
│   ├── css/styles.css        # Custom theme
│   └── images/
└── media/                    # Uploaded images (created at runtime, git-ignored)
```

### App responsibilities

| App         | Responsibility                                                              |
|-------------|------------------------------------------------------------------------------|
| `common`    | Landing page / dashboard, reusable forms (search), demo-data command         |
| `producers` | Managing farms and producers                                                 |
| `products`  | Managing the product catalog and linking products to producers               |
| `markets`   | Scheduling market days and assigning attending producers                     |

## Data Model

```
Producer 1 ──────< * Product          (many-to-one: Product.producer → Producer)
Producer * >────< * MarketDay         (many-to-many: MarketDay.producers ↔ Producer.market_days)
```

| Model       | Key fields                                                                                   |
|-------------|----------------------------------------------------------------------------------------------|
| `Producer`  | name (unique), address, country, description, contact, email (unique), phone, website (unique), image |
| `Product`   | name, description, category, price, quantity, unit, expiry date, image, **producer (FK)**     |
| `MarketDay` | date, location, market type, description, opening / closing time, **producers (M2M)**         |

- Deleting a **producer** also deletes their products (`CASCADE`).
- Deleting a **market day** only removes the producer links. The producers themselves are kept.

## Pages & URLs

| Page                     | URL                          |
|--------------------------|------------------------------|
| Home                     | `/`                          |
| All products             | `/products/`                 |
| Product details          | `/products/<id>/`            |
| Add product              | `/products/add/`             |
| Update product           | `/products/<id>/update/`     |
| Delete product (confirm) | `/products/<id>/delete/`     |
| All producers            | `/producers/`                |
| Producer details         | `/producers/<id>/`           |
| Add producer             | `/producers/add/`            |
| Update producer          | `/producers/<id>/update/`    |
| Delete producer (confirm)| `/producers/<id>/delete/`    |
| All market days          | `/markets/`                  |
| Market day details       | `/markets/<id>/`             |
| Add market day           | `/markets/add/`              |
| Update market day        | `/markets/<id>/update/`      |
| Delete market day (confirm) | `/markets/<id>/delete/`   |

Every page can be reached from the navigation bar, the footer, or links on other pages.

## Custom 404 Page

Django only renders the custom `404.html` template when `DEBUG = False`. To see it locally:

1. In `FarmersMarket/settings.py`, set `DEBUG = False` (keep `ALLOWED_HOSTS = ['*']`).
2. Run `python manage.py runserver --insecure` (`--insecure` keeps static files served while `DEBUG` is off).
3. Open any URL that does not exist, e.g. http://127.0.0.1:8000/does-not-exist/.

## Optional Demo Data

The application is fully usable with an empty database. If you want sample data for a quick demo, you can run:

```bash
python manage.py seed_market_data
```

This step is **optional** and not required for evaluation.
