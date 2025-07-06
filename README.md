<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Slim-Beatnik/backend_module01_project">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Repair Shop DB</h3>

  <p align="center">
If you have been following along with the practice assignments your Mechanic API should have the following.

Rate Limiting and Caching:
Using the Flask-Limiter package, have a rate limit applied to at least one route in your API
Using the Flask-Caching package, have implemented caching on at least on route in your API
(Additional Optional Challenge): Apply a default rate limit to your project, offering blanket protection to all routes. Feel free to dive into the Flask-Limiter docs to figure this out: https://flask-limiter.readthedocs.io/en/stable/

Token Authentication: requires python-jose package.
Create an encode_token function that takes in a customer_id to create a token specific to that user.
login_schema, which can be made by excluding all fields except email and password from your CustomerSchema
In your customer blueprint, create a login route:
---- POST '/login' : passing in email and password, validated by login_schema
---- After credentials have been validate utilizes the encode_token() function to make a token to be returned to that customer.
Create @token_required wrapper, that validates the token and returns the customer_id to the function it's decorating.
Create a route that requires a token, that returns the service_tickets related to that customer.
---- GET '/my-tickets': requires a Bearer Token authorization.
---- The route function should receive the customer_id from the @token_required wrapper.
---- Using that id query the service_tickets where the customer_id is equal to the id passed in.
Additionally add @token_required to any routes you think should require authorization. (ex: Update, Delete,...)
(Additonal Optional Challenge): Create a login route for mechanics, which uses a separate function to encode tokens specifically for mechanics (Hint: add a field to the token payload). Additionally create another wrapper that checks the token for that field when authorizing. Apply this wrapper to relevant Mechanics and Inventory routes (What routes should a mechanic be required to be logged in for).
Advanced Queries:
Add an update route to your service_ticket blueprint to add and remove mechanics from a ticket.
---- PUT '/<int:ticket_id>/edit' : Takes in remove_ids, and add_ids
---- Use id's to look up the mechanic to append or remove them from the ticket.mechanics list
Create an endpoint in mechanics blueprint that returns a list of mechanics in order of who has worked on the most tickets
Apply Pagination to GET Customers route.
Assignment Continuation:

Incorporating a new resource to the API, we are now going to track inventory.

Inventory Model:
Create a new Inventory model in models.py which includes the following fields:
id: Unique Identifier
name: Part name
price: float value (price of the part)
Many-to-Many Relationship:
Establish a many-to-many relationship from Inventory to ServiceTicket, as One ticket can require many parts, and the same kind of part can be used on many different tickets.

The junction table does not have to support any additional fields, and can be a simple table object similar to your service_mechanic table. 

(Additional Optional Challenge): Make the junction table a Model object with additional field of quantity.

Inventory Blueprint:
Create a new folder in blueprints for Inventory:
Initialize the blueprint (don't forget to import routes under the blueprint initialization)
Register the blueprint with a url_prefix = '/inventory'
Create a Schema for Inventory (use SQLAlchemyAutoSchema to generate schema from Inventory Model)
Inventory Routes:
For inventory implement basic CRUD routes to Create, Read, Update, and Delete parts stored in our inventory. 

Additionally Create a route in the service_ticket blueprint to add a single part to an existing Service Ticket.

Testing and Submission:

Test all routes in Postman to ensure each endpoint works as designed. In Postman add every test request to a collection, and export that collection to your API project folder. Push your work to Github and submit the link to the GitHub repo.

Presenting
All students who joined Coding Temple February and onward need to present there project either on Thursdays or Friday live sessions, or you can schedule a 1-on-1 with Dylan to present.
For Pre-February students you are still encouraged to present as it is a great way to build you Tech-Communication skills which are a must.

Bonus features completed:
@role_required decorator added. It has a role in the payload, and protects mechanic routes.


    <br />
    <a href="https://github.com/Slim-Beatnik/backend_module01_project"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Slim-Beatnik/backend_module01_project">View Demo</a>
    &middot;
    <a href="https://github.com/Slim-Beatnik/backend_module01_project/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/Slim-Beatnik/backend_module01_project/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)



<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

Python, MySQL workbench and server, Postman.
Implimented: SQLAlchemy, Flask, Marshmallow

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/Slim-Beatnik/backend_module01_project.git
   ```
2. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin Slim-Beatnik/backend_module01_project
   git remote -v # confirm the changes
   ```
3. Create a virtual environment
   ```sh
   python -m venv venv
   python3 -m venv venv
   ```
4. Activate the virtual environment
   ```sh
   venv\\Scripts\\Activate
   source venv/bin/activate
   ```
5. Install dependencies:
  pip: ```sh
    pip install -r requirements.txt
  ```
  uv: ```sh
        uv sync
      ```

  Postman setup:
  repair_shop_db.postman_collection.json must run in the db_test_environment.postman_environment.json
  - if you're out of free collection runs -
  Open a terminal and input the following command and navigate to the correct directory for the project.
  Then:
  ```sh
    postman collection run repair_shop_db.postman_collection.json -e db_test_environment.postman_environment.json
  ```

  then use uv run app.py
6. Bonus ********
  if you're using uv, check out ruff
  Corey Shafer Youtube video: https://www.youtube.com/watch?v=828S-DMQog8

7. Verify paths in Postman:
  import repairshop_db.postman_collection.json
  You can then run all, or split up your run by folder.
  There is a main folder for creation:
  C___
  And another folder for read, update and delete:
  _RUD

Notes:
  several deletes are soft-deletes with intent -
  The idea behind it also includes columns in the inventory, specifically the recalled and recallable. It's important to keep records of any recallable services to serve your customers properly, if not legally. Further, service tickets should probably be kept until the end of the current tax year.

  There are also web storefront routes, /inventory/shop allows front-end to get all products for showcase or shopping purposes. They are also available by ~shop/\<id\>, or searched by ~shop/search.

  Customers can look up their tickets via service_tickets/my-tickets
  Similarly, mechanics can look their assigned tickets via service_tickets/assigned-tickets/search

  Both Mechanics and Inventory objects can be associated with a service ticket with add and remove id_lists

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/Slim-Beatnik/backend_module01_project/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/Slim-Beatnik/backend_module01_project/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Slim-Beatnik/backend_module01_project" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - totem64@gmail.com.com

Project Link: [https://github.com/Slim-Beatnik/backend_module01_project](https://github.com/Slim-Beatnik/backend_module01_project)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Slim-Beatnik/backend_module01_project.svg?style=for-the-badge
[contributors-url]: https://github.com/Slim-Beatnik/backend_module01_project/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Slim-Beatnik/backend_module01_project.svg?style=for-the-badge
[forks-url]: https://github.com/Slim-Beatnik/backend_module01_project/network/members
[stars-shield]: https://img.shields.io/github/stars/Slim-Beatnik/backend_module01_project.svg?style=for-the-badge
[stars-url]: https://github.com/Slim-Beatnik/backend_module01_project/stargazers
[issues-shield]: https://img.shields.io/github/issues/Slim-Beatnik/backend_module01_project.svg?style=for-the-badge
[issues-url]: https://github.com/Slim-Beatnik/backend_module01_project/issues
[license-shield]: https://img.shields.io/github/license/Slim-Beatnik/backend_module01_project.svg?style=for-the-badge
[license-url]: https://github.com/Slim-Beatnik/backend_module01_project/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/3dkylehill
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
