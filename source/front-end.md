# Front-End

The application is a Progressive Web App (PWA). This means that most modern browsers allow users to install the application locally. The source code for the application can be found {{ '[here]({}{})'.format(githubBase,frontEndRepo) }}. To contribute to this application, please ensure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [node](https://nodejs.org/en/download/) installed. To clone the application enter: `git clone URL`, replacing `URL` with _{{githubBase}}{{frontEndRepo}}_

Change to the app directory (using `cd legume-choice-client`). You then need to install all of the dependencies using the command `npm install`. To start developing the application locally, run `npm start`, the application should then load in your browser and you can begin editing components. the code for each of the components can be found in the directory `./src/components`. This will contain a folder for each of the components. The names of the components should be self explanatory, and comments within each components should sufficiently explain

The application mainly uses [class based components](https://reactjs.org/docs/components-and-props.html). If you are new to react, we recommend following [this React tutorial](https://reactjs.org/tutorial/tutorial.html).

This application uses the react [context API](https://reactjs.org/docs/context.html) in order to share state between components. The context includes all of the data collected in the application. To understand more about how this data is structured, please refer to the "raw data" subsection of the [database](database.md) section.

## Data files

Much of the structure of the application depends on data files, which give information about what typologies exist, what legumes are available, what legume-functions exist etc...

-   For the data-entry component, the data file can be found in the file `./src/components/data-entry-component/data-entry-data.js`
-   For the legume information, the data file can be found in the file `./src/components/legumes-component/legume-information-clean.js`. To add a legume to the application, simply add a legume to this list.
-   Information on which components are rendered, and their routes, can be found in the file `./src/components/sidebar-component/sidebar-data.js`.

## Limitations

-   Changing the names of the variables, and the location of the data-files, is very likely to cause problems.
