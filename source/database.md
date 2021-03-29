# Database

The MongoDB database can be found on the legumeCHOICE virtual machine. To view the database:

-   Connect to the virtual machine
-   Use the command `mongo` to start the MongoDB shell.
-   Use the command `show databases` to view the available databases. The database "legume-choice" should be available. To begin querying this database, you must use the command `use legume-choice`.
-   There are three "collections" in the legume-choice database, `projects`, `projectsarchives`, `cursors`.

The `projects` collection includes all of the most recent data for each project. This includes the objects `rawdata`, `projectSecret`, `projectID`, and `date`. `rawdata` includes all of the information from the individual project (described in more detail below). `projectSecret` includes a code which was created when the project was first created in the react application, this ensures that only people with the original project file can overwrite a record in the database. `projectID` is the original project ID. `date` is the ISO date the project was uploaded/updated.

The `projectsarchives` collection includes every upload to the database. This means whenever a project is overwritten, because of changes made by the data collector, the previous version of the project is stored in the archive. The `cursor` collection is a capped collection with a tailable cursor. This is used in data-processing, it allows the python daemon to wait for changes to the database. This was done as MongoDB (when it is not hosted on MongoDB Atlas or MongoDB realm) does not offer trigger functions.
