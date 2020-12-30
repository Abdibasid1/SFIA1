# **SFIA1**

# **Contents**
* Introduction
  * Objective
  * Proposal

* Architecture
  * Trello Board
  * ERD
  * Risk Assesment 

* Development 
  * Front End 
  * Unit Testing

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
I decided to create a site which will allow boxing club owners to create a boxing club and create a boxer which they can assign to a particular club, with this inplace it allows the club owner 

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



### ERD
##### *Old ERD*
This is the initial Entity-relationship diagram which showcases the tables for Admin. boxer and club. With this table, I would have to implement a login function for the Admin however having read the scope of the project I realised that this was not required.

<img width="460" height="300" src="https://user-images.githubusercontent.com/74771255/103309306-b2842600-4a0c-11eb-81a2-3e295dfb083c.jpg">

##### *New ERD*
This is my new ERD which shows how the database for the application is structured. The Club and Boxer tables have a one to many relationship. This allows the club owner to assign a boxer to a particular club during the creating of a boxer stage. This will then enable the club owner to view which boxers are at a particular club.

<img width="460" height="300" src="https://user-images.githubusercontent.com/74771255/103321075-e290f080-4a2f-11eb-920a-6c573ecf8099.jpg">


## Risk Assesment 





# **Development** 
### Front End 



### Unit Testing





  

 
