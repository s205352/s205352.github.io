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
        <div class="title">A short data story - prostitution in San Francisco</div>
        <div class="authors">Rohan Khalid and Shiv Gopal</div>
        <div class="abstract">
            <div class="abstract-title">Abstract</div>
            <p>
                This paper delves into the "Police Department Incident Reports: Historical 2003 to May 2018" dataset to explore the intricacies of crime incidents for prostitution within San Francisco. Through a comprehensive analysis, we aim to uncover patterns and insights that could aid in predictive policing and offer a deeper understanding of the city's dynamics over the studied period.
            </p>
            <div class="keywords">Index Terms—Narrative visualization, storytelling, design methods, case study, journalism, social data analysis.</div>
        </div>
        <div class="columns">
            <div class="section">
                <div class="section-title">1 Introduction</div>
                <p>
                    The dataset "Police Department Incident Reports: Historical 2003 to May 2018" is a large and impressive dataset found on the San Francisco Government's data platform. This dataset includes crime incidents from the San Francisco Police Department from 2003 up to May 2018. It serves as a significant source of information regarding crime incidents which have been reported within the city limits during this period. The special part about this data is not just the mentioned incidents but also all of the exciting parameters and information included for each crime incident. All these supplementary parameters about each crime incident give us a much deeper insight into how the incidents took place in all those years in San Fransisco. This type of information could help in both predictive policing in order to improve the safety of the city by using the data to increase the chance of correctly predicting crime behaviour in the city and also in terms of understanding the underlying issues in the city and to notice any exciting patterns across different parameters. 
                    
                    The dataset includes numerous fields that detail the specifics of each incident, such as the incident number, category, description, police district, location, and the date and time it occurred. Such information-heavy datasets are essential resources for researchers, politicians, and the police. Researchers can use such information to discover findings about the city's crime scene, and politicians and police can use the information when analyzing crime patterns and developing crime prevention strategies. 
                    
                    Furthermore, the availability of this dataset on a public government platform shows the government's commitment to transparency and accountability within the city's law enforcement operations. It empowers the city's citizens and can help improve public safety. A pivotal point to keep in mind is that even though that data is from 2003 to 2018, the 2018 data is only until May, so this is the reason why the amount of crime of that year might appear less in certain graphs when comparing years it might be better to look from 2003 to 2017.
                </p>
            </div>
            <div class="section">
                <div class="section-title">2 Our Story on Prostitution Trends</div>
                <p>
                    Our focus in this dataset and the data story we would like to talk about is the way the city has handled the prostitution which takes place in the city. We initially noticed a big decrease in the number of prostitution incidents in 2017 compared with 2008. We therefore decided we wanted to research this further to find out what the data can tell us about prostitution incidents between 2008 and 2017.
                </p>
            </div>
        </div>
    <div class="column-separator"></div>
    <div class="section-title">3 Data Visualizations</div>
    <embed type="text/html" src="/1.html" width="800" height="400">
        <div class="columns">
        <div class="section-title">3.1 Bar chart time-series</div>
            <div class="section">
                <p>
                    The first visualization we will look at is a time series bar chart. This plot contains the years from 2008 to 2017 on the x-axis and the number of prostitution incidents for each year on the y-axis. What we can see here is, first of all, a validation of our initial observation that prostitution is less in 2017 compared to 2008. What is more interesting is that there is almost a steady yearly decrease in all the years in between. This tells us that not only are prostitution incidents being reported less in 2017 than in 2008, but also that there has been a somewhat consistent decrease in the number of prostitution incidents in each year, with some minor outliers. This seems like it is going correctly, and the city is doing well.
                </p>
            </div>
        </div>
    <div class="column-separator"></div>
        <div class="columns">
        <div class="section-title">3.2 Pie charts for police districts</div>
            <div class="section">
                <p>
                    The second visualization also looks at prostitution incidents for each year. However, we are now utilizing our information on which district it takes place and have visualized it in a pie chart. The reason for this is that we already know that the overall number of prostitution incidents is almost decreasing each year, but how? Do all districts have much less prostitution, or are just some of the districts the reason for this? When looking at the pie charts for each year, it is clear that the decrease in prostitution incidents is heavily due to certain districts. Mission had the most incidents in the first year at 702, and it has been on quite a rollercoaster such as in 2009 where it made up almost 3/4 of all prostitution incidents. However, it reached 214 in 2017, even less than the previous year, so Mission has decreased the overall number. The same can be said for the following districts: Northern, Tenderloin (which has almost eliminated prostitution from 226 to 8 incidents from 2008 till 2017). However, some districts were almost non-existent in the earlier pie chart, which indicates that compared to the rest of the districts, not a lot of prostitution was taking place, but now they are filling more of the pie chart and have more incidents. This can be said about Tereval and Southern. Some also stayed pretty consistent. Overall, based on the overall numbers, we can however say that prostitution incidents have steadily been decreasing, but that that is not the case in all districts and that there are certain districts which play a big role in this decrease..
                </p>
            </div>
        </div>
        <embed type="text/html" src="/2.html" width="800" height="2000">
    <div class="column-separator"></div>
        <div class="columns">
        <div class="section-title">3.3 Map over incidents in districts</div>
            <div class="section">
                <p>
                    The third visualization is quite similar to the second one; the difference here is that we are using a district map instead of pie charts, and instead of having multiple pie charts, we have one map which animates the yearly  difference in the number of prostitution incidents by giving different colours to the districts in the map. This map, of course, showcases the same tendencies as described earlier. Still, it is a good way to visually understand where the issues have been the largest and the smallest in San Francisco, as described earlier (this can also be seen by holding the mouse over the districts). Furthermore, this also shows that generally, the number of prostitution has decreased, especially in some areas.
                </p>
            </div>
        </div>
        <embed type="text/html" src="/3.html" width="700" height="400">
    <div class="column-separator"></div>
        <div class="columns">
        <div class="section-title">End of our short story</div>
            <div class="section">
                <p>
                    The second visualization also looks at prostitution incidents for each year. However, we are now utilizing our information on which district it takes place and have visualized it in a pie chart. The reason for this is that we already know that the overall number of prostitution incidents is almost decreasing each year, but how? Do all districts have much less prostitution, or are just some of the districts the reason for this? When looking at the pie charts for each year, it is clear that the decrease in prostitution incidents is heavily due to certain districts. Mission had the most incidents in the first year at 702, and it has been on quite a rollercoaster such as in 2009 where it made up almost 3/4 of all prostitution incidents. However, it reached 214 in 2017, even less than the previous year, so Mission has decreased the overall number. The same can be said for the following districts: Northern, Tenderloin (which has almost eliminated prostitution from 226 to 8 incidents from 2008 till 2017). However, some districts were almost non-existent in the earlier pie chart, which indicates that compared to the rest of the districts, not a lot of prostitution was taking place, but now they are filling more of the pie chart and have more incidents. This can be said about Tereval and Southern. Some also stayed pretty consistent. Overall, based on the overall numbers, we can however say that prostitution incidents have steadily been decreasing, but that that is not the case in all districts and that there are certain districts which play a big role in this decrease..
                </p>
            <div class="section-title">News stories from the area</div>
            <div class="section">
                <p>
                    The second visualization also looks at prostitution incidents for each year. However, we are now utilizing our information on which district it takes place and have visualized it in a pie chart. The reason for this is that we already know that the overall number of prostitution incidents is almost decreasing each year, but how? Do all districts have much less prostitution, or are just some of the districts the reason for this? When looking at the pie charts for each year, it is clear that the decrease in prostitution incidents is heavily due to certain districts. Mission had the most incidents in the first year at 702, and it has been on quite a rollercoaster such as in 2009 where it made up almost 3/4 of all prostitution incidents. However, it reached 214 in 2017, even less than the previous year, so Mission has decreased the overall number. The same can be said for the following districts: Northern, Tenderloin (which has almost eliminated prostitution from 226 to 8 incidents from 2008 till 2017). However, some districts were almost non-existent in the earlier pie chart, which indicates that compared to the rest of the districts, not a lot of prostitution was taking place, but now they are filling more of the pie chart and have more incidents. This can be said about Tereval and Southern. Some also stayed pretty consistent. Overall, based on the overall numbers, we can however say that prostitution incidents have steadily been decreasing, but that that is not the case in all districts and that there are certain districts which play a big role in this decrease..
                </p>
            </div>
            </div>
        </div>
    <div class="column-separator"></div>
        <div style="text-align: left;">
        <div class="section-title">References</div>
            <div class="section">
                <p>
                    <a href="https://www.example.com">Visit Example</a>
                </p>
            </div>
        </div>
    </div>
</body>
</html>
