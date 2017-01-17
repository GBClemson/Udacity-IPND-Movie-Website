import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        .trailer-container{
            float:left;
            width: 70%;
            height: 100%;
        }        
        .storyline {
            /*Submitter Greg Bopp has added this class selector to display a synopsis of the movie in the trailer popup window*/
            float: left;
            width: 28%;
            height: 72%;
            line-height: 3em;
            overflow:auto;
            background-color:black;
            color: white;
            margin: 5px,5px,5px,0px;
            padding: 5px;
            border-left: 1px solid white;
        }
        #trailer-video {
            float:left;
            width: 70%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .info_container{/*This class was added by Greg Bopp to create a container that will show release year and age rating for each movie entry*/
            /*display: block;*/
            width: 100%;    
        }
        .year{/*This class was added by Greg Bopp to dispaly Release year for each movie entry*/
            float: left;
            width: 40%
        }
        .rating{/*This class was added by Greg Bopp to dispaly the age rating for each movie entry*/
            float: right;
            width: 40%
        }
        .scale-media {
            background-color: black;
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            background-color: black;
            border: none;
            height: 100%;
            position: absolute;
            width: 70%;
            left: 0;
            top: 0;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened        
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            // The next line of code was added siply as a check to see if I am getting a variable value from my python file to the trailer popup window
            window.alert("The YouTubeId value in JS is "+trailerYouTubeId); 
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=0&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media">
            <div class="trailer-container" id="trailer-video-container"></div>
            <div class="storyline">
              <h5>"generic text placeholder that should ultimately be a movie synopsis from my python file appearing next to the movie trailer still
              that is to the left right now. Yes this is excessive amounts of unimportant text"</h5>
              <br><h5><b>CLICK THE VIDEO TO WATCH THE TRAILER</b></h5>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
    <div class="info_container"><!--This class was added by Greg Bopp to dispaly release year and age rating for each movie entry-->
        <p>{storyline_txt}</p>
        <div class="year">{year}</div><div class="rating">{rating}</div>
    </div>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        storyline_txt=movie.storyline
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
        #print("The current movie storyline is "+storyline_txt+".")
        #print("The movie has a trailer_youtube_id value in our python DEF of "+trailer_youtube_id)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            year=movie.year, rating=movie.rating, #year and rating was added to display release year and age rating for each movie entry
            storyline_txt=storyline_txt,
        )
        
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
