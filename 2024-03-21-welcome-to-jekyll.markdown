---
layout: page
title: Assignment 2
---

<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Academic Papers Collection</title>
    <style>
        body {
            font-family: 'Times New Roman', serif;
            margin: 40px;
        }

        .paper {
            border: 1px solid #000;
            padding: 20px;
            margin-bottom: 40px;
        }

        .title,
        .authors {
            text-align: center;
        }

        .title {
            font-size: 24px;
            text-transform: uppercase;
        }

        .authors {
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
                This paper delves into the "Police Department Incident Reports: Historical 2003 to May 2018" dataset to explore the intricacies of crime incidents within San Francisco. Through a comprehensive analysis, we aim to uncover patterns and insights that could aid in predictive policing and offer a deeper understanding of the city's dynamics over the studied period.
            </p>
            <div class="keywords">Index Terms—Narrative visualization, storytelling, design methods, case study, journalism, social data analysis.</div>
        </div>
        <div class="columns">
            <div class="section">
                <div class="section-title">1 Introduction</div>
                <p>
                    The dataset "Police Department Incident Reports: Historical 2003 to May 2018" includes crime incidents from the San Francisco Police Department from 2003 up to May 2018. It serves as a significant source of information for analyzing crime incidents within the city limits during this period, providing a deep insight into the city's crime dynamics through various parameters associated with each incident.
                </p>
            </div>
            <div class="column-separator"></div>
            <div class="section">
                <div class="section-title">2 Our Story on Prostitution Trends</div>
                <p>
                    Our analysis reveals a notable decrease in prostitution incidents from 2008 to 2017. This study explores the underlying factors contributing to this decline and examines the effectiveness of the city's strategies in managing such incidents.
                </p>
            </div>
        </div>

        <div class="section">
            <div class="section-title">3 Data Visualization Insights</div>
            <p>
                Our visual analysis includes a time series bar chart showing the year-on-year changes in prostitution incidents, highlighting a consistent decrease. Additionally, pie charts by district offer insights into geographical shifts in these incidents, pointing to significant reductions in specific areas while others show an increase.
            </p>
        </div>
    </div>

</body>
</html>
