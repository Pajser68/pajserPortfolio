# pajserPortfolio
Portfolio page made with Python and Flask as a part of the undergraduate computer science course.

## Features
- **About Me**: Learn about my background and experience
- **My Projects**: Browse through my portfolio projects
- **Contact**: Get in touch with me

## Running the Application

### Option 1: Run with Docker (Recommended)

1. Build the Docker image:
```bash
docker build -t pajser-portfolio .
```

2. Run the container:
```bash
docker run -p 5000:5000 pajser-portfolio
```

3. Open your browser and navigate to: `http://localhost:5000`

### Option 2: Run Locally with Python

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to: `http://localhost:5000`

## Project Structure
```
pajserPortfolio/
├── app.py              # Main Flask application
├── Dockerfile          # Docker configuration
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   ├── base.html      # Base template with navigation
│   ├── about.html     # About Me page
│   ├── projects.html  # My Projects page
│   └── contact.html   # Contact page
└── static/            # Static files
    └── style.css      # CSS styling
```
