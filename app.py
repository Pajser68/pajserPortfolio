from flask import Flask, render_template
import os
from database import db

app = Flask(__name__)

# Database configuration
database_url = os.getenv('DATABASE_URL', 'sqlite:///portfolio.db')
print(f"Using database: {database_url}")  # Debug logging
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db with app
db.init_app(app)

# Import models after db is initialized
from models.project import Project

# Initialize database and create tables
def init_db():
    with app.app_context():
        db.create_all()
        print("Database tables created successfully")
        
        if Project.query.count() == 0:
            print("Database is empty, adding initial projects...")
            add_initial_projects()
        else:
            print(f"Database already has {Project.query.count()} project(s)")

def add_initial_projects():
    """Add initial sample projects to the database"""
    projects = [
            Project(
                name='NK Dobrinj static site',
                github_link='https://github.com/Pajser68/nkdobrinj_static_site',
                description='Static web site about my favourite non-existent football team.',
                technologies='HTML,CSS,JavaScript,Photoshop,Premiere'
            ),
            Project(
                name='Personal portfolio',
                github_link='https://github.com/Pajser68/pajserPortfolio',
                description='Personal portfolio made as a part of an undergraduate computer science study. Showcases personal projects and information.',
                technologies='Python,Flask,PostgreSQL,SQLAlchemy,Git,Docker,HTML,CSS,JavaScript'
            )
        ]
        
    for project in projects:
        existing = Project.query.filter(
            (Project.name == project.name) | (Project.github_link == project.github_link)
        ).first()
        
        if existing:
            print(f"Project already exists: {existing.name}")
        else:
            db.session.add(project)
            print(f"Added project: {project.name}")
    
    db.session.commit()


@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    # Fetch projects from database
    db_projects = Project.query.all()
    
    # Convert to format expected by template
    projects_list = [
        {
            'title': project.name,
            'description': project.description,
            'technologies': project.technologies.split(',') if project.technologies else [],
            'github_link': project.github_link
        }
        for project in db_projects
    ]
    
    return render_template('projects.html', projects=projects_list)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    init_db()
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
