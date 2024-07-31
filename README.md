Project Description: Blog Website with Integrated Chatbot

Overview
This project is a blog website featuring CRUD (Create, Read, Update, Delete) functionalities for blog management and an integrated chatbot powered by machine learning. The platform is designed to offer seamless user experiences, robust backend support, and scalable deployment in a cloud environment.

Frontend Features
1.	Blog Management:
o	CRUD Operations: Users can create, view, update, and delete blog posts.
o	Listing and Organization: Blog posts are listed in an organized manner, providing easy navigation and searchability.

2.	Chatbot Integration:
o	Basic Query Resolution: The chatbot is capable of handling basic greetings and queries such as "hi," "bye," and "help."
o	Sentiment Analysis: For queries beyond the predefined responses, the chatbot analyzes and returns the sentiment of the user's input using an ML model.

Backend Features
1.	API Development:
o	CRUD API: RESTful APIs for managing blog posts and user data.
o	Notification System: A dedicated API model for handling notifications related to blog posts.

2.	Websocket Integration:
o	Chatbot Communication: Websockets are used to enable real-time communication between the user and the chatbot.
o	Real-time Notifications: Currently, signals are implemented to trigger notifications when a new blog is posted. Full Websocket-based real-time notification mapping is under development.

3.	Machine Learning Integration:
o	Quick Response System: Ongoing efforts to implement machine learning models for providing quick, intelligent responses to user queries. Presently, the system returns sentiment analysis results for user inputs.
Technical Stack

1.	Deployment and Hosting:
o	ASGI Application: The application is served using Daphne and Nginx to handle asynchronous communication effectively.
o	Cloud Hosting: Hosted on AWS, utilizing services like S3 for storage and a load balancer to manage traffic and ensure scalability.
2.	Technologies Used:
o	Frontend: Modern web technologies for a dynamic and responsive user interface.
o	Backend: Robust server-side technologies to ensure efficient data handling and processing.
o	Websockets: For real-time interaction capabilities.
o	Machine Learning: Implemented for enhancing user interaction with intelligent responses.
o	Signal: Used for backend notification triggers.
This project aims to provide a comprehensive and interactive blogging platform with the added value of machine learning-driven user interaction. Future enhancements will focus on extending the chatbot's capabilities and refining real-time notification systems.
