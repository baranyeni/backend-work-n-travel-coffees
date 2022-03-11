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

### Technical expectations

- The platform will be accessed from browsers
- It should have responsive behavior

# Scripts & Configuration

### Localisation
To create messages.pot file from the text used in templates
```bash
pybabel extract -F babel.cfg -o locales/messages.pot ../web
```

To create a new translation
```bash
pybabel init -i messages.pot -d translations -l <lang_code>
```

To compile our translations
```bash
pybabel compile -d translations
```

### Database

To implement latest changes from migration files run;
```bash
flask db upgrade
```

To generate new migration;
```bash
flask db migrate -m '<migration_file_name>'
```

### Environment Variables
To specify environment variables you should duplicate the `env/.env.sample` and
rename to `.env.development` and type down the necessary fields.