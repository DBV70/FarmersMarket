# Farmers Market

My project for the SoftUni Django Basics regular exam.

It's a small web app for running a local farmers market. You can keep track of the producers (farms, bakeries, dairies and so on), the products they sell, and the market days they take part in.

## What you can do

- Add, view, edit and delete **producers**. A producer's page lists all of their products.
- Add, view, edit and delete **products**. Each product can belong to a producer and has a category, price, quantity, unit and an optional expiry date and image.
- Add, view, edit and delete **market days**, and choose which producers attend each one.
- Search producers and products by name, and markets by location.
- Products can also be sorted by name, price or date added.
- See totals, the latest products and the upcoming market days on the home page.

## Setup

You need Python 3.12 or newer.

```bash
git clone https://github.com/DBV70/FarmersMarket.git
cd FarmersMarket

python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000/.

The database starts empty and everything can be created from the site. The easiest order is:

1. Producers → Add Producer
2. Products → Add Product (pick a producer)
3. Markets → Add Market Day (pick the attending producers)

You don't need any environment variables, accounts or passwords. The app uses SQLite and the default settings in `FarmersMarket/settings.py`. There's no login, and you don't need the admin panel.

## Apps

- `common`: the home page, the search form and the custom template filters
- `producers`: the Producer model and its pages
- `products`: the Product model and its pages
- `markets`: the MarketDay model and its pages

## Models

- **Producer**: name, address, country, description, contact person, email, phone, website, image
- **Product**: name, description, category, price, quantity, unit, expiry date, image, and producer (many-to-one)
- **MarketDay**: date, location, market type, description, opening and closing time, and producers (many-to-many)

If you delete a producer, their products are deleted too. Deleting a market day only removes the links to its producers.

## Forms and validation

- All forms have custom labels, placeholders and help texts. The producer and market day forms also have custom error messages.
- Market days are validated in the model:
  - the market must open between 08:00 and 12:00 and close by 19:00
  - it must open before it closes
  - a new market day can't be in the past
- A product's price must be at least 0.01 and its quantity can't be negative. Producer name, email and website must be unique.
- When you edit a market day, the date and market type are disabled, so they can't be changed.
- Every delete goes through a confirmation page. It shows a short read-only summary of the object. Unneeded fields are left out of that form.

## Templates

- Every page extends `shared/base.html`, which includes the header, navigation bar and footer partials. All add and edit pages share `shared/form-card.html`.
- The custom filters are in `common/templatetags/market_filters.py`:
  - `expiry_status` shows "Expires in 5 days", "Expires today" or "Expired"
  - `stock_level` shows "In stock", "Low stock" or "Out of stock"
- The styling uses Bootstrap 5, Font Awesome and my own `static/css/styles.css`.

## Custom 404 page

Django only shows a custom 404 page when `DEBUG` is off. To see it:

1. Set `DEBUG = False` in `FarmersMarket/settings.py`.
2. Run `python manage.py runserver --insecure`. The `--insecure` flag keeps the CSS loading.
3. Open a URL that doesn't exist, for example http://127.0.0.1:8000/abc/.

## Demo data (optional)

If you want some sample data to click around with run `python manage.py seed_market_data` in the console.

```bash
python manage.py seed_market_data
```
## AI content

- HTML templates partly contain AI-generated content.
- CSS contains AI-generated content.
- README.md partly contains AI-generated content.
- Function used for filling data in the database `seed_market_data.py` contains AI-generated content.
