---
layout: page
title: Assignment 2
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Academic Paper Layout</title>
<style>
    body {
        font-family: 'Times New Roman', serif;
        margin: 40px;
    }
    .paper {
        border: 1px solid #000;
        padding: 20px;
    }
    .title {
        text-align: center;
        font-size: 24px;
        text-transform: uppercase;
    }
    .authors {
        text-align: center;
        font-size: 20px;
        margin-top: 5px;
        margin-bottom: 20px;
    }
    .abstract,
    .section {
        margin-top: 30px;
    }
    .abstract-title,
    .section-title {
        font-weight: bold;
        margin-bottom: 10px;
    }
    .keywords {
        margin-top: 10px;
        font-style: italic;
    }
    .columns {
        column-count: 2;
        column-gap: 40px;
    }
    .column-separator {
        display: inline-block;
        width: 100%;
        border-bottom: 1px solid #000;
        margin: 20px 0;
    }

</style>
</head>
<body>
    <div class="paper">
        <div class="title">Narrative Visualization: Telling Stories with Data</div>
        <div class="authors">Edward Segel and Jeffrey Heer</div>
        <div class="abstract">
            <div class="abstract-title">Abstract</div>
            <p>
                <!-- Abstract text here -->
            </p>
            <div class="keywords">Index Terms—Narrative visualization, storytelling, design methods, case study, journalism, social data analysis.</div>
        </div>
        <div class="columns">
            <div class="section">
                <div class="section-title">1 Introduction</div>
                <p>
                    <!-- Introduction text here -->
                    The dataset "Police Department Incident Reports: Historical 2003 to May 2018" is a large and impressive dataset found on the San Francisco Government's data platform. This dataset includes crime incidents from the San Francisco Police Department from 2003 up to May 2018. It serves as a significant source of information regarding crime incidents which have been reported within the city limits during this period. The special part about this data is not just the mentioned incidents but also all of the exciting parameters and information included for each crime incident. All these supplementary parameters about each crime incident give us a much deeper insight into how the incidents took place in all those years in San Fransisco. This type of information could help in both predictive policing in order to improve the safety of the city by using the data to increase the chance of correctly predicting crime behaviour in the city and also in terms of understanding the underlying issues in the city and to notice any exciting patterns across different parameters. 
                    
                    The dataset includes numerous fields that detail the specifics of each incident, such as the incident number, category, description, police district, location, and the date and time it occurred. Such information-heavy datasets are essential resources for researchers, politicians, and the police. Researchers can use such information to discover findings about the city's crime scene, and politicians and police can use the information when analyzing crime patterns and developing crime prevention strategies. 
                    
                    Furthermore, the availability of this dataset on a public government platform shows the government's commitment to transparency and accountability within the city's law enforcement operations. It empowers the city's citizens and can help improve public safety. A pivotal point to keep in mind is that even though that data is from 2003 to 2018, the 2018 data is only until May, so this is the reason why the amount of crime of that year might appear less in certain graphs when comparing years it might be better to look from 2003 to 2017.

                </p>
                <!-- More content here -->
            </div>
            <div class="column-separator"></div>
            <div class="section">
                <div class="section-title">2 Related Work</div>
                <p>
                    <!-- Related work text here -->
                </p>
                <!-- More content here -->
            </div>
            <!-- You can continue adding more sections within the columns div as needed -->
        </div>
    </div>

    <div class="paper">
        <div class="columns">
            <div class="section">
                <div class="section-title">2 Our story</div>
                <p>
                    <!-- Story text here -->
                    Our focus in this dataset and the data story we would like to talk about is the way the city has handled the prostitution which takes place in the city. We initially noticed a big decrease in the number of prostitution incidents in 2017 compared with 2008. We therefore decided we wanted to research this further to find out what the data can tell us about prostitution incidents between 2008 and 2017.
                </p>
                <embed type="text/html" src="/1.html" width="1100" height="400">
            </div>
        </div>
    </div>
</body>
</html>
