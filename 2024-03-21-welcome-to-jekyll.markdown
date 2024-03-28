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
</body>
</html>
