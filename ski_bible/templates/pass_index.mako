<!DOCTYPE html>
<html lang="${request.locale_name}">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="pyramid web application">
    <meta name="author" content="Pylons Project">
    <link rel="shortcut icon" href="${request.static_url('ski_bible:static/pyramid-16x16.png')}">

    <title>Pass Index</title>

    <!-- Bootstrap core CSS -->
    <!--<link href="//oss.maxcdn.com/libs/twitter-bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet"> -->
    <link rel="stylesheet" type="text/css" href="//maxcdn.bootstrapcdn.com/bootswatch/3.2.0/paper/bootstrap.min.css">
    <script type="text/javascript" src="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>

    <!-- Custom styles for this scaffold -->
    <link href="${request.static_url('ski_bible:static/theme.css')}" rel="stylesheet"

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="//oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="//oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>
    <div class="container">
      <div class="row">
        <h1>I see you've found the pass index</h1>
      </div>
      <div class="row">
        <table class="table table-striped table-hover">
          <thead>
            <tr>
              <th>ID</th>
              <th>UID</th>
              <th>Speed</th>
              <th>Line</th>
              <th>Count</th>
              <th>Division</th>
              <th>Date</th>
            </tr>
          </thead>
          <tbody>
            % for row in passes:
              <tr>
                <td>${row['id']}</td>
                <td>${row['uid']}</td>
                <td>${row['speed']}</td>
                <td>${row['line']}</td>
                <td>${row['count']}</td>
                <td>${row['division']}</td>
                <td>${row['date']}</td>
              </tr>
            % endfor
          </tbody>
        </table>
      </div>
    </div>
  </body>
</html>

