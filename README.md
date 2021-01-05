# **SFIA1**

# **Contents**
* [Introduction](#introduction)
  * [Objective](#objective)
  * [Proposal](#proposal)

* [Architecture](#architecture )
  * [Trello Board](#trello-Board)
  * [ERD](#erd)
  * [Risk Assesment](#risk-assesment )
  * [Continuous Integration](#continuous-integration)

* [Development](#development)
  * [Front End](#front-end)
  
* [Testing](#testing)
  * [Unit Testing Console](#unit-testing-console)
  * [Unit Testing Jenkins](#unit-testing-jenkins)
  * [Coverage](#coverage)

* [Future Improvements](#future-improvement)

* [Author](#author)

# *Introduction*
### Objective

The objective for the SFIA1 is to create a CRUD application utilising the different softwares learnt during training.

The following requirements are required from me:

* A functioning CRUD application created in Python
* A functioning front-end website utilising Flask
* A trello board 
* A Relational database, containing a one-to-many relationship
* Clear documentation
* A risk assessment
* Automated tests in Jenkins
* Code fully integrated into Github

### Proposal
I decided to create a site which will allow boxing club owners to create a boxing club and create a boxer. They can assign a boxer to a particular club, with this inplace it allows the club owner to extract information with ease. 
An outline of how CRUD will be implemented can be seen below.

#### The two create functions below satifies Create
* Create a boxer:
     * The boxers first name
     * The boxers last name 
     * The boxers email
     * The weightclass
     * Club choice
* Create a club:
     * The club name
     * The club location
     * The club email
     * The manager

* Read:
     * View club information 
     * View boxer information
     * View which boxers are signed up to which clubs

* Update:
     * Boxers information

* Delete:
     * Boxers information
     * club information

# **Architecture**
### Trello Board
Trello is an incredible web-based project management and collaboration tool that helped me plan my project in one platform. Trello follows the Kanban system which aided me to schedule my tasks for the project into digestible components. Trello is a free system and utilises coloured labels according to my priority which was perfect for my small project.
Next to each card the MOSCOW rule was followed the M is must, C is could and S is should. 

<img width="460" height="300" src="https://user-images.githubusercontent.com/74771255/103366250-03058d00-4aba-11eb-9f20-b049c46b2123.jpg">


### ERD
##### *Old ERD*
This is the initial Entity-relationship diagram which showcases the tables for Admin. boxer and club. With this table, I would have to implement a login function for the Admin however having read the scope of the project I realised that this was not required.

<img width="460" height="300" src="https://user-images.githubusercontent.com/74771255/103309306-b2842600-4a0c-11eb-81a2-3e295dfb083c.jpg">

##### *New ERD*
This is my new ERD which shows how the database for the application is structured. The Club and Boxer tables have a one to many relationship. This allows the club owner to assign a boxer to a particular club during the creating of a boxer stage. This will then enable the club owner to view which boxers are assigned to a particular club.

<img width="460" height="300" src="https://user-images.githubusercontent.com/74771255/103321075-e290f080-4a2f-11eb-920a-6c573ecf8099.jpg">


## Risk Assesment 
[Here is a link to the full risk assesment form]https://docs.google.com/spreadsheets/d/1ZyntPGcurU_Xrc7W5w9BoK8OMcglQ3lHaZJgJJV8-8o/edit?usp=sharing

Screenshots of the risk assessment is provided below:
Risk number 6 and 7 was added at the later stage of the project as these risks became clear to me.

<img width="460" height="300" src="https://user-images.githubusercontent.com/74771255/103369473-22a0b380-4ac2-11eb-95b1-9dbed90c26bf.jpg">
<img width="460" height="300" src="https://user-images.githubusercontent.com/74771255/103369484-26ccd100-4ac2-11eb-9c21-e11a9d446731.jpg">


## Continuous Integration

![CI](https://user-images.githubusercontent.com/74771255/103577491-d643e200-4ecc-11eb-8baf-92cee5a1c672.jpg)
Jenkins is an open-source automation tool with plugins built for Continuous Integration purposes. Jenkins was used to build and test my project continuously making it easier for me to integrate changes to the project, and making it easier for me to obtain a fresh build. For the project the code was pushed to Github then Jenkins fetched and built the repository, lastly it run the unit test.

# **Development** 
### Front End 
The front end of the website is created with HTML so it is basic but full functional. When the application is launched the user is directed to the Home page
##### Home Page
The home page displays the a create boxer and a create club button at the top. It also displays club information and the boxers assigned to that particular club.

![home page 1](https://user-images.githubusercontent.com/74771255/103374934-ac577d80-4ad0-11eb-844c-b6b5a740ba3f.jpg)

##### Create Boxer
Once the user clicks on the create a boxer button they are directed to this page which will allow them to fill the boxers information. Also at the choose club section, the drop-down will list all the clubs created previously, this will allow the user to assign boxers to a specific club.once the user clicks on add boxer this information will be displayed on the home page.

![create a boxer](https://user-images.githubusercontent.com/74771255/103376989-fbec7800-4ad5-11eb-831b-d0fa2ef4001c.jpg)

Once the user clicks on add boxer this information will be displayed on the home page.

![actual created boxer](https://user-images.githubusercontent.com/74771255/103378923-e0846b80-4adb-11eb-86c0-fe25eac19eeb.png)

##### Create club
Upon the user clicking on the create a club button they will be directed to page which will allow them to fill the club information. Once the user clicks add club the information will be displayed on the home page.

![create a club](https://user-images.githubusercontent.com/74771255/103377394-34d91c80-4ad7-11eb-82a6-94367701d65e.jpg)

Once the user clicks add club the information will be displayed on the home page.

![actual created club](https://user-images.githubusercontent.com/74771255/103379114-728c7400-4adc-11eb-9502-f24f971a7618.jpg)

##### Update Boxer information 
The user can update the boxers information from the home page by clicking on the update button under the boxers information. They will be directed to this page which is similar to the create a boxer page which displays a list of fields the user must fill in. In the screenshot below the user updates the weight class of the particular boxer from Cruzer weight to Heavyweight. Also, the original information of the boxer is displayed at the top.

![update boxer](https://user-images.githubusercontent.com/74771255/103378061-065c4100-4ad9-11eb-8e01-e385b7b15704.png)

Once the user clicks the add boxer button the new information will displayed on the homepage.

![actual updated boxer](https://user-images.githubusercontent.com/74771255/103379205-c5fec200-4adc-11eb-8ab7-2e3273b45f8b.jpg)

##### Delete Boxer
The user can delete a boxer from a club by clicking on the delete button under the boxers information. In this instance the boxer Mike Tyson will be deleted from the Stonebridge boxing club.

![delete boxer](https://user-images.githubusercontent.com/74771255/103382327-8dfc7c80-4ae6-11eb-8515-582e81e9c67a.jpg)

Once the boxer is deleted the boxers information is removed from the club.

![actual deleted boxer](https://user-images.githubusercontent.com/74771255/103382328-90f76d00-4ae6-11eb-92d2-a8dd9c3bf599.jpg)


##### Delete Club
The user can delete a club by click on the delete club button situated at the bottom of the club information this will remove club and boxers assigned to that club.

![delete club](https://user-images.githubusercontent.com/74771255/103380074-ab7a1800-4adf-11eb-844e-4230950804c9.jpg)

### Testing
##### Unit Testing Console
Unit test was conducted for the project to test every function of the site. The test written asserts actions into the application and returns the set response given with in the unit testing. 

![pytest](https://user-images.githubusercontent.com/74771255/103466640-9f3fc600-4d3e-11eb-9455-a2f2e16b64ce.jpg)

The coverage in the console:

![pytest cov](https://user-images.githubusercontent.com/74771255/103466638-9a7b1200-4d3e-11eb-9200-8788a72f0cda.jpg)

##### Unit Testing Jenkins
The same principle applies to the jenkins unit test however the test is conducted automatically here after i push to the repository.  

![testjenkins](https://user-images.githubusercontent.com/74771255/103578681-e8bf1b00-4ece-11eb-997c-6ab28766e2b4.jpg)

##### Coverage
The HTML format of the coverage was produced to show how much of the code in the app has been tested successfully.

![cov](https://user-images.githubusercontent.com/74771255/103466134-f1cab380-4d39-11eb-8721-fc2e83c44ea6.jpg)


### Future Improvements
* In the future I will implement integration test (selenium) and systemd within the coding stage of the project. 
* More fields for the when the boxer is getting created i.e. Records and Telephone number.
* Allow deletion of a club with boxers as currently, that is not fully functional only clubs without boxers can be deleted.
* Implement a login function for the club owner and club manager as this will outline the roles and responsibility of different users of the application as its currently only tailored for the club owner.

### Author

Abdibasid Yacquub      
 
