# Flats Prices in Kengarags (Riga)

This project collects, stores, and analyzes apartment prices in Kengarags, using data from the [ss.lv](https://www.ss.lv) archive.

---

## 📦 Project Structure

| File                   | Description |
|------------------------|-------------|
| `database_criation.sql`| SQL query to create the `kengarags_prices` table |
| `SQL_quarys.py`        | PostgreSQL connection and `add_to_database()` function |
| `data_extraction.py`   | Scraping apartment ads from ss.lv and inserting into DB |
| `data_analys.py`       | Price analysis and visualization (charts, simple ML model) |
| `requirements.txt`     | List of dependencies |
| `README.md`            | Project documentation |

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/Daniel1272/portfolio.git
cd portfolio/Flats_prices_kengarags
Install dependencies:
pip install -r requirements.txt
🗃️ Database Setup

Create a PostgreSQL database named flats_prices_riga, then execute the SQL query from database_criation.sql:

CREATE TABLE kengarags_prices (
    id SERIAL PRIMARY KEY,
    address TEXT,
    rooms INTEGER,
    square_meters INTEGER,
    floor_ INTEGER,
    total_floors INTEGER,
    project TEXT,
    type_ TEXT,
    price INTEGER,
    price_per_m2 REAL,
    created_at DATE
);
🔐 Database Connection Configuration

Open SQL_quarys.py and replace the connection parameters with your own:

DATABASE_USER = 'your_username'
DATABASE_PASSWORD = 'your_password'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5432'
DATABASE_NAME = 'flats_prices_riga'
🚀 How to Run

Data extraction:
python data_extraction.py
Data analysis and visualization:
python data_analys.py
After running data_analys.py, you will see 4 plots:

Average price per m² by number of rooms over time
Average price per m² by project over time
Price per m² by floor
Price vs area with linear regression line
📊 Libraries Used

psycopg2
numpy
pandas
requests
beautifulsoup4
lxml
matplotlib
scikit-learn
📌 Author

Daniel1272

