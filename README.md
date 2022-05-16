# pet-blog-project
This is simple blog based on Django Framework with PostgreSQL database.
Deployed app available here https://pet-blog-project.herokuapp.com/

## Sections
**Main page** has list of 5 last articles ordered by create time.

**Cats and Dogs** pages are categories with articles. Each of them contains 15 articles. Categories contains pagination.

**Search** page helps users to find interested articles by title.

**Join** page is simple registration form without email confirmation.

**Login** login page.

After login, links to **Join** and **Login** are replaced by **Logout** link.

**Contact** page saves messages from users.

**Terms and Conditions** simple template page.

Under each article registrated users can leave commentaries.

## API
API made to have fast access to articles. For each category user can request all articles in JSON.
API available by path **domain**/api/v1/**category**.
For example - https://pet-blog-project.herokuapp.com/api/v1/dogs/

