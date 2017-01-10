$('.collapse').on('show.bs.collapse', function(){
      var i = $(this).parent().find('#caret')
      i.toggleClass('fa-caret-down fa-caret-up');
    }).on('hide.bs.collapse', function(){
      var i = $(this).parent().find('#caret')
      i.toggleClass('fa-caret-up fa-caret-down');
    });



// Facebook Share button popup
    function fbShare(url, title, descr, image, winWidth, winHeight) {
        var winTop = (screen.height / 2) - (winHeight / 2);
        var winLeft = (screen.width / 2) - (winWidth / 2);
        window.open('http://www.facebook.com/sharer.php?s=100&p[title]=' + title + '&p[summary]=' + descr + '&p[url]=' + url + '&p[images][0]=' + image, 'sharer', 'top=' + winTop + ',left=' + winLeft + ',toolbar=0,status=0,width=' + winWidth + ',height=' + winHeight);
    }


// Twitter share button popup
$('a.tweet').click(function(e){
  //We tell our browser not to follow that link
  e.preventDefault();
  //We get the URL of the link
  var loc = $(this).attr('href');
  //We get the title of the link
  var title  = escape($(this).attr('title'));
  //We trigger a new window with the Twitter dialog, in the middle of the page
  window.open('http://twitter.com/share?url=' + loc + '&text=' + title + '&', 'twitterwindow', 'height=450, width=550, top='+($(window).height()/2 - 225) +', left='+$(window).width()/2 +', toolbar=0, location=0, menubar=0, directories=0, scrollbars=0');
});