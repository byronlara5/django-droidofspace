(function($){
  

  $(function(){
	$('.button-collapse').sideNav({
      menuWidth: 240, // Default is 240
      edge: 'left', // Choose the horizontal origin
      closeOnClick: false // Closes side-nav on <a> clicks, useful for Angular/Meteor
    }

		
  );


    
    $('.slider').slider({
      full_width: false,
      height: 500,
      indicators: false,
      interval: 8000,
      transition: 500

    });

  

   $(document).ready(function(){
    // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
    $('.modal-trigger').leanModal();
  });

 
  
  $(document).ready(function(){
    $('.materialboxed').materialbox();
  });

 $('.parallax').parallax();
 
  }); // end of document ready
})(jQuery); // end of jQuery name space