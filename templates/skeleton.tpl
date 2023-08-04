<!doctype html>
<html lang="en" class="h-100">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="author" content="Steve" >
    <title>{{title}}</title>
    % include('templates/head.tpl')

  </head>

  <body class="d-flex flex-column h-100">

    % include('templates/header.tpl', user_id=get("user_id", ""))

    <!-- Begin page content -->
    <main class="flex-shrink-0">
      <div class="container">
        {{!base}}
      </div>
    </main>

    % include('templates/footer.tpl')

    % include('templates/javascript.tpl', use_noback=get("use_noback", True))
  </body>

</html>
