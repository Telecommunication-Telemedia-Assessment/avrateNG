<html>
  <head>
    <title>{{title}}</title>
    % include('templates/header.tpl')
    <script>
      function get_plot_data(data_as_json){
        data_obj={} //bring data to appropriate structure for plotting

        for (var video_name in data_as_json) {
           data_obj[video_name]={y: data_as_json[video_name], name: video_name, type: 'box'};     
            console.log(data_obj)   
          }
      
        var plot_data = [] //create array to plot the data
        for (var item in data_obj) {
          plot_data.push(data_obj[item]);
          }
      return plot_data
      }
    </script>
  </head>
   

  <body>
    <!--Div that will hold the chart-->
    <div id="slider_boxplot">
      <script> 
        var json_data = {{ !rating_dict }}; // get json Data from server
  
        var layout_slider = { //set layout
          title: 'Boxplot showing slider ratings depending on video',
          yaxis: {
            title: 'Slider rating',
            zeroline: false,
            range: [0,100]
            },
          };
        var plot_data = get_plot_data(json_data['slider'])
        Plotly.newPlot("slider_boxplot", plot_data, layout_slider); //plot the data
    </script> </div> 
    <br>
    <div id="radio_boxplot">
      <script> 
        var json_data = {{ !rating_dict }}; // get json Data from server

        var layout_radio = { //set layout
          title: 'Boxplot showing radio ratings depending on video',
          yaxis: {
            title: 'Radio rating',
            zeroline: false,
            range: [1,5]
            },
          };
        var plot_data = get_plot_data(json_data['radio']);
        Plotly.newPlot("radio_boxplot", plot_data, layout_radio); //plot the data
      </script>
    </div>


    

    


    
    

  </body>

</html>
