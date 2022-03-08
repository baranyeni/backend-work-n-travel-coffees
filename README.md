# backend-work-n-travel-coffees

This project was made with the idea of collecting and listing coffee shops that give their customers the chance to sit and work freely with their laptops. People who prefer to work while drinking delicious coffee in different and cozy places on a daily basis are invited to explore and are expected to share their experiences and evaluations with other people on this platform.

## Requirements

### User stories

Users should;

- Be able to list coffee shops
- Be able to make comment and review coffee shops
- Be able to give points based on 5 (1-5)
- Be able to star or pick as favorite selected shop
- Be able to generate custom personal lists and add shops into them

### Technical expectaions

- The platform will be accessed from browsers
- It should have responsive behavior


### Scripts & Configuration
To create messages.pot file from the text used in templates
- pybabel extract -F babel.cfg -o locales/messages.pot ../web

To create a new translation
- pybabel init -i messages.pot -d translations -l <lang_code>

To compile our translations
- pybabel compile -d translations


For DB management, open flask shell run in order;
- from wsgi import db
- db.create_all