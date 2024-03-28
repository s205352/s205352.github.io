<!DOCTYPE html>
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
        .title, .authors {
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
        .abstract, .section {
            margin-top: 30px;
        }
        .abstract-title, .section-title {
            font-weight: bold;
            margin-bottom: 10px;
        }
        .keywords {
            margin-top: 10px;
            font-style: italic;
        }
        .navigation {
            text-align: center;
            margin-bottom: 20px;
        }
        .navigation a {
            padding: 10px;
            text-decoration: none;
            color: #000;
            border: 1px solid #000;
            margin: 5px;
        }
    </style>
</head>
<body>

    <div class="navigation">
        <a href="#paper1">Page 1</a>
        <a href="#paper2">Page 2</a>
        <a href="#paper3">Page 3</a>
    </div>

    <div id="paper1" class="paper">
        <div class="title">Narrative Visualization: Telling Stories with Data</div>
        <div class="authors">Edward Segel and Jeffrey Heer</div>
        <div class="abstract">
            <div class="abstract-title">Abstract</div>
            <p>
                <!-- Abstract text here -->
            </p>
            <div class="keywords">Index Terms—Narrative visualization, storytelling, design methods, case study, journalism, social data analysis.</div>
        </div>
        <div class="section">
            <div class="section-title">1 Introduction</div>
            <p>
                <!-- Introduction text here -->
            </p>
        </div>
        <!-- Other sections -->
    </div>

    <div id="paper2" class="paper">
        <div class="title">Analysis of Prostitution Incidents in San Francisco</div>
        <div class="authors">Author Name</div>
        <div class="abstract">
            <div class="abstract-title">Abstract</div>
            <p>
                <!-- Abstract text for Paper 2 -->
            </p>
            <div class="keywords">Index Terms—Data analysis, San Francisco, prostitution incidents.</div>
        </div>
        <div class="section">
            <div class="section-title">1 Our Story</div>
            <p>
                <!-- Story text for Paper 2 -->
            </p>
        </div>
        <!-- Other sections -->
    </div>

    <div id="paper3" class="paper">
        <div class="title">Title of Paper 3</div>
        <div class="authors">Author Name</div>
        <div class="abstract">
            <div class="abstract-title">Abstract</div>
            <p>
                <!-- Abstract text for Paper 3 -->
            </p>
            <div class="keywords">Index Terms—Keywords for Paper 3.</div>
        </div>
        <div class="section">
            <div class="section-title">1 Introduction</div>
            <p>
                <!-- Introduction text for Paper 3 -->
            </p>
        </div>
        <!-- Other sections -->
    </div>

</body>
</html>
