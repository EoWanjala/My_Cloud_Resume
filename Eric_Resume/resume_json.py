import json
from bs4 import BeautifulSoup

with open('EoWanjala/My_Cloud_Resume/Eric_Resume/eric_resume.html', 'r') as file:
    html_content = file.read()

#html_content="EoWanjala/My_Cloud_Resume/Eric_Resume/eric_resume.html
# 
# EoWanjala/My_Cloud_Resume/Eric_Resume/eric_resume.html "


# Assuming you have the HTML content of the resume in a variable called 'html_content'
soup = BeautifulSoup(html_content, 'html.parser')

# Extract relevant information from the HTML
resume_data = {
    'name': soup.find('h2', {'class': 'name'}).text.strip(),
    'profession': soup.find('p', {'class': 'career'}).text.strip(),
    'contact': {
        'phone': soup.find('li', string=lambda text: 'phone' in text.lower()).text.strip().split('\n')[1].strip(),
        'email': soup.find('li', string=lambda text: 'email' in text.lower()).text.strip().split('\n')[1].strip(),
        'linkedin': soup.find('li', string=lambda text: 'linkedin' in text.lower()).text.strip().split('\n')[1].strip(),
    },
    'skills': [
        {
            'name': skill.find('p', {'class': 'skill-title'}).text.strip(),
            'progress': skill.find('div', {'class': 'progress'}).get('class')[1].split('-')[1]
        }
        for skill in soup.find_all('li', recursive=False)
    ],
    'experience': [
        {
            'company': job.find('h5', {'class': 'tl-title'}).text.strip(),
            'dates': job.find('p', {'class': 'para'}).text.strip(),
            'title': job.find('h5', {'class': 'tl-title-2'}).text.strip(),
            'description': job.find('p', {'class': 'para'}).find_next_sibling('p', {'class': 'para'}).text.strip()
        }
        for job in soup.find_all('div', {'class': 'timeline'})
    ],
    'education': {
        'degree': soup.find('h5', {'class': 'tl-title-2'}).text.strip(),
        'details': soup.find('p', {'class': 'para'}).text.strip()
    },
    'certifications': [
        {
            'name': soup.find('h5', {'class': 'tl-title'}).text.strip(),
            'date': soup.find('div', {'class': 'tl-content'}).find('p', {'class': 'para'}).text.strip()
        }
    ],
    'projects': [
        {
            'name': project.find('h5', {'class': 'tl-title'}).text.strip(),
            'description': project.find('div', {'class': 'tl-content'}).find('p', {'class': 'para'}).text.strip()
        }
        for project in soup.find_all('div', {'class': 'timeline'}, limit=2, skip=1)
    ],
    'references': [
        {
            'name': ref.find('h6', {'class': 'sub-title'}).text.strip(),
            'position': ref.find('p', {'class': 'sub-para'}).text.strip(),
            'contact': {
                'phone': ref.find('li', string=lambda text: 'phone' in text.lower()).text.strip().split('\n')[1].strip(),
                'email': ref.find('li', string=lambda text: 'email' in text.lower()).text.strip().split('\n')[1].strip()
            }
        }
        for ref in soup.find_all('div', {'class': 'referee'})
    ]
}

# Convert the resume data to JSON
json_resume = json.dumps(resume_data, indent=2)
print(json_resume)
