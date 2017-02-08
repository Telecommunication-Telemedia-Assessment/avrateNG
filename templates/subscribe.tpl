<!DOCTYPE html>
<html>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="Steve Göring">
  <head>
    <title>{{title}}</title>
    % include('templates/header.tpl')
  </head>

  <body>
      <div class="container">
        % include('templates/nav.tpl')

        <div class="row marketing">
          <div class="col-lg-6">
          <h4>subscribe <small>to MensaBot+</small></h4>
          {{!msg}}
          <form class="form-inline" method="post" action="subscribe" >
            <ul>
              <li><input name="email" type="email" class="form-control" placeholder="email@provider.com"
                  % if email != "":
                    value={{email}}
                  % end
                  >
              </li>
              <li><div class="input-group">
                    <span class="input-group-addon">
                      % for m in sorted(mensas.keys()):
                        <input type="checkbox" aria-label="test" value="{{mensas[m]}}"> {{m}}
                      % end
                    </span>
                  </div>
              <li>notification time</li>

              <li><input name="time" type="text" class="form-control" placeholder="12:00"
                  % if time != "":
                    value={{time}}
                  % end
                  ></li>

              <li><button type="submit" class="btn btn-primary">subscribe</button></li>
            </ul>
          </form>
          </div>
        </div>

        % include('templates/footer.tpl')
      </div>

  </body>

</html>