# Identity, Authentication, and Access Control

## Introduction
`Identity`, `Authentication`, and `Access Control` are three core concepts that, respectively, help determine who someone is, verify who they say they are, and then allow them work and interact with a set of approved objects appropriate to who they are or what roles they fill. This module explores these concepts to illustrate them in the real world and in cyberspace. The module includes a variety of hands-on labs that help students build up and scaffold these concepts. 

## Intended Audience
Undergraduate students in an Introduction to Cybersecurity Class

## Learning Objectives
By the end of this module, students will be able to:

* Define personal identity in terms of digital and physical attributes and information.
* Differentiate between a digital identity (who someone is) and a credential (how someone proves who they are).
* Place different types of credentials into categories by associating them with one of the three phrases: "something you know," "something you have," and "something you know"
* Associate credentialing with role-based permissions and discern between different levels of access needs as part of different scenarios. 
* Describe the relationship between password complexity and the amount of time required to crack a password.

## Materials Required

* see specific lab guides for materials

## Prerequisite lessons
None

## Learning Facilitation
### Warm up Activities
* Role Play an identity, authentication, and access control scenario (see - [role play scenario](#role-play-scenario))
* Introduce the concept of Identity, Roles, and Permissions more formally (see - [Intro](#intro))

### Focused Activities
* Examine a real identity, authentication, and access control scenario online (see - [identity lab](#identity-lab))
* Explore password complexity and brute forcing  (see - [password lab](#password-lab))

### Closure
Reflect 

## Assessment
Assessment strategy goes here

## Role Play Scenario (15 minutes)
The entry point for the lesson is a role play scenario. Role play is an active learning technique that gets students up, moving, and interacting. The purpose of this exercise is to serve both as a `hook` to get students interested, and to provide a `scaffold` for students to work from as they explore the topic area. 

The role play scenario should be structured as follows:
* Begin by describing a hospital scenario as listed below.
  - A hospital has four kinds of people:
    - patients
    - patient family members
    - surgeon
    - nurses
  - Our hospital supports two kinds of use
    - surgery operating room
    - lobby

### Part 1: Role-based permissions exploration
* Ask students to think about what each kind of user should be able to do in each place. Give students 3 minutes of class time to write down their thoughts.
* While the students are thinking, create a two-column chart on the whiteboard. For the rows, list out the different kind of users. For the columns, list out the two places (surgery operating room and lobby).
* After the three minutes are up, ask students to tell you what each kind of person should be able to do in each place. Take a few minutes to collect some thoughts from students.

> Some examples might be: nurses and doctors should be able to enter the operating room, patients should be able to enter the operating room when accompanied by a doctor, family should not be able to enter the operating room. Other uses might be that doctors should be able to order drugs to be administered, while nurses should not. Allow your students to be creative, but try to ensure there are plenty of different role-specific permissions.

* Discuss and reflect upon the findings the class comes up with to emphasize the differences between roles. 

### Part 2: Identity, Authentication, and Access control
* Ask all students to think of three things that could be used to identify a person. Tell them they must identify one thing the person knows, one thing the person is, and one thing the person has. Encourage students to think about unique differentiators. Give them one minute. 
* Again, as in part 2, ask students to share their thoughts with the class and begin creating a list of thoughts in the three different categories. 
* Now ask students how a hospital could measure and verify that the different type of users are who they say they are using some of the identity descriptors the class has come up with. Give students 3  minutes to come up with a few ideas. Once again, list them on the board.
* Have students now role play an access request. 
  - Setup two stations, assign one student to each one. The assigned student will represent a place (emergency room or lobby). Give them a prop (e.g. a piece of paper that says ER) to hold up and position them on opposite sides of your classroom.
  - Assign one student to each role (doctor, nurse, etc.).
  - Pick some of the verification methods listed on the board. Assign a one student to each one for each place. Their role will be to allow a request if it is valid, or deny it if it is not valid. (e.g. a retina scanner in the emergency room).
  - Initial start with one verifier (e.g. password) and have the students user role players walk up to the password verifier roleplayer. Hand the use roleplayer a password post-it note. Write the same password on another post-it and hand it to the verifier. Have the user walk up to the verifier and have the verifer check if the password is valid.
  - Now, arrange multiple verifier in a row to simulate multi-factor authentication. 
  > Make sure to pause to ensure that all students here the rationale for this methodology. 
  - Now, ask the class how just being verified to access a place, doesn't mean that every user should be able to do everything. 
  - Now assign a student to represent permission checkers. Pick several from the earlier chart and assign them to each place, arrange the permission checkers in a row after the identity verifiers. Have them check to see if the student user role players have permission to do certain things in the place. 
  - Run this loop several times with several different permissions, have the entire class observe the workflow from start to finish.


## Intro (15 minutes)
After the role play scenario, the instructor should overview the lesson objectives and connect them to the role play activity. The attached intro slides introduce the module topics more formally and further fill-in detail that can be build on top of the role play scenario scaffolding. The objective is for students to conceptualize the various steps before an access decision can be granted, namely: `identify`, `authenticate`, `authorize.`

The intro slides introduce these concepts and associated vocabulary.

## Identity Lab

## Password Lab

## Lead Author
- Dr. Matthew Hale, University of Nebraska at Omaha

### Acknowledgements
Special thanks to Dongwon Lee for reviewing these materials

### License
[Dr. Matthew L. Hale](http://faculty.ist.unomaha.edu/mhale/) <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
