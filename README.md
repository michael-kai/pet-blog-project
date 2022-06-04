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

**Add Post** page available for registered users. User can post own articles.

**Contact** page saves messages from users.

**Terms and Conditions** simple template page.

Under each article registrated users can leave commentaries.

## API
### Articles Endpoints

**api/v1/articles/** - List of all articles. 

Allowed: GET, POST, HEAD, OPTIONS. Only authenticated users can post articles.

Required fields to post article:

Title, slug, content, photo(only URL), cat. Field cat is required as id of category. 1 is for dogs, 2 is for cats.
Customized validation of the fields.
By default all posts by users are set to not-published.

**api/v1/articles/{article_id}** - Detailed endpoint of the specific article. 

Allowed: GET, PUT, PATCH, DELETE, HEAD, OPTIONS. 

Only authors can use PUT, PATCH, DELETE methods.

### Users Endpoints

**api/v1/auth/users/** - Registration. Provide {username} and {password}. 

Allowed GET, POST, HEAD, OPTIONS. GET available only after getting a token.

**auth/token/login/** - Login. Provide {username} and {password}. Allowed POST, OPTIONS. API token will be in response after successful login. To use a token add it in headers. E.g. - {Authorization} - {Token YOUR_TOKEN}.

**auth/token/logout/** - Logout. Allowed POST. Provide a token in headers.

**api/v1/auth/users/me/** - Your account. Allowed: GET, PUT, PATCH, DELETE, HEAD, OPTIONS.
