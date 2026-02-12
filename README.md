# 🕷️ Neural Crawler - Web Crawler

<p align="center">
  <img src="/images/crawler3.png" alt="Neural Crawler Banner" style="width:100%; height:auto;" />
</p>

<p align="center">
  <strong>A powerful, Flask-powered web crawler built with Scrapy for efficient data extraction</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Framework-Scrapy-green.svg" alt="Scrapy">
  <img src="https://img.shields.io/badge/Web_Framework-Flask-lightgrey.svg" alt="Flask">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>

---

## 📖 Overview

**Neural Crawler** is a modern web scraping application that combines the power of [Scrapy](https://scrapy.org/) with a user-friendly [Flask](https://flask.palletsprojects.com/) web interface. It enables users to crawl websites and extract structured data with just a single click.

The default configuration targets [Books to Scrape](http://books.toscrape.com/), extracting book titles, prices, and availability information—but can be easily customized to crawl any website.

## ✨ Features

- 🌐 **Web Interface** - Simple, intuitive Flask-based UI for triggering crawls
- ⚡ **Fast Crawling** - Powered by Scrapy's asynchronous architecture
- 📊 **JSON Output** - Structured data export in JSON format
- 🔧 **Configurable** - Easily customizable spider rules and settings
- 🤖 **Robots.txt Compliant** - Respects website crawling policies
- ⏱️ **Timeout Protection** - Built-in safeguards against runaway crawls
- 🎯 **Page Limit Control** - Configurable page count limits

  <p align="center">
  <img src="/images/crawler-2.jpg" alt="Neural Crawler Banner" style="width:100%; height:auto;" />
</p>

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core programming language |
| **Scrapy** | Web crawling framework |
| **Flask** | Web application framework |
| **HTML/CSS** | Frontend interface |

## 📁 Project Structure

```
Neural-Crawler-Web-Crawler/
├── app.py                  # Flask application entry point
├── crawler_runner.py       # Spider execution handler
├── output.json             # Crawled data output
├── scrapy.cfg              # Scrapy configuration
├── neuralcrawling/         # Scrapy project module
│   ├── __init__.py
│   ├── items.py            # Data models
│   ├── middlewares.py      # Spider/Downloader middlewares
│   ├── pipelines.py        # Data processing pipelines
│   ├── settings.py         # Scrapy settings
│   └── spiders/
│       ├── __init__.py
│       └── crawling_spider.py  # Main crawler spider
├── static/
│   └── style.css           # Application styles
├── templates/
│   └── index.html          # Web interface template
└── images/
    └── crawler-2.jpg       # Banner image
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Neural-Crawler-Web-Crawler.git
   cd Neural-Crawler-Web-Crawler
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask scrapy
   ```

## 💻 Usage

### Running the Web Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Access the interface**
   
   Open your browser and navigate to: `http://127.0.0.1:5000`

3. **Start crawling**
   
   Click the **"Start Crawling"** button to begin data extraction.

### Running the Spider Directly

You can also run the Scrapy spider directly from the command line:

```bash
scrapy crawl mycrawler -o output.json
```

## ⚙️ Configuration

### Spider Settings

Modify `neuralcrawling/spiders/crawling_spider.py` to customize:

| Setting | Default | Description |
|---------|---------|-------------|
| `allowed_domains` | `books.toscrape.com` | Domains the spider can crawl |
| `start_urls` | `http://books.toscrape.com/` | Starting URLs for crawling |
| `CLOSESPIDER_PAGECOUNT` | `10` | Maximum pages to crawl |

### Global Settings

Edit `neuralcrawling/settings.py` to adjust:

- `ROBOTSTXT_OBEY` - Respect robots.txt rules (default: `True`)
- `DOWNLOAD_DELAY` - Delay between requests (default: `1` second)
- `CONCURRENT_REQUESTS_PER_DOMAIN` - Parallel requests per domain (default: `1`)

## 📤 Output Format

Crawled data is saved to `output.json` in the following structure:

```json
[
  {
    "title": "A Light in the Attic",
    "price": "£51.77",
    "availability": "In"
  },
  {
    "title": "Tipping the Velvet",
    "price": "£53.74",
    "availability": "In"
  }
]
```

## 🎨 Customization

### Crawling a Different Website

1. Update `allowed_domains` and `start_urls` in `crawling_spider.py`
2. Modify the `rules` to match the target site's URL patterns
3. Update `parse_item()` to extract the desired data fields
4. Adjust the HTML template in `templates/index.html` to display new fields

### Example: Custom Data Extraction

```python
def parse_item(self, response):
    yield {
        "title": response.css("h1::text").get(),
        "price": response.css(".price::text").get(),
        "description": response.css(".description p::text").get(),
        "url": response.url,
    }
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


##  Acknowledgments

- [Scrapy](https://scrapy.org/) - The fast, high-level web crawling framework
- [Flask](https://flask.palletsprojects.com/) - The lightweight WSGI web application framework
- [Books to Scrape](http://books.toscrape.com/) - Test website for web scraping

---

