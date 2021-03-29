# Database

The MongoDB database can be found on the legumeCHOICE virtual machine. To view the database:

-   Connect to the virtual machine
-   Use the command `mongo` to start the MongoDB shell.
-   Use the command `show databases` to view the available databases. The database "legume-choice" should be available. To begin querying this database, you must use the command `use legume-choice`.
-   There are three "collections" in the legume-choice database, `projects`, `projectsarchives`, `cursors`.

The `projects` collection includes all of the most recent data for each project. This includes the objects `rawdata`, `projectSecret`, `projectID`, and `date`. `rawdata` includes all of the information from the individual project (described in more detail below). `projectSecret` includes a code which was created when the project was first created in the react application, this ensures that only people with the original project file can overwrite a record in the database. `projectID` is the original project ID. `date` is the ISO date the project was uploaded/updated.

The `projectsarchives` collection includes every upload to the database. This means whenever a project is overwritten, because of changes made by the data collector, the previous version of the project is stored in the archive. The `cursor` collection is a capped collection with a tailable cursor. This is used in data-processing, it allows the python daemon to wait for changes to the database. This was done as MongoDB (when it is not hosted on MongoDB Atlas or MongoDB realm) does not offer trigger functions.

## Raw Data

The rawdata has a format which reflects the structure of the front end. All raw data is scored in the `currentProject` object. This has 9 different objects:

-   `agroEcoData`: All of the data collected on agroecology for the project. This is a simple object, with only four biofilters.
-   `contextScores`: Contains the following four objects
    -   `attributes`: The context attributes which need to be scored (e.g. land, labour, seed etc...)
    -   `participants`: The people who are giving context scores (farmer and expert)
    -   `typologies`: The potential typologies of the people who are providing scores (low, medium, and high)
    -   `scores`: All of the individual scores entered into the application, and the averages for each attribute.
-   `legumeData`: The information for all of the legumes. The main object of importance is `allLegumes`.
-   `location`: The location information extracted from the polygon mapping exercise.
-   `pairWiseScores`: Each of the scores entered for the pairWise selection exercise. These are broken down into each of the following
    -   `averages`: Average scores
    -   `female`: Scores entered for female selections
    -   `male`: Scores entered for male selections
    -   `legumeFunctions`: Each of the functions offered as options
-   `participatoryMatrixScores`: The main object of importance here is `farmers`, which contains a list of all of the farmers consulted in data collection.
-   `projectInfo`: A simple object with all of the data entered in the project information section of the application
-   `projectSecret`: Information used for the submission of the project. Including whether the project was a "real" or "test" project and what date the data is due to be made public.
-   `results`: Summaries of all the results.
