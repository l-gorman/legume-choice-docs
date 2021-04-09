# Public Data

This section describes how public data is presented. The legumeCHOICE public data can be found {{ '[here]({}{})'.format(apiUrl,publicData) }}.
Data can be broken down into two categories, **AggregatedProjects** and **IndividualProjects**.

The **IndividualProjects** folder contains reformatted results for each individual project which has been collected. These projects can be identified by their project ID (see [using the app](legume-choice-app.md)). The **AggregatedProjects** folder includes results for all of the projects together, in single CSVs.

For both **IndividualProjects** and **AggregatedProjects**, the results are broken down into 6 files:

-   **ContextData.csv**: The individual scores for each context categories, broken down by the 6 groups who are providing scores. The average for each score is also included.
-   **LegumeResults.csv**: For each individual legume, we have the legume attributes (function, context, and agro-eco), as well as their results which have been calculated based on data entered into the application.
-   **PairwiseSelections.csv**: The options for the pairwise selections ("option1" and "option2") as well as pariwise selections made for each of the legume functions ("maleChoice", "femaleChoice").
-   **PairwiseSummaryScores.csv**: The overall scores for each of the legume functions. Summarised in categories "male", "female", and "average".
-   **ParticipatoryMatrixScores.csv**: The participatory matrix scores, exactly as they are arranged in the original application.
-   **agroEcoData.csv**: The agroecological information for each individual project.
